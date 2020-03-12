# Concurrency

    Konkurensi adalah kejadian simultan.

Threading dan asyncio keduanya berjalan pada satu prosesor dan karenanya hanya menjalankan satu per satu. Mereka secara cerdik menemukan cara untuk bergiliran mempercepat proses keseluruhan. Meskipun mereka tidak menjalankan berbagai train secara bersamaan, ini disebut konkurensi.

Cara thread atau task bergiliran adalah perbedaan besar antara threading dan asyncio. Dalam threading, sistem operasi benar-benar tahu tentang setiap thread dan dapat menghentikannya kapan saja untuk mulai menjalankan thread yang berbeda. Ini disebut pre-emptive multitasking karena sistem operasi dapat mencegah thread untuk beralih.

Pre-emptive multitasking berguna karena kode di thread tidak perlu melakukan apa pun untuk beralih. Ini juga bisa sulit karena ungkapan "kapan saja". Switch ini dapat terjadi di tengah-tengah pernyataan Python tunggal, bahkan yang sepele seperti x = x + 1.

Asyncio, di sisi lain, menggunakan multitasking kooperatif. task-task harus bekerja sama dengan mengumumkan kapan mereka siap untuk keluar. Itu berarti bahwa kode dalam task harus sedikit berubah untuk mewujudkan hal ini.

### Paralelisme

Dengan multiprocessing, Python menciptakan proses baru. Suatu proses di sini dapat dianggap sebagai program yang hampir sama sekali berbeda, meskipun secara teknis mereka biasanya didefinisikan sebagai kumpulan sumber daya di mana sumber daya termasuk memori, pegangan file, dan hal-hal seperti itu. Salah satu cara untuk memikirkannya adalah bahwa setiap proses berjalan dengan interpreter Python sendiri.

Perbedaan Konkurensi dan Paralelisme

Jenis konkurensi | Pengalihan Keputusna | Jumlah Prosesor 
---------------- | -------------------- | ---------------
Pre-emptive multitasking (threading) | Sistem operasi memutuskan kapan harus beralih task eksternal ke Python. | 1
Cooperative multitasking (asyncio) | task memutuskan kapan harus menyerahkan kontrol. | 1

Multiprocessing (multiprocessing)_| Semua proses berjalan pada waktu yang sama pada prosesor yang berbeda. | Many


Concurrency dapat membuat perbedaan besar untuk dua jenis masalah. Ini disebut CPU-bound dan I/O-bound.

Masalah I/O-bound menyebabkan program  melambat karena sering harus menunggu input / output (I/ ) dari beberapa sumber daya eksternal. Mereka sering muncul ketika program Anda bekerja dengan hal-hal yang jauh lebih lambat daripada CPU.

Contoh hal yang lebih lambat dari CPU Anda banyak, tetapi program Anda untungnya tidak berinteraksi dengan sebagian besar dari mereka. Hal-hal lambat yang akan paling sering berinteraksi dengan program Anda adalah sistem file dan koneksi jaringan.

Mari kita lihat seperti apa tampilannya:

![0203]()

Dalam diagram di atas, kotak biru menunjukkan waktu ketika program  sedang bekerja, dan kotak merah dihabiskan untuk menunggu operasi I/O selesai. Diagram ini bukan untuk mengukur karena request di internet dapat mengambil beberapa pesanan lebih besar dari instruksi CPU, sehingga program dapat menghabiskan sebagian besar waktunya menunggu.

Di sisi lain, ada kelas program yang melakukan perhitungan signifikan tanpa berbicara dengan jaringan atau mengakses file. Ini adalah program yang terikat CPU, karena sumber daya yang membatasi kecepatan program Anda adalah CPU, bukan jaringan atau sistem file.

Berikut diagram yang sesuai untuk program yang terikat CPU :

![0203]()

Saat mengerjakan contoh berikut, akan terlihat bahwa berbagai bentuk konkurensi berfungsi lebih baik atau lebih buruk dengan program yang terikat CPU dan I/O. Menambahkan konkurensi ke program menambah kode dan komplikasi tambahan, jadi harus memutuskan apakah potensi percepatan sebanding dengan upaya ekstra. 

Berikut ringkasan singkat untuk memperjelas konsep ini :

