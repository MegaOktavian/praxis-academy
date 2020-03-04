# Brief Tour of the Standard Library 1
### Operating System Interface

    Modul os menyediakan puluhan fungsi untuk berinteraksi dengan sistem operasi

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/materi%205a/Screenshot%20from%202020-03-03%2023-22-24.png)

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/materi%205a/Screenshot%20from%202020-03-03%2023-23-51.png)

    Fungsi dir () dan help () berguna sebagai alat bantu interaktif untuk bekerja dengan modul besar seperti os:

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/materi%205a/Screenshot%20from%202020-03-03%2023-26-50.png)

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/materi%205a/Screenshot%20from%202020-03-03%2023-27-11.png)

    Untuk tugas manajemen file dan direktori harian, modul shutil menyediakan antarmuka level yang lebih tinggi yang lebih mudah digunakan :

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/materi%205a/Screenshot%20from%202020-03-03%2023-30-11.png)

### File Wildcards

    Modul glob fungsi untuk membuat daftar file dari pencarian wildcard direktori :

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/materi%205a/Screenshot%20from%202020-03-03%2023-32-55.png)

### Argumen Command Line

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/materi%205a/Screenshot%20from%202020-03-03%2023-36-51.png)

    Modul argparse menyediakan mekanisme untuk memproses argumen command line.

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/materi%205a/Screenshot%20from%202020-03-03%2023-41-10.png)

### Pengalihan Error Output dan Pengakhiran Program

    Modul sys juka memiliki atribut stdin, stdout, dan stderr.

    stderr digunakan untuk memnunculkan peringatan dan pesan kesalahan untuk membuatnya terlihat bahkan setelah stdout telah di redirect.

### String Pattern Matching

    Modul re menyediakan alat ekspresi reguler untuk pengolahan string yang canggih.

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/materi%205a/Screenshot%20from%202020-03-03%2023-50-21.png)

## Matematik

    Modul math memberikan akses yang mendasari fungsi C library untuk floating point math.
     
![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/materi%205a/Screenshot%20from%202020-03-03%2023-54-06.png)

    Modul random menyediakan alat untuk memberikan pilihan acak.

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/materi%205a/Screenshot%20from%202020-03-04%2000-56-34.png)

    Modul statistic  untuk menghitung sifat statistik dasar (mean, median, varian, dall) dari data numerik.

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/materi%205a/Screenshot%20from%202020-03-04%2000-57-38.png)

### Internet Access

    Modul urllib.request untuk mengambil data dari URL dan smtplib untuk mengirim surat.

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/materi%205a/Screenshot%20from%202020-03-04%2000-58-55.png)

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/materi%205a/Screenshot%20from%202020-03-04%2001-00-34.png)

### Tanggal dan Waktu

    Modul datetime digunakan untuk memanipulasi tanggal dan waktu secara sederhana dan kompleks.

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/materi%205a/Screenshot%20from%202020-03-04%2001-13-50.png)

### Data Compression

    Pengarsipan modul : zlib, gzip, bz2, lzma, dan tarfile.

![0103]()

### Pengukuran Kinerja

    Modul timeit cepat menunjukkan keunggulan kinerja yang sederhana.

![0103]()

    Module profite dan pstats menyediakan alat untuk mengidentifikasi bagian waktu krisis dalam blok kode yang lebih besar.

### Kontrol Kualitas

    Modul doctest menyediakan alat untuk memindai modul dan memvalidasi tes tertanam dalam docstrings program ini.

![0103]()

### Batteries Included

* xmlrpc.client dan xmlrpc.server melaksanakan prosedur pemanggilan jarak jauh ke dalam tugas yang hampir sepele.
* email package adalah library untuk mengelola pesan email
