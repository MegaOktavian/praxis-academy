# Testing Kode

### Testing Manual vs Otomatis

    Pengujian eksplorasi adalah bentuk pengujian yang dilakukan tanpa rencana.

    Pengujian otomatis adalah pengeksekusian test plan dengan skrip bukan manusia.

### Unit Tests vs Integration Tests

Pikirkan bagaimana Anda bisa menguji lampu pada mobil. Anda akan menyalakan lampu (dikenal sebagai langkah uji) dan pergi ke luar mobil atau meminta teman untuk memeriksa bahwa lampu menyala (dikenal sebagai pernyataan uji). Pengujian beberapa komponen dikenal sebagai pengujian integrasi.

    Tes unit adalah tes yang lebih kecil, yang memeriksa apakan satu komponen berperasi dengan cara yang benar.

Terdapat dua jenis tes :
1. Tes integrasi memeriksa apakah komponen dalam aplikasi beroperasi.
2. Tes unit memeriksa komponen kecil dalam aplikasi

Contoh : mengecek nilai sum() dari angka (1, 2, 3) sama dengan 6 :

    assert sum([1, 2, 3]) == 6, "Should be 6"

Contoh diatas tidak akan menampilkan apapun karena nilainya benar.

![0202]()

Contoh nilai sum bernilai error karena tidak sama dengan 6

    assert sum([1, 1, 1]) == 6, "Should be 6"

![0202]()

Menambahkan niali baru dan menjalankannya menggunakan terminal :

![0202]()

Dengan menggunakan python, sum() menerima setiap iterable sebagai argumen pertama. Berikut test dengan tuple :

![0202]()

Jika file test_sum_2.py dijalankan, maka akan terjadi kesalahan karena sum() dari [1,2,2] adalah 5 bukan 6.

## Memilih Test Runner
### unittest

    unittest berisi kerangka kerja pengujian dan test runner.

unittest mensyaratkan bahwa :
o Memasukkan test kedalam kelas sebagai metode
o Menggunakan serangkaian metode pernyataan khusus di unittest.

Untuk mengonversi contoh sebelumnya ke test case yang belum dipatenkan, harus:
o Impor unittest dari perpustakaan standar
o Buat kelas yang disebut TestSum yang mewarisi dari kelas TestCase
o Ubah fungsi tes menjadi metode dengan menambahkan diri sebagai argumen pertama
o Ubah pernyataan untuk menggunakan metode self.assertEqual () pada kelas TestCase
o Ubah titik entri baris perintah untuk memanggil unittest.main ()

![0202]()

### nose

nose kompetibel dengan semua tes yang ditulis menggunakan unittest framework dan dapat digunakan sebagai pengganti drop-in untuk  unittest test runner. Untuk memulainya install terlebih dahulu :

![0202]()

Cobalah execute pada file yang telah dibuat :

![0202]()

### pytest

Keuntungan nyata dari pytest datang dari penulisan pytest test cases. pytest test cases adalah serangkaian fungsi dalam file python yang diulai dengan nama test_.

pytest memiliki beberapa fitur :
o Mendukung untuk pernyataan assert bawaan bukannya menggunakan metode self.assert*()
o Mendukung penyaringan untuk uji kasus
o Kemampuan untuk mengulang dari tes yang gagal terakhir
o Ekosistem ratusan plugin untuk memperluas fungsionalitas

Penulisan TestSum dengan pytest akan seperti ini :

    def test_sum():
        assert sum([1, 2, 3]) == 6, "Should be 6"

    def test_sum_tuple():
        assert sum((1, 2, 2)) == 6, "Should be 6"

### Uji Pertama

Buat projek baru dan didalamnya buat folder baru bernama my_sum. Didalam folder my_sum, buatlah file kosong bernama __init__.py. File tersebut dapat diimport sebagai modul dari direktori induk.
Folder akan terlihat :

![0202]()

Masukkan script berikut ini kedalam file __init__.py

    def sum(arg):
        total = 0
        for val in arg:
            total += val
        return total

buatlah file yang bernama test.py yang akan berisi test case. Tempatkan file ini di dalam folder project, sehingga susunanya menjadi :

![0202]()