I/O-Bound Process | CPU-Bound Process
----------------- | ----------------- 
Program menghabiskan sebagian besar waktunya berbicara dengan perangkat yang lambat, seperti koneksi jaringan, hard drive, atau printer. | Program menghabiskan sebagian besar waktunya melakukan operasi CPU.
Mempercepatnya mencakup tumpang tindih waktu yang dihabiskan untuk menunggu perangkat ini. | Mempercepatnya berarti menemukan cara untuk melakukan lebih banyak perhitungan dalam jumlah waktu yang sama.

## Cara Mempercepat Program I/O-Bound

Mari fokus pada program terikat I/O dan masalah umum mengunduh konten melalui jaringan. Sebagai contoh, akan mengunduh halaman web dari beberapa situs, tetapi sebenarnya itu bisa berupa lalu lintas jaringan apa pun. Lebih mudah untuk memvisualisasikan dan mengatur dengan halaman web.

### Synchronous Version

Perhatikan bahwa program ini membutuhkan modul request. Menjalankan request :

    pip install requests

![0203]()

Versi ini tidak menggunakan konkurensi sama sekali:

    import requests
    import time

    def download_site(url, session):
        with session.get(url) as response:
            print(f"Read {len(response.content)} from {url}")


    def download_all_sites(sites):
        with requests.Session() as session:
            for url in sites:
                download_site(url, session)


    if __name__ == "__main__":
        sites = [
            "https://www.jython.org",
            "http://olympus.realpython.org/dice",
        ] * 80
        start_time = time.time()
        download_all_sites(sites)
        duration = time.time() - start_time
        print(f"Downloaded {len(sites)} in {duration} seconds")

![0203]()

download_site () hanya mengunduh konten dari URL dan mencetak ukurannya. Dimungkinkan untuk menggunakan get() dari request secara langsung, tetapi membuat objek Session memungkinkan request untuk melakukan beberapa trik jaringan yang bagus dan benar-benar mempercepat.

download_all_sites() membuat Session dan kemudian menelusuri daftar situs, mengunduh masing-masing secara bergantian.

### Masalah dengan Synchronous Version

Masalah besar di sini adalah relatif lambat dibandingkan dengan solusi lain yang tersedia. Berikut ini contoh dari apa hasil akhir yang diberikan pada mesin saya:

    $ ./io_non_concurrent.py
    [most output skipped]
    Downloaded 160 in 14.289619207382202 seconds

### threading Version

Tampilan program yang sama dengan threading :

    import concurrent.futures
    import requests
    import threading
    import time


    thread_local = threading.local()


    def get_session():
        if not hasattr(thread_local, "session"):
            thread_local.session = requests.Session()
        return thread_local.session


    def download_site(url):
        session = get_session()
        with session.get(url) as response:
            print(f"Read {len(response.content)} from {url}")


Saat Anda menambahkan threading, struktur keseluruhannya sama dan hanya perlu membuat beberapa perubahan. download_all_sites () berubah dari memanggil fungsi satu kali per situs ke struktur yang lebih kompleks.

    ThreadPoolExecutor = Thread + Pool + Executor.

Objek Pool akan membuat kumpulan benang, yang masing - masing dapat berjalan secara bersamaan. Akhirnya, Executor adalah bagian yang akan mengontrol bagaimana dan kapan setiap thread di Pool akan berjalan. Ini akan mengeksekusi request di Pool.

Mengimplementasikan ThreadPoolExecutor sebagai manajer konteks dapat menggunakan sintaks with untuk mengelola membuat dan membebaskan kumpulan Thread.

Metode .map() menjalankan fungsi yang diteruskan pada setiap situs dalam daftar. Ia secara otomatis menjalankannya secara bersamaan menggunakan kumpulan thread yang dikelolanya.

Threading.local() membuat objek yang terlihat seperti global tetapi spesifik untuk setiap thread individu. Dalam contoh, ini dilakukan dengan threadLocal dan get_session() :

    threadLocal = threading.local()

    def get_session():
        if not hasattr(threadLocal, "session"):
            threadLocal.session = requests.Session()
        return threadLocal.session


ThreadLocal ada dalam modul threading untuk secara khusus menyelesaikan masalah ini. Saat get_session() dipanggil, session yang dihadapinya khusus untukthread thread khusus yang digunakannya. Jadi setiap thread akan membuat satu session saat pertama kali memanggil get_session() dan kemudian hanya akan menggunakan session itu pada setiap panggilan berikutnya sepanjang masa pakainya.

