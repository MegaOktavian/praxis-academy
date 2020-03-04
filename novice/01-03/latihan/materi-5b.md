# Brief Tour of the Standard Library 2
### Output Formatting

    Modul reprlib menyediakan versi repr() disesuaikan untuk menampilkan display berukuran besar atau deep.

gambar 1

    Modul pprint menawarkan kontrol untuk mencetak baik built-in dan user yang mendefinisikan objek dengan cara yang dapat dibaca oleh interpreter.

gambar 2

    Modul textwrap - format paragraf untuk teks agar sesuai dengan lebar layar yang diberikan.

gambar 3

    Modul local - mengakses database dengan format data tertentu.

gambar 4

### Templating

    Modul string termasuk versatile template class dengan sintak yang disederhanakan, cocok untuk mengedit end-users.

gambar 5

    Metode substituse() - menimbulkan KeyError ketika placeholder tidak disediakan dalam kamus atau argumen kata kunci.

gambar 6

### Bekerja dengan Binary Data Record Layouts

    Modul struct menyediakan pack() dan unpack() yang berfungi untuk bekerja dengan format variabel panjang biner record.

gambar 8

### Multi-threading

    Threading adalah teknik untuk memisahkan tugas - tugas yang tidak tergantung secara berurutan.

    Modul threading dapat menjalankan tugas di latar belakang sementara program utama terus berjalan.

gambar 9

### Logging

    Modul logging menawarkan sistem logging penuh fitur dan  fleksibel.

gambar 10

### Weak References

    Module weakref menyediakan alat untuk objek pelacakan tanpa membuat referensi.

gambar 11

### Tools untuk Berkerja dengan List

    Modul array menyediakan array() objek seperti list yang menyimpan hanya homogen data dan menyimpannya.

gambar 12

    Modul collection menyediakan deque() objek seperti daftar dengan menambahkan lebih cepat dan muncul dari sisi kiri namun pencarian lebih lambat ditengah.

gambar 13

    Modul bisect berfungsi untuk memanipulasi daftar yang diurutkan.

gambar 14

    Modul heapq menyediakan fungsi untuk melaksanakan tumpukan berdasarkan daftar reguler.

gambar 15

### Decimal Floating Point Arithmetic 

    Modul decimal menawarkan data tipe desimal untuk desimal aritmatika floating point.

Kelas ini sangat membantu untuk :
* Aplikasi keuangan dan penggunaan lainnya yang membutuhkan representasi desimal yang tepat
* Kontrol atas precission
* Kontrol atas pembulatan untuk memenugi persyaratan hukum atau peraturan
* Pelacakan tempat desimal yang signifikan

gambar 16