Saat menambahkan lebih banyak test, file tunggal akan menjadi berantakan dan sulit untuk dipertahankan. Buatlah folder bernama tests/ dan membagi file test menjadi beberapa bagian.

Tambahkan script berikut kedalam file test.py :

    import unittest
    from my_sum import sum


    class TestSum(unittest.TestCase):
        def test_list_int(self):
            """
            Test that it can sum a list of integers
            """
            data = [1, 2, 3]
            result = sum(data)
            self.assertEqual(result, 6)

    if __name__ == '__main__':
        unittest.main()

Contoh kode ini:

1. Mengimpor sum() dari paket my_sum yang dibuat
2. Menentukan kelas kasus uji baru yang disebut TestSum, yang mewarisi dari unittest.TestCase
3. Menentukan metode pengujian, .test_list_int (), untuk menguji daftar bilangan bulat. Metode .test_list_int () akan:
   - Deklarasikan data variabel dengan daftar angka (1, 2, 3)
   - Tetapkan hasil my_sum.sum (data) ke variabel hasil
   - Menyatakan bahwa nilai hasil sama dengan 6 dengan menggunakan metode .assertEqual () pada kelas unittest.TestCase
4. Menentukan titik entri baris perintah, yang menjalankan test-runner .main () () yang paling tidak kompatibel

    assertion adalah memvalidasi output terhadap respons yang dikenal.

Ada beberapa praktik seputar cara menulis pernyataan:
1. Pastikan tes berulang dan jalankan pengujian beberapa kali untuk memastikan tes memberikan hasil yang sama setiap waktu
2. Coba dan nyatakan hasil yang terkait dengan data input, seperti memeriksa bahwa hasilnya adalah jumlah nilai aktual dalam sum() contohnya

unittest hadir dengan banyak metode untuk menegaskan nilai, tipe, dan keberadaan variabel. Berikut adalah beberapa metode yang paling umum digunakan :

![0202]()

Putuskan side effect sebelum melakukan pengujian. side effect merupakan bagian paling penting dari pengujian.

Jalankan file test.py menggunakan terminal menggunakan perintah :

    python -m unittest test

![0202]()

Dapat memberikan opsi tambahan untuk mengubah output. Salah satunya adalah -v untuk berbose :

    python -m unittest -v test

![0202]()

Dapat membuat permintaan auto-discovery menggunakan :

    python -m unittest discover

![0202]()

Ini akan mencari direktori saat ini untuk setiap file yang dinamai test*.py.

Dapat memberikan nama direktori sebagai gantinya dengan -s flag dan nama direktori :

    python -m unittest discover -s test

![0202]()

unittest akan menjalankan semua tes dalam satu rencana tes dan memberikan hasilnya.

Jika kode sumber tidak di root direktori dan terkandung dalam subdirektori, misalnya dalam folder src/. Dapat mengetahui dimana unittest untuk tesk pengeksekusian sehingga itu dapat mengimport modul dengan benar menggunakan -t flag :

    python -m unittest discover -s test -t src

Dibagian atas file test.py tambahkan pernyataan impor untuk mengimpor tipe Fractions dari franctions modul :

    from fractions import Fraction

Sekarang tambahkan tes dengan pernyataan mengharapkan nilai yang salah, dalam hal ini mengharapkan jumlah 1/4, 1/4, dan 2/5 menjadi 1:

import unittest

from my_sum import sum


    class TestSum(unittest.TestCase):
        def test_list_int(self):
            """
            Test that it can sum a list of integers
            """
            data = [1, 2, 3]
            result = sum(data)
            self.assertEqual(result, 6)

        def test_list_fraction(self):
            """
            Test that it can sum a list of fractions
            """
            data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
            result = sum(data)
            self.assertEqual(result, 1)

    if __name__ == '__main__':
        unittest.main()

Jika Anda menjalankan tes lagi dengan python -m unittest test, output :

![0202]()

Di output, didadatkan informasi berikut:
1. Baris pertama menunjukkan hasil eksekusi semua tes, satu gagal (F) dan satu berlalu (.).
2. Entri FAIL menunjukkan beberapa detail tentang tes gagal:
   - Nama metode pengujian (test_list_fraction)
   - Modul tes (tes) dan test case (TestSum)
   - Traceback ke garis gagal
   - Detail pernyataan dengan hasil yang diharapkan (1) dan hasil aktual (Fraksi (9, 10))

### Cara menggunakan Django Test Runner

    from django.test import TestCase

    class MyTestCase(TestCase):
        # Your test methods


Untuk menjalankan rangkaian pengujian, alih-alih menggunakan unittest di baris perintah, gunakan tes manage.py:

    python manage.py test

### Menggunakan unittest dan Flask

Flask mengharuskan aplikasi diimpor dan kemudian diatur dalam mode uji. Semua instantiasi klien uji dilakukan dalam metode setUp dari uji. Dalam contoh berikut, my_app adalah nama aplikasi. Kode dalam file pengujian akan terlihat seperti ini :

    import my_app
    import unittest


    class MyTestCase(unittest.TestCase):

        def setUp(self):
            my_app.app.testing = True
            self.app = my_app.app.test_client()

        def test_home(self):
            result = self.app.get('/')
            # Make your assertions

Untuk mengeksekusinya gunakan perintah :

    python -m unittest discover

### Skenario Pengujian

Terdapat 3 langkah dasar :
1. Buat input.
2. jalankan kode, ambil output.
3. Bandingkan hasilnya dengan hasil yang diharapkan.

    Data yang dibuat sebagai input disebut fixture.

    Jika menjalankan tes yang sama dan melewati nilai yang berbeda setiap kali dan mengharapkan hasil yang sama disebut sebagai parameterization.

### Menangani Kegagalan yang Diharapkan

Sebelumnya, ketika Anda membuat daftar skenario untuk menguji sum(), sebuah pertanyaan muncul: Apa yang terjadi ketika Anda memberikan nilai yang buruk, seperti bilangan bulat tunggal atau string?

Dalam hal ini, diharapkan sum() untuk melakukan kesalahan. Ketika itu melakukan kesalahan, itu akan menjadi tes yang gagal.

Ada cara khusus untuk menangani kesalahan yang diharapkan. Dapat menggunakan .assertRaises () sebagai manajer konteks, lalu di dalam blok with, jalankan langkah-langkah pengujian :

    import unittest

    from my_sum import sum


    class TestSum(unittest.TestCase):
        def test_list_int(self):
            """
            Test that it can sum a list of integers
            """
            data = [1, 2, 3]
            result = sum(data)
            self.assertEqual(result, 6)

        def test_list_fraction(self):
            """
            Test that it can sum a list of fractions
            """
            data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
            result = sum(data)
            self.assertEqual(result, 1)

        def test_bad_type(self):
            data = "banana"
            with self.assertRaises(TypeError):
                result = sum(data)

    if __name__ == '__main__':
        unittest.main()

Test case yang sekarang akan berhasil jika sum(data) menimbulkan TypeError.

Ada beberapa teknik sederhana yang dapat digunakan untuk menguji bagian aplikasi yang memiliki banyak efek samping:
1. Kode refactoring untuk mengikuti Prinsip Tanggung Jawab Tunggal (Single Responsibility Principle)
2. Mengejek panggilan metode atau fungsi apa pun untuk menghilangkan efek samping
3. Menggunakan pengujian integrasi alih-alih pengujian unit untuk aplikasi ini

    Pengujian integrasi adalah pengujian beberapa komponen aplikasi untuk memeriksa apakah mereka bekerja bersama. 

### Penulisan Tes Integrasi

Pengujian integrasi mungkin memerlukan tindakan seperti konsumen atau pengguna aplikasi dengan:
1. Memanggil API REST HTTP
2. Memanggil API Python
3. Memanggil layanan web
4. Menjalankan baris perintah

Masing-masing jenis tes integrasi ini dapat ditulis dengan cara yang sama seperti tes unit, mengikuti pola Input, Execute, dan Assert. Perbedaan yang paling signifikan adalah bahwa tes integrasi memeriksa lebih banyak komponen sekaligus dan karenanya akan memiliki lebih banyak efek samping daripada tes unit. Selain itu, tes integrasi akan memerlukan lebih banyak tempat untuk dipasang, seperti database, soket jaringan, atau file konfigurasi.

Cara sederhana untukmemisahkan tes unit dan integrasi adalah dengan meletakkan folder yang berbeda :

![0202]()

Direktori flag yang ditentukan, -s, dapat ditambahkan ke unittest discover dengan jalur yang berisi tes :

    python -m unittest discover -s tests/integration


### Menguji Aplikasi Berbasis Data

Banyak tes integrasi akan membutuhkan data backend seperti database untuk ada dengan nilai-nilai tertentu. Jenis - jenis tes integrasi ini akan bergantung pada berbagai perlengkapan pengujian untuk memastikan semuanya dapat diulang dan diprediksi.

Teknik yang baik untuk digunakan adalah menyimpan data uji dalam folder di dalam folder pengujian integrasi Anda yang disebut fixture untuk menunjukkan bahwa itu berisi data uji. Kemudian, dalam pengujian dapat memuat data dan menjalankan tes.

Berikut adalah contoh struktur itu jika data terdiri dari file JSON :

![0202]()

Di dalam test case Anda, Anda bisa menggunakan metode .setUp () untuk memuat data uji dari file fixture di jalur yang dikenal dan melakukan banyak tes terhadap data tes itu. Ingat Anda dapat memiliki beberapa kasus uji dalam satu file Python, dan penemuan yang paling tidak aktif akan menjalankan keduanya. Anda dapat memiliki satu test case untuk setiap set data pengujian :

import unittest


class TestBasic(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.app = App(database='fixtures/test_basic.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 100)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=10)
        self.assertEqual(customer.name, "Org XYZ")
        self.assertEqual(customer.address, "10 Red Road, Reading")


    class TestComplexData(unittest.TestCase):
        def setUp(self):
            # load test data
            self.app = App(database='fixtures/test_complex.json')

        def test_customer_count(self):
            self.assertEqual(len(self.app.customers), 10000)

        def test_existence_of_customer(self):
            customer = self.app.get_customer(id=9999)
            self.assertEqual(customer.name, u"バナナ")
            self.assertEqual(customer.address, "10 Red Road, Akihabara, Tokyo")

    if __name__ == '__main__':
        unittest.main()

### Tox

    Tox adalah aplikasi yang mengotomatiskan pengujian di berbagai lingkungan.

Menginstall tox gunakan perintah :

    pip install tox

![0202]()

Alih-alih harus mempelajari sintaks konfigurasi Tox, dapat memulai dengan menjalankan aplikasi quickstart:

![0202]()

Tox dikonfigurasi melalui file konfigurasi di direktori proyek Anda. File konfigurasi Tox berisi yang berikut:
1. Perintah untuk menjalankan untuk menjalankan tes
2. Setiap paket tambahan diperlukan sebelum menjalankan
3. Versi target Python untuk diuji

File tox.ini :

    [tox]
    envlist = py27, py36

    [testenv]
    deps =

    commands =
        python -m unittest discover

Sebelum menjalankan Tox, harus ada file setup.py di folder aplikasi. Jika tidak ada dapat menambahkan baris file berikut di file tox.ini

    envlist = py27, py36
    skipsdist=True

Jika tidak membuat setup.py dan aplikasi memiliki beberapa dependensi dari PyPI, maka harus menentukannya pada sejumlah baris di bawah bagian [testenv]. misalnya Django akan membutuhkan :

    [testenv]
    deps = django

Jalankan Tox, itu akan membuat dua lingkungan baru. Satu untuk python 2.7 dan 3.6. Direktori Tox tersebut .tox/. Dalam direktori .tox/ akan mengeksekusi :

    python -m unittest

![0202]()

Menjalankan proses ini dengan memanggil Tox :

    tox

![0202]()

Tox akan menampilkan hasil tes terhadap masing-masing lingkungan. Saat pertama kali dijalankan, Tox membutuhkan sedikit waktu untuk membuat lingkungan virtual, tetapi begitu sudah, eksekusi kedua akan jauh lebih cepat.


Ada beberapa opsi baris perintah tambahan yang bagus untuk diingat.

alankan hanya satu lingkungan, seperti Python 3.6 :

    tox -e py36

Buat kembali lingkungan virtual, jika dependensi Anda berubah atau paket situs rusak :

    tox -r

Jalankan Tox dengan lebih sedikit keluaran verbose:

    tox -q

Menjalankan Tox dengan lebih banyak keluaran verbose:

    tox -v

### Menjalankan Tes secara otomatis

Alat pengujian otomatis disebut sebagai alat CI/CD, yang merupakan singkata dari "Continuous Integration/Continuous Deployment”.

    Travis Ci adalah salah satu dari banyak layanan CI (Continuous Integration) yang tersedia.

Buat file .travis.yml dengsn script :

    language: python
    python:
    - "2.7"
    - "3.7"
    install:
    - pip install -r requirements.txt
    script:
    - python -m unittest discover

konfigurasinya memerintahkan Travis CI untuk:
1. Uji terhadap Python 2.7 dan 3.7 (Anda dapat mengganti versi itu dengan yang Anda pilih.)
2. Instal semua paket yang Anda daftarkan di requirement.txt (Anda harus menghapus bagian ini jika Anda tidak memiliki ketergantungan.)
3. Jalankan python -m unittest untuk menjalankan tes

### Passive Linting dengan flake8

Menginstall flake8 menggunakan perintah :

    pip install flake8

![0202]()

Kemudian jalankan file test.py menggunakan flake8 :

    flake8 test.py

![0202]()

flake8 dapat dikonfigurasi pada baris perintah atau di dalam file konfigurasi di proyek. Jika ingin mengabaikan aturan tertentu, seperti E305 yang ditunjukkan di atas,dapat mengaturnya dalam konfigurasi. flake8 akan memeriksa file .flake8 di folder proyek atau file setup.cfg. Jika memutuskan untuk menggunakan Tox, dapat meletakkan bagian konfigurasi flake8 di dalam tox.ini.

Contoh ini mengabaikan direktori .git dan __pycache__ serta aturan E305. Selain itu, ia menetapkan panjang garis maks ke 90 bukannya 80 karakter. Mungkin akan ditemukan bahwa batasan default 79 karakter untuk lebar garis sangat terbatas untuk pengujian, karena berisi nama metode yang panjang, string literal dengan nilai tes, dan potongan data lainnya yang bisa lebih panjang. Adalah umum untuk menetapkan panjang garis untuk pengujian hingga 120 karakter :

    [flake8]
    ignore = E305
    exclude = .git,__pycache__
    max-line-length = 90

Atau, Anda dapat memberikan opsi ini di baris perintah :

    flake8 --ignore E305 --exclude .git,__pycache__ --max-line-length=90

Dapat menambahkan flake8 kedalam konfigurasi CI. Untuk Travis CI, maka :

    matrix:
    include:
        - python: "2.7"
        script: "flake8"

### Aggressive Linting dengan Pemformatan Kode

Pembuatan kode akan mengubah kode secara otomatis untuk memenuhi koleksi praktik gaya dan tata letak.

    black adalah formatter yang sangat tidak kenal ampun.

menginstal black menggunakan perintah

    pip install black

![0202]()

Menjalankan file menggunakan black :

    black test.py

![0202]()

Penggunaan linting pada fluake8 :

    flake8 --max-line-length=120 tests/

### Pengujain Degradasi Kerja

Mengeksekusi test() dalam 100 waktu dan print() : 

    def test():
        # ... your code

    if __name__ == '__main__':
        import timeit
        print(timeit.timeit("test()", setup="from __main__ import test", number=100))

Opsi lain, jika memutuskan untuk menggunakan pytest sebagai pelari uji, adalah plugin pytest-benchmark. Ini menyediakan perlengkapan terbaik yang disebut benchmark. Ini dapat melewati tolok benchmark() panggilan apa pun, dan itu akan mencatat waktu panggilan tersebut ke hasil pytest.

Menginstal pytest-benchmark :

    pip install pytest-benchmark

![0202]()

Menambahkan tes yang menggunakan fixture dan melewati callable yang akan dieksekusi :

    def test_my_function(benchmark):
        result = benchmark(test)

### Menguji Kelemahan dan Keamanan Aplikasi

Menginstall bandit :

    pip install bandit

![0202]()

Kemudian berikan nama modul aplikasi denan -r flug :

    bandit -r my_sum

![0202]()