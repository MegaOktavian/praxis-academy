# OOP (Object-oriented programming)

    Object-oriented programming (OOP) adalah paradigma programming berdasarkan konsep "objek". OOP dapat berisikan data, atribut, kode dan method.

    Variabel digunakan untuk menyimpan informasi yang di format dalam sejumlah kecil tipe data bawaan seperti integer dan karakter numerik, termasuk juga struktur data seperti string, list dan hash tables.

    Procedures dikenal sebagai function, methods, routines atau subroutines yang mengambil input, menghasilkan output dan memanipulasi data.

Modular programming menyediakan kemampuan untuk mengelompokkan prosedur keladam file dan module untuk keperluan organisasi

Bahasa yang mendukung OOP biasanya menggunakan pewarisan untuk penggunaan kembali kode dan ekstensibilitas dlam bentuk kelas dan prototype.

    Classes - definisi untuk format data dan prosedur yang tersedia untuk jenis atau tipe objek tertentu. Misal : kelas yang berisi data anggota dan fungsi anggota.

    Object - contoh kelas

Contoh : sistem belanja online mungkin memiliki objek keranjang belanja, pelanggan, dan produk.

    Class Variabel - memiliki kelas secara keseluruhan, hanya ada satu salinanya dari  masing - masing.

    Instance variables atau atribut - data yang dimiliki oleh objek individu, setip objek memiliki salinannya masing - masing.

    Member variables - merujuk pada variabel kelas dan contoh yang ditentukan oleh kelas tertentu.

    Class Methods - memiliki kelas secara keseluruhan dan hanya memiliki akses ke variabel kelas dan input dari pemanggilan prosedur

    Instance methods - memiliki objek individu dan memiliki akses ke instance variables (atribut) untuk objek spesifik yang dipanggil, output, input dan class variables.

### Encapsulation

    Encapsulation adalah konsep OOP yang menyatukan data dan fungsi yang memanipulasi data, dan menjaga keduanya aman dari gangguan luar serta penyalahgunaan.

Beberapa bahasa memberikan kelas untuk pembatasan akses secara eksplisit. Misalnya untuk data internal menggunakan kelas private dan untuk data external menggunakan kelas public.

### Composition, inheritance, and delegation

    Object composition adalah objek yang dapat berisikan objek lain dalam atribut mereka.

Misalnya, objek dalam kelas kelas Karyawan berisikan objek di kelas Alamat selain atributnya sendiri seperti "nama" dan "opsisi".

Subclass dapat menggantikan metode yang ditentukan oleh supperclass.

    Mixins digunakan untuk menambahkan metode yang sama ke beberapa kelas.

Contoh : kelas UnicodeConversionMixin mungkin menyeiakan metod unicode_to_ascii() ketika disertakan dalam kelas FileReader dan kelas WebPageScraper, yang tidak berbagi induk yang sama.

    Delegation adalah fitur bahasa lain yang dapat digunakan sebagai alternatif pewarisan

### Polymorphism

    Subtyping (suatu bentuk polemorfisme) adalah ketika kode panggilan bisa agnostik untuk kelas mana dalam hierarki yang didukungnya beroperasi, kelas induk atau salah satu turunnya.

Misalnya : objek bertipe Circle dan Square diturunkan dari kelas umum yang disebut Shape. Fungsi Draw untuk setiap jenis Shape mengimplementasikan apa yang diperlukan untuk menggambar dirinya sendiri sementara kode panggilan dapat tetap tidak peduli dengan tipe Shape tertentu yang sedang digambar. 

### Class-responsibility-collaboration (CRC) cards

    CRC adalah alat brainstorming yang digunakan dalam desain perangkat lunak berorientasi objek.

CRC biasnya dibuat dari kartu indeks. Kartu dipartisi menjadi tiga are :
1. Di atas kartu terdapat nama class
2. Di sebelah kiri berisi responsibiliti dari kelas
3. Di sebelah kanan terdapat kolaborator (kelas lain) yang berinteraksi dengan kelas ini untuk memenuhi tanggung jawabnya.

#### Membuat kartu CRC

Dimulai dengan menulis skenario yang mengidentifikasi aktor utama dan tindakan yang dilakukan aktor.  Hanya tulis tindakan dan aktor yang spesifik untuk skenario tertentu Kata benda harus berubah menjadi kelas kartu, kata kerja biasanya berubah menjadi resposibiliti (tanggung jawab) dari kartu, dan kolaborator adalah kartu lain dengan kartu yang berinteraksi.