# Pengujian Perangkat Lunak

Pengujian software adalah investigasi yang dilakukan untuk memberikan stakeholder informasi tentang kualitas dari software produk atau jasa yang diuji. Pengujian perangkat lunak juga dapat memberikan pandangan yang objektif dan independen terhadap perangkat lunak untuk memungkinkan menghargai bisnis dan memahami risiko penerapan perangkat lunak. Teknik pengujian meliputi proses menjalankan program atau aplikasi dengan tujuan menemukan bug perangkat lunak, dan memverifikasi bahwa produk perangkat lunak layak untuk digunakan.

Tidak semua cacat software disebabkan oleh kesalahan pengkodean. Salah satu sumber kesalahan adalah kesenjangan persyaratan, yaitu persyaratan yang tidak dikenali yang menyebabkan kesalahan kelalaian oleh perancang program.

## Pendekatan Pengujian

### Pengujian Statik, Dinamik dan Pasif

Pengujian Statik adalah pengujian berdasarkan ulasan, penelusuran dan inspeksi.

Pengujian dinamis adalah pengujian yang mengeksekusi kode yang diprogram dengan serangkaian kasus pengujian tertentu.

Pengujian pasif berarti memverifikasi perilaku sistem tanpa interaksi dengan produk perangkat lunak.

### Pendekatan Eksplorasi

Pendekatan eksplorasi adalah suatu pendekatan untuk pengujian perangkat lunak yang secara ringkas digambarkan sebagai pembelajaran simultan, desain pengujian dan pelaksanaan pengujian.

### Pendekatan "Box"

___Pengujian White-box__

![0304](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/0304/readme/Screenshot%20from%202020-03-26%2008-43-58.png)

Pengujian ini memverifikasi struktur internal atau cara kerja suatu program, yang bertentangan dengan fungsionalitas yang terpapar pada pengguna akhir.

___Pengujian Black-box__

![0304](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/0304/readme/Screenshot%20from%202020-03-26%2008-44-18.png)

Pengujian ini memeriksa fungsionalitas tanpa sepengetahuan implementasi internal, tanpa melihat kode sumber. Penguji hanya mengetahui apa yang seharusnya dilakukan perangkat lunak, bukan bagaimana melakukannya.

__Pengujian Komponen Antarmuka__
Pengujian ini adalah variasi dari pengujian kotak hitam, dengan fokus pada nilai data diluar tindakan terkait komponen subsistem. Praktik pengujian komponen antarmuka dapat digunakan untuk memeriksa penanganan data yang dikirim kan antara berbagai unit, atau komponen subsistem, diluar pengujian integrasi penuh antara unit - unit tersebut.

__Pengujian Visual__
Tujuan dari pengujian ini adalah untuk memberikan pengembang dengan kemampuan memeriksa apa yang terjadi pada titik kegagalan perangkat lunak dalam menyajikan data sedemikian rupa sehingga pengembang dapat dengan mudah menemukan informasi yang dibutuhkan, dan informasi tersebut dinyatakan dengan jelas.

__Pengujian Grey-box__
Pengujian ini melibatkan pengetahuan tentang struktur data dan algoritma interna untuk tujuan merancang tes saat melaksanakan tes tersebut pada pengguna, atau tingkat kotak hitam.

## Tingkat Pengujian

### Pengujian Unit

Pengujian unit mengacu oada tes yang memverifikasi fungsionalitas bagian kode tertentu, biasnya pada tingkat fungsi. Jenis tes ini biasanya dituliskan pengembang saat mengerjakan kode (white-box), untuk memastikan bahwa fungsional bahwa fungsi spesifik berfungsi seperti yang diharapkan.

Pengujian unit adalah proses pengembangan perangkat lunak yang melibatkan aplikasi tersinkronisasi dari spektrum luas strategi pencegahan dan deteksi cacat untuk mengurasi risiko, waktu, dan biaya pengembangan perangkat lunak.

### Pengujian Integrasi

Pengujian integrasi adalah semua pengujian perangkat lunak yang berupaya memverifikasi antarmuka antara komponen dengan desain perangkat lunak.  Pengujian ini berfungsi untuk mengekspos kerusakan pada antarmuka dan interaksi antara komponen terintegrasi (modul).

### Pengujian Sistem

Pengujian sistem menguji sistem yang sepenuhnya terintegrasi untuk memverifikasi bahwa sistem memenuhi persyaratan.

### Pengujian Penerimaan Operasional

Penerimaan operasional digunakan untuk melakukan kesiapan operasional dari suatu produk, layanan atau sistem sebagai bagian dari sistem manajemen mutu.

## Pengujian Jenis, Teknik dan Taktik

Berikut beberapa pengujian yang dapat dilakukan :
1. Pengujian instalasi
2. Pengujian kompatibilitas
3. Pengujian smoke dan sanity
4. Pengujian regerasi
5. Pengujian penerimaan
6. Pengujian alfa
7. Pengujian beta

## Verifikasi dan Validasi Perangkat Lunak

Verifikasi adalah proses mengevaluasi suatu sistem atau komponen untuk menentukan apakah produk dari fase pengembangan tertentu memenuhi kondisi yang diberlakukan pada awal fase itu.
    
Validasi adalah proses mengevaluasi suatu sistem atau komponen selama atau pada akhir proses pengembangan untuk menentukan apakah memenuhi persyaratan yang ditentukan.

# Pengujian Unit

