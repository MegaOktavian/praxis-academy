# Dependency Injection (DI) Part 1

DI adalah istilah untuk membuat instance kelas tingkat atas, dan meneruskannya sebagai argumen penginisialisasi satu sama ain :

    class Api:
        def fetch_remote_data(self):
            print('Api called')
            return 42


    class BusinessLogic:
        def __init__(self, api: Api):
            self.api = api

        def do_stuff(self):
            api_result = self.api.fetch_remote_data()
            print(f'the api returned a result: {api_result}')
            # do something with the data and return a result

    # ---

    if __name__ == '__main__':
        api = Api()
        logic = BusinessLogic(api=api)

        # ...
        print(logic.do_stuff())

![0204](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-04/latihan/Screenshot%20from%202020-03-12%2000-06-41.png)

Install injector :

    pip install injector

![0204](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-04/latihan/Screenshot%20from%202020-03-12%2000-09-51.png)

Contoh yang lebih kompleks :

    class Api:
        def fetch_remote_data(self):
            print('Api called')
            return 42


    class BusinessLogic:
        def __init__(self, api: Api):
            self.api = api

        def do_stuff(self):
            api_result = self.api.fetch_remote_data()
            print(f'the api returned a result: {api_result}')
            # do something with the data and return a result

Menambahkan module dependensi, dimana kelas yang mewarisi dari injector.Module dan memiliki banyak metode.

    class AppModule(Module):

        @singleton
        @provider
        def provide_business_logic(self, api: Api) -> BusinessLogic:
            return BusinessLogic(api=api)

        @singleton
        @provider
        def provide_api(self) -> Api:
            # there is no complex logic in our case,
            # but you can use this method to hide the complexity of initial 
            configuration
            # e.g. when instantiating a particular DB connector.
            return Api()

Membuat injector dan mengirimnya :

    if __name__ == '__main__':
        injector = Injector(AppModule())

        logic = injector.get(BusinessLogic)
        logic.do_stuff()

Versi kelas API untuk tujuan pengujian :

    class TestApi(Api):
        def fetch_remote_data(self):
            print('Demo Api called')
            return 24

Dengan asumsi mungkin ada lebih banyak kelas, buatlah modul dependensi terpisah :

    class TestAppModule(Module):

        @singleton
        @provider
        def provide_api(self) -> Api:
            return TestApi()

Ketika membuat injektor, setiap instance injektor dapat dilengkapi dengan konfigurasi modul dependensi sebanyak yang diinginkan :

    if __name__ == '__main__':
        real_injector = Injector(AppModule())
        test_injector = Injector([AppModule(), TestAppModule()])

        real_logic = real_injector.get(BusinessLogic)
        real_logic.do_stuff()

        test_logic = test_injector.get(BusinessLogic)
        test_logic.do_stuff()


# Dependency Injection (DI) Part 2

DI mendefinisikan sumber daya dependen dan menyediakan cara untuk membuat instance atau membuatnya secara eksternal.

    Jika objek A tergantung pada onjek B, objek A tidak boleh membuat objek impor B secara langsung. Objek A harus menyediaka n cara untuk menyuntikkan objek B. Tanggung jawab atas pembuatan objek dan injeksi dependensi didelegasikan ke kode eksternal.

### Mengapa Menggunakan Dependency Injection ?

1. Fleksibilitas komponen yang dapat  dikonfigurasi - Krena komponen dikonfigurasi secara eksternal, dapat etrdapat berbagai definisi untuk suatu komponen.
2. Membuat pengujian menjadi mudah - Instantiating objek tiruan dan mengintegrasikan dengan definisi kelas lebih mudah.
3. Kohesi tinggi - Kode dengan kompleksitas modul berkurang, peningkatan usabilitas modul.
4. Minimalis dependensi - Karena dependensi didefinisikan dengan jelas, lebih mudah untuk mengilangkan / mengurangi dependensi yang tidak perlu.

Contoh berikut menunjukkan penggunaan dan implementasi DI dengan python. Buatlah file bernama email_client.py  yang berisi kelas __Email Client__ yang bergantung pada objek __konfigurasi__ :

    class EmailClient(object):
        
        def __init__(self, config):
            self._config = config
            self.connect(self._config)
            
        def connect(self, config):
            # Implement function here
            pass

Buat file baru bernama  email_reader.py yang berisi kelas EmailReader dan bergantung pada objek EmailClient :

    class EmailReader(object):
        
        def __init__(self, client):
            try:
                self._client = client
            except Exception as e:
                raise e
                
        def read(self):
            # Implement function here
            pass
    view raw

Untuk mendefinisikan dependensi diatas secara eksternal, buat file bernama containers.py. Import paket dependency_injector dan kelas untuk digunakan :

    from dependency_injector import providers, containers
    from email_client import EmailClient
    from email_reader import EmailReader

Tambahkan kelas Configs ke file. Kelas ini adalah eadah dengan penyedia konfigurasi yang menyediakan semua objek konfigurasi.

    class Configs(containers.DeclarativeContainer):
        config = providers.Configuration('config')
        # other configs

Tambahkan kelas Client. Kelas ini adalah wadah yang mendefinisikan semua jenis klien. EmailClient dibuat dengan penyedia tunggal, menyatakan satu instance dari kelas ini dan mendefinisikan dependensi pada objek config.

    class Clients(containers.DeclarativeContainer):
        email_client = providers.Singleton(EmailClient, Configs.config)
        # other clients 

Tambahkan kelas Readers. Kelas ini mendefinisikan dependensi EmailReader kelas pada kelas EmailClient.

    class Readers(containers.DeclarativeContainer):
        email_reader = providers.Factory(EmailReader, client=Clients.email_client)
        # other readers 

Buat file main.py untuk menjalankannya :

    from containers import Readers, Clients, Configs

    if __name__ == "__main__":
        Configs.config.override({
            "domain_name": "imap.gmail.com",
            "email_address": "YOUR_EMAIL_ADDRESS",
            "password": "YOUR_PASSWORD",
            "mailbox": "INBOX"
        })
        email_reader = Readers.email_reader()
        print email_reader.read()

Dalam file main.py, objek config ditimpa dengan objek kamus yang diberikan. Kelas EmailReader adalah instantiated tanpa membuat instance kelas EmailClient dalam file utama, menghapus overhead mengimpor atau membuatnya. Bagian itu diurus dengan file kontainer.