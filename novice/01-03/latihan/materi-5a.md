# Brief Tour of the Standard Library 1
### Operating System Interface

    Modul os menyediakan puluhan fungsi untuk berinteraksi dengan sistem operasi

![0102](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/materi%205a/Screenshot%20from%202020-03-03%2023-22-24.png)

    Fungsi dir () dan help () berguna sebagai alat bantu interaktif untuk bekerja dengan modul besar seperti os:

gambar 2

gambar 3

    Untuk tugas manajemen file dan direktori harian, modul shutil menyediakan antarmuka level yang lebih tinggi yang lebih mudah digunakan :

gambar 4

### File Wildcards

    Modul glob fungsi untuk membuat daftar file dari pencarian wildcard direktori :

gambar 5

### Argumen Command Line

gambar 6

    Modul argparse menyediakan mekanisme untuk memproses argumen command line.

gambar 7

### Pengalihan Error Output dan Pengakhiran Program

    Modul sys juka memiliki atribut stdin, stdout, dan stderr.

    stderr digunakan untuk memnunculkan peringatan dan pesan kesalahan untuk membuatnya terlihat bahkan setelah stdout telah di redirect.

gambar 8

### String Pattern Matching

    Modul re menyediakan alat ekspresi reguler untuk pengolahan string yang canggih.

gambar 9

## Matematik

    Modul math memberikan akses yang mendasari fungsi C library untuk floating point math.
     
gambar 10

    Modul random menyediakan alat untuk memberikan pilihan acak.

gambar 11

    Modul statistic  untuk menghitung sifat statistik dasar (mean, median, varian, dall) dari data numerik.

gambar 12

### Internet Access

    Modul urllib.request untuk mengambil data dari URL dan smtplib untuk mengirim surat.

gambar 13

gambar 14

### Tanggal dan Waktu

    Modul datetime digunakan untuk memanipulasi tanggal dan waktu secara sederhana dan kompleks.

gambar 15

### Data Compression

    Pengarsipan modul : zlib, gzip, bz2, lzma, dan tarfile.

gambar 16

### Pengukuran Kinerja

    Modul timeit cepat menunjukkan keunggulan kinerja yang sederhana.

gambar 17

    Module profite dan pstats menyediakan alat untuk mengidentifikasi bagian waktu krisis dalam blok kode yang lebih besar.

### Kontrol Kualitas

    Modul doctest menyediakan alat untuk memindai modul dan memvalidasi tes tertanam dalam docstrings program ini.

gambar 18

### Batteries Included

* xmlrpc.client dan xmlrpc.server melaksanakan prosedur pemanggilan jarak jauh ke dalam tugas yang hampir sepele.
* email package adalah library untuk mengelola pesan email
