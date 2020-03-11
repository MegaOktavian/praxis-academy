# Concurrency

    Konkurensi adalah kejadian simultan.

Threading dan asyncio keduanya berjalan pada satu prosesor dan karenanya hanya menjalankan satu per satu. Mereka secara cerdik menemukan cara untuk bergiliran mempercepat proses keseluruhan. Meskipun mereka tidak menjalankan berbagai train secara bersamaan, ini disebut konkurensi.

Cara thread atau task bergiliran adalah perbedaan besar antara threading dan asyncio. Dalam threading, sistem operasi benar-benar tahu tentang setiap thread dan dapat menghentikannya kapan saja untuk mulai menjalankan thread yang berbeda. Ini disebut pre-emptive multitasking karena sistem operasi dapat mencegah thread untuk beralih.

Pre-emptive multitasking berguna karena kode di thread tidak perlu melakukan apa pun untuk beralih. Ini juga bisa sulit karena ungkapan "kapan saja". Switch ini dapat terjadi di tengah-tengah pernyataan Python tunggal, bahkan yang sepele seperti x = x + 1.

Asyncio, di sisi lain, menggunakan multitasking kooperatif. Tugas-tugas harus bekerja sama dengan mengumumkan kapan mereka siap untuk keluar. Itu berarti bahwa kode dalam tugas harus sedikit berubah untuk mewujudkan hal ini.

### Paralelisme

Dengan multiprocessing, Python menciptakan proses baru. Suatu proses di sini dapat dianggap sebagai program yang hampir sama sekali berbeda, meskipun secara teknis mereka biasanya didefinisikan sebagai kumpulan sumber daya di mana sumber daya termasuk memori, pegangan file, dan hal-hal seperti itu. Salah satu cara untuk memikirkannya adalah bahwa setiap proses berjalan dengan interpreter Python sendiri.

Perbedaan Konkurensi dan Paralelisme

Jenis konkurensi | Pengalihan Keputusna | Jumlah Prosesor 
---------------- | -------------------- | ---------------
Pre-emptive multitasking (threading) | Sistem operasi memutuskan kapan harus beralih tugas eksternal ke Python. | 1
Cooperative multitasking (asyncio) | Tugas memutuskan kapan harus menyerahkan kontrol. | 1

Multiprocessing (multiprocessing)_| Semua proses berjalan pada waktu yang sama pada prosesor yang berbeda. | Many


Concurrency dapat membuat perbedaan besar untuk dua jenis masalah. Ini disebut CPU-bound dan I/O-bound.

Masalah I/O-bound menyebabkan program  melambat karena sering harus menunggu input / output (I/ ) dari beberapa sumber daya eksternal. Mereka sering muncul ketika program Anda bekerja dengan hal-hal yang jauh lebih lambat daripada CPU.

Contoh hal yang lebih lambat dari CPU Anda banyak, tetapi program Anda untungnya tidak berinteraksi dengan sebagian besar dari mereka. Hal-hal lambat yang akan paling sering berinteraksi dengan program Anda adalah sistem file dan koneksi jaringan.

Mari kita lihat seperti apa tampilannya:

![0203]()

Dalam diagram di atas, kotak biru menunjukkan waktu ketika program  sedang bekerja, dan kotak merah dihabiskan untuk menunggu operasi I/O selesai. Diagram ini bukan untuk mengukur karena permintaan di internet dapat mengambil beberapa pesanan lebih besar dari instruksi CPU, sehingga program dapat menghabiskan sebagian besar waktunya menunggu.

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

Perhatikan bahwa program ini membutuhkan modul permintaan. Menjalankan permintaan :

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

download_site () hanya mengunduh konten dari URL dan mencetak ukurannya. Dimungkinkan untuk menggunakan get() dari permintaan secara langsung, tetapi membuat objek Session memungkinkan permintaan untuk melakukan beberapa trik jaringan yang bagus dan benar-benar mempercepat.

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