Inilah pengujian tercepat saya. Ingat bahwa versi non-konkuren membutuhkan waktu lebih dari 14 detik :

    $ ./io_threading.py
    [most output skipped]
    Downloaded 160 in 3.7238826751708984 seconds

Seperti apa diagram waktu pelaksanaannya :

![0203]()

### Masalah dengan Versi threading.

Thread dapat berinteraksi dengan cara yang halus dan sulit dideteksi. Interaksi ini dapat menyebabkan kondisi ras yang sering mengakibatkan bug acak dan intermiten yang mungkin cukup sulit ditemukan. 

### asyncio Version

#### asyncio Basics

Konsep umum asyncio adalah bahwa objek Python tunggal, yang disebut loop event mengontrol bagaimana dan kapan setiap task dijalankan. Loop event menyadari setiap task dan mengetahui keadaan apa yang ada di dalamnya. Pada kenyataannya, ada banyak keadaan yang bisa menjadi task, tetapi untuk sekarang mari kita bayangkan loop event yang disederhanakan yang hanya memiliki dua keadaan.

    Status siap akan menunjukkan bahwa task harus dikerjakan dan siap dijalankan, dan status menunggu berarti task menunggu beberapa hal eksternal selesai, seperti operasi jaringan.

loop event yang disederhanakan menyimpan dua daftar task, satu untuk masing-masing status ini. Ini memilih salah satu task siap dan mulai kembali berjalan. task itu berada dalam kendali penuh sampai secara kooperatif menyerahkan kontrol kembali ke loop event.

Ketika task yang berjalan memberikan kontrol kembali ke loop event, loop event menempatkan task itu ke dalam daftar siap atau tunggu dan kemudian menelusuri setiap task dalam daftar tunggu untuk melihat apakah sudah siap oleh operasi I/O. Ia tahu bahwa task-task dalam daftar siap masih siap karena ia tahu mereka belum berjalan.

Setelah semua task diurutkan ke dalam daftar yang benar lagi, loop event memilih task berikutnya untuk dijalankan, dan proses berulang. loop event yang disederhanakan memilih task yang telah menunggu paling lama dan menjalankannya. Proses ini berulang hingga loop event selesai.

__Poin penting dari asyncio adalah bahwa task-task tidak pernah melepaskan kendali tanpa sengaja melakukannya.__ 

#### async dan wait

Paling mudah untuk menganggap async sebagai flag ke Python yang memberitahukannya bahwa fungsi yang akan didefinisikan menggunakan wait. Ada beberapa kasus di mana ini tidak sepenuhnya benar, seperti generator asinkron, tetapi berlaku untuk banyak kasus dan memberi model sederhana saat memulainya.

Satu pengecualian untuk ini yang akan dilihat dalam kode selanjutnya adalah async dengan pernyataan, yang membuat manajer konteks dari objek yang biasanya Anda tunggu. Meskipun semantiknya sedikit berbeda, idenya sama yaitu untuk menandai manajer konteks ini sebagai sesuatu yang bisa dihapus.

#### Kembali ke Kode

Menjalankan 
    
    pip install aiohttp 

sebelum menjalankannya :

    import asyncio
    import time
    import aiohttp


    async def download_site(session, url):
        async with session.get(url) as response:
            print("Read {0} from {1}".format(response.content_length, url))


    async def download_all_sites(sites):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in sites:
                task = asyncio.ensure_future(download_site(session, url))
                tasks.append(task)
            await asyncio.gather(*tasks, return_exceptions=True)


    if __name__ == "__main__":
        sites = [
            "https://www.jython.org",
            "http://olympus.realpython.org/dice",
        ] * 80
        start_time = time.time()
        asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
        duration = time.time() - start_time
        print(f"Downloaded {len(sites)} sites in {duration} seconds")


![0203]()

Versi ini sedikit lebih kompleks dari dua versi sebelumnya. Ini memiliki struktur yang serupa, tetapi ada sedikit lebih banyak pekerjaan yang mengatur task daripada menciptakan ThreadPoolExecutor.

#### download_site ()

download_site () di bagian atas hampir identik dengan versi threading dengan pengecualian kata kunci async pada baris definisi fungsi dan async dengan kata kunci ketika benar- benar memanggil session.get().

#### download_all_sites ()

download_all_sites () adalah tempat untuk melihat perubahan terbesar dari contoh threading.

Dapat berbagi session di semua task, sehingga session dibuat di sini sebagai manajer konteks. Task dapat berbagi session karena semuanya berjalan di thread yang sama. Tidak ada cara satu task bisa mengganggu yang lain saat session dalam kondisi buruk.

Di dalam manajer konteks itu, ia membuat daftar task menggunakan asyncio.ensure_future() yang juga menangani untuk memulai mereka. Setelah semua task dibuat, fungsi ini menggunakan asyncio.gather() untuk menjaga konteks session tetap hidup sampai semua task selesai.

Kode threading melakukan sesuatu yang mirip dengan ini, tetapi detailnya ditangani dengan mudah di ThreadPoolExecutor. Saat ini tidak ada kelas AsyncioPoolExecutor.

Namun, ada satu perubahan kecil tapi penting yang terkubur dalam perinciannya di sini. Dalam contoh threading tidak jelas berapa jumlah thread yang optimal.

Salah satu keunggulan asyncio adalah skalanya jauh lebih baik daripada threading. Setiap task membutuhkan sumber daya yang jauh lebih sedikit dan lebih sedikit waktu untuk membuat daripada thread, sehingga membuat dan menjalankan lebih dari itu berfungsi dengan baik. 

__main__

Sifat asyncio berarti harus memulai loop event dan memberi tahu task mana yang harus dijalankan. Bagian __main__ di bagian bawah file berisi kode untuk get_event_loop() dan kemudian run_until_complete(). Jika tidak ada yang lain, mereka telah melakukan pekerjaan luar biasa dalam menamai fungsi-fungsi itu.


#### Rocks Versi asyncio

Diagram waktu eksekusi terlihat sangat mirip dengan apa yang terjadi pada contoh threading. Hanya saja request I/O dilakukan dengan thread yang sama:

![0203]()

Kurangnya wrapper yang bagus seperti ThreadPoolExecutor membuat kode ini sedikit lebih kompleks daripada contoh threading. Ini adalah kasus di mana harus melakukan sedikit pekerjaan ekstra untuk mendapatkan kinerja yang jauh lebih baik.

Juga ada argumen umum bahwa harus menambahkan async dan menunggu di lokasi yang tepat adalah komplikasi tambahan. Untuk sebagian kecil, itu benar. Sisi lain dari argumen ini adalah memaksa untuk memikirkan kapan task yang diberikan akan diganti, yang dapat membantu Anda membuat desain yang lebih baik, lebih cepat.

Masalah penskalaan juga tampak besar di sini. Menjalankan contoh threading di atas dengan thread untuk setiap situs terasa lebih lambat daripada menjalankannya dengan sedikit thread. Menjalankan contoh asyncio dengan ratusan task sama sekali tidak memperlambatnya.

### Masalah dengan Versi asyncio

Ada beberapa masalah dengan asyncio. Memerlukan pustaka versi async khusus untuk mendapatkan manfaat penuh asycio. Seandainya baru saja menggunakan request untuk mengunduh situs, itu akan jauh lebih lambat karena request tidak dirancang untuk memberi tahu perulangan event yang diblokir. Masalah ini semakin kecil dan semakin kecil seiring berjalannya waktu dan lebih banyak library merangkul asyncio.

Masalah lain yang lebih halus adalah bahwa semua keuntungan multitasking kooperatif dibuang jika salah satu task tidak bekerja sama. Kesalahan kecil dalam kode dapat menyebabkan task lari dan menahan prosesor untuk waktu yang lama, membuat kelaparan task lain yang perlu dijalankan. Tidak ada cara untuk loop event untuk masuk jika task tidak menyerahkan kontrol kembali ke sana.

### multiprocessing Version

Tidak seperti pendekatan sebelumnya, versi multiprosessionng dari kode mengambil keuntungan penuh dari banyak CPU yang dimiliki oleh komputer baru dan keren Anda. Kodenya :

    import requests
    import multiprocessing
    import time

    session = None


    def set_global_session():
        global session
        if not session:
            session = requests.Session()


    def download_site(url):
        with session.get(url) as response:
            name = multiprocessing.current_process().name
            print(f"{name}:Read {len(response.content)} from {url}")


    def download_all_sites(sites):
        with multiprocessing.Pool(initializer=set_global_session) as pool:
            pool.map(download_site, sites)


    if __name__ == "__main__":
        sites = [
            "https://www.jython.org",
            "http://olympus.realpython.org/dice",
        ] * 80
        start_time = time.time()
        download_all_sites(sites)
        duration = time.time() - start_time
        print(f"Downloaded {len(sites)} in {duration} seconds")

![0203]()

#### multiprocessing Code

Apa yang terjadi di sini adalah bahwa Pool menciptakan sejumlah proses juru bahasa Python yang terpisah dan masing-masing menjalankan fungsi yang ditentukan pada beberapa item di iterable, yang dalam kasus adalah daftar situs. Komunikasi antara proses utama dan proses lainnya ditangani oleh modul multiprosesor untuk Anda.

Garis yang menciptakan Pool patut diperhatikan. Pertama, itu tidak menentukan berapa banyak proses untuk dibuat di Pool, meskipun itu adalah parameter opsional. Secara default, multiprocessing.Pool() akan menentukan jumlah CPU di komputer dan cocok dengan itu. Ini seringkali merupakan jawaban terbaik, dan itu ada dalam kasus kami.

Untuk masalah ini, meningkatkan jumlah proses tidak membuat segalanya lebih cepat. Ini sebenarnya memperlambat segalanya karena biaya untuk menyiapkan dan menghancurkan semua proses itu lebih besar daripada manfaat melakukan request I/O secara paralel.

Selanjutnya kita memiliki bagian initializer = set_global_session dari panggilan itu. Ingatlah bahwa setiap proses di Pool memiliki ruang memori sendiri. Itu berarti bahwa mereka tidak dapat berbagi hal-hal seperti objek session.

Parameter fungsi initializer dibuat hanya untuk kasus ini. Tidak ada cara untuk mengembalikan nilai kembali dari penginisialisasi ke fungsi yang disebut oleh proses download_site(), tetapi Anda dapat menginisialisasi variabel session global untuk menahan session tunggal untuk setiap proses. Karena setiap proses memiliki ruang memori sendiri, global untuk masing-masing akan berbeda.

### Mengapa Rocks Versi multiprosessionng

Versi multiprosessionng dari contoh ini bagus karena relatif mudah disetel dan memerlukan sedikit kode tambahan. Ini juga mengambil keuntungan penuh dari daya CPU di komputer. Diagram waktu eksekusi untuk kode ini terlihat seperti ini :

![0203]()

### Masalah dengan Versi multiprosessionng

Versi contoh ini memang memerlukan beberapa pengaturan tambahan, dan objek session global aneh. Harus meluangkan waktu untuk memikirkan variabel mana yang akan diakses di setiap proses.

Akhirnya, jelas lebih lambat daripada versi asyncio dan threading dalam contoh ini :

    $ ./io_mp.py
        [most output skipped]
    Downloaded 160 in 5.718175172805786 seconds

### Cara Mempercepat Program Terikat CPU

Masalah I/O-terikat menghabiskan sebagian besar waktunya menunggu operasi eksternal, seperti panggilan jaringan, untuk menyelesaikan. Masalah yang terikat CPU, di sisi lain, melakukan beberapa operasi I / O, dan waktu eksekusi keseluruhannya merupakan faktor seberapa cepat dapat memproses data yang diperlukan. Fungsi ini menghitung jumlah kuadrat dari masing-masing angka dari 0 hingga nilai yang diteruskan :

    def cpu_bound(number):
        return sum(i * i for i in range(number))

Anda akan lulus dalam jumlah besar, jadi ini akan memakan waktu cukup lama. Ingat, ini hanyalah pengganti untuk kode Anda yang benar-benar melakukan sesuatu yang bermanfaat dan membutuhkan waktu pemrosesan yang signifikan, seperti menghitung akar persamaan atau menyortir struktur data yang besar.

### Versi Sinkronisasi CPU-Bound

Versi contoh yang tidak bersamaan :

    import time


    def cpu_bound(number):
        return sum(i * i for i in range(number))


    def find_sums(numbers):
        for number in numbers:
            cpu_bound(number)


    if __name__ == "__main__":
        numbers = [5_000_000 + x for x in range(20)]

        start_time = time.time()
        find_sums(numbers)
        duration = time.time() - start_time
        print(f"Duration {duration} seconds")

![0203]()

Kode ini memanggil cpu_bound() 20 kali dengan jumlah besar yang berbeda setiap kali. Semua ini dilakukan pada satu thread dalam satu proses pada satu CPU. Diagram waktu eksekusi terlihat seperti ini:

Timing Diagram dari Program Bound CPU

![0203]()

Tidak seperti contoh I/O-bound, contoh CPU-bound biasanya cukup konsisten dalam waktu menjalankannya. Yang ini membutuhkan waktu sekitar 7,8 detik pada mesin saya :

    $ ./cpu_non_concurrent.py
    Duration 7.834432125091553 seconds

### Versi threading dan asyncio

Dalam contoh I/O-bound, sebagian besar waktu keseluruhan dihabiskan untuk menunggu operasi yang lambat selesai. threading dan asyncio mempercepat ini dengan memungkinkan untuk tumpang tindih saat menunggu alih-alih melakukannya secara berurutan.

Namun, pada masalah yang terikat CPU, tidak perlu menunggu. CPU melakukan cranking secepat mungkin untuk menyelesaikan masalah. Dalam Python, kedua thread dan task berjalan pada CPU yang sama dalam proses yang sama. Itu berarti bahwa satu CPU melakukan semua pekerjaan kode non-konkuren ditambah kerja ekstra untuk mengatur thread atau task. Dibutuhkan lebih dari 10 detik :

    $ ./cpu_threading.py
    Duration 10.407078266143799 seconds

### Versi multiprosesor CPU-Bound

Berbeda dengan pustaka konkurensi lainnya, multiprosesor dirancang secara eksplisit untuk berbagi beban kerja CPU yang besar di banyak CPU. Seperti apa diagram waktu pelaksanaannya :

![0203]()

    import multiprocessing
    import time


    def cpu_bound(number):
        return sum(i * i for i in range(number))


    def find_sums(numbers):
        with multiprocessing.Pool() as pool:
            pool.map(cpu_bound, numbers)


    if __name__ == "__main__":
        numbers = [5_000_000 + x for x in range(20)]

        start_time = time.time()
        find_sums(numbers)
        duration = time.time() - start_time
        print(f"Duration {duration} seconds")

![0203]()

Harus mengimpor multiprocessing dan kemudian hanya mengubah dari perulangan melalui angka untuk membuat objek multiprocessing.Pool dan menggunakan metode .map() untuk mengirim nomor individu ke proses pekerja saat mereka menjadi bebas. Proses parameter opsional ke konstruktor multiprocessing.Pool () layak mendapat perhatian. Dapat menentukan berapa banyak objek Proses yang ingin dibuat dan kelola di Pool. Secara default, ini akan menentukan berapa banyak CPU di mesin dan membuat proses untuk masing-masing. Walaupun ini bekerja dengan baik untuk contoh sederhana, mungkin ingin memiliki sedikit lebih banyak kontrol dalam lingkungan produksi.

### Masalah dengan Versi multiprosessionng

Ada beberapa kelemahan menggunakan multiprosesor. Mereka tidak benar-benar muncul dalam contoh sederhana ini, tetapi memecah masalah Anda sehingga setiap prosesor dapat bekerja secara mandiri terkadang menjadi sulit.

Juga, banyak solusi memerlukan lebih banyak komunikasi antara proses. Ini dapat menambah kompleksitas pada solusi Anda yang tidak perlu ditangani oleh program tidak bersamaan.

### Kapan Menggunakan Concurrency

Langkah pertama dari proses ini adalah memutuskan apakah harus menggunakan modul concurrency. Sementara contoh-contoh di sini membuat masing-masing library terlihat sangat sederhana, konkurensi selalu disertai dengan kompleksitas ekstra dan seringkali dapat mengakibatkan bug yang sulit ditemukan.

Pertahankan penambahan konkurensi hingga memiliki masalah kinerja yang diketahui dan kemudian tentukan jenis konkurensi yang dibutuhkan. Setelah memutuskan bahwa harus mengoptimalkan program, mencari tahu apakah program terikat dengan CPU atau I/O-bound adalah langkah besar berikutnya. Ingat bahwa program I/O-bound adalah mereka yang menghabiskan sebagian besar waktu mereka menunggu sesuatu terjadi sementara program yang terikat CPU menghabiskan waktu mereka memproses data atau menghitung angka secepat mungkin.