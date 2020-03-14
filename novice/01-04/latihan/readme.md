# Unified Modeling Language (UML)

    UML adalah tujuan umum, perkembangan, bahasa pemodelan dibidang rekayasa perangkat lunak yang dimaksudkan untuk menyediakan cara standar untuk memvisualisasikan deain sistem.

### Design

UML menawarkan cara untuk menvisualisasikan blueprint arsitektur sistem dalam diagram, termasuk eleme - elemen seperti :
- Semua kegiatan (pekerjaan).
- Komponen individu dari sistem :
  -> Bagaimana mereka berinteraksi dengan komponen perangkat lunak lain.
- Bagaimana sistem akan berjalan.
- Bagaimana entitas berinteraksi dengan orang lain (komponen dan antarmuka).
- Antarmuka user eksternal.

# Pemodelan

    Diagram adalah representasi grafik parsial dari model sistem. Himpunan dari diagram tidak perlu sepenuhnya mengcober model dan menghapus diagram tidak akan mengubah model.

    Modul juga dapat berisi dokumentasi yang menggerakan elemen model dan diagram.

Diagram UML mewakili dua tampilan berbeda dari model sistem :
- Tampilan statis (terstruktur) : menekankan struktur statis dari sistem yang menggunakan objek, atribut, operasi dan hubungan. Ini termasuk diagram class dan diagram struktur komposit.
- Tampilan dinamis (perilaku) : menekankan perilaku dinamis sistem dengan menunjukkan kolaborasi antar object dan perubahan pada kondisi internal objrk. Tampilan ini mencakup diagram sequence, diagram aktivitas dan diagram state machine.

    Use case  adalah cara menentkan penggunaan sistem yang diperlukan.

### Diagram 

Contoh diagram yang dikategorikan hierarkis :

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%201/Screenshot%20from%202020-03-04%2021-58-01.png)

### Struktur Diagram

    Struktur diagram menekankan hal -hal yang harus dalam sistem yang dimodelkan. Karena diagram sruktur mewakili struktur, diagram tersebut digunakan secara luas dalam mendokumetasikan arsitektur software dari sistem software.

 Diagram component

 ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%201/Screenshot%20from%202020-03-04%2022-02-31.png)

 Diagram class

 ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%201/Screenshot%20from%202020-03-04%2022-03-02.png)

 ### Diagram Behavior (Perilaku)

    Behavior diagram menekankan apa yang harus terjadi dalam sistem yang dimodelkan. Karena diagram ini menggambarkan perilaku suatu sistem, diagram ini digunakan secara luas untuk menggambarkan fungsionalitas sistem perangkat lunak.

Diagram aktivitas

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%201/Screenshot%20from%202020-03-04%2022-09-58.png)

Diagram usecase

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%201/Screenshot%20from%202020-03-04%2022-10-29.png)

### Diagram Interaksi

    Diagram interaksi merupakan bagian dari diagram perilaku yang menkankan aliran kontrol dan data dari hal - hal dalam sistem yang dimodelkan.

Diagram sequence

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%201/Screenshot%20from%202020-03-04%2022-13-00.png)

Diagram komunikasi

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%201/Screenshot%20from%202020-03-04%2022-13-16.png)

### Metamodeling

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%201/Screenshot%20from%202020-03-04%2022-13-38.png)

Object Management Group (OMG) telah mengembangkan arsitektur metamodeling untuk mendefinisikan UML, yang disebut Meta-Object Fasilitator. MOF dirancang sebagai arsitektur empat lapis, seperti yang ditunjukkan pada gambar di atas. Ini memberikan model meta-meta di bagian atas, yang disebut lapisan M3. Model M3 ini adalah bahasa yang digunakan oleh Meta-Object Fasilitator untuk membangun metamodel, yang disebut model-M2.

#  Applications of UML

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%202/Screenshot%20from%202020-03-04%2022-21-55.png)

Diagram keadaan tersebut menunjukkan bagaimana UML digunakan unutk setiap perancangan  sistem pintu yang hanya bisa dibuka dan ditutup.

UML dapat dignakan untuk mengembangkan dan memberikan contoh pemodelan ekspresif yang siap pakai kepada pengguna (programmer).

    UML adalah bahasa gafis untuk menvisualisasikan, menentukan, membangun, dan mendokumentasikan informasi tentang sistem instensif perangkat lunak.

### Pemodelan aplikasi UML menggunakan berbagai diagram

o Struktur diagram dan aplikasinya
    
    Strukturisasi diagram menunjukkan pandangan dari suatu sistem yang menunjukkan struktur objek, termasuk pengklarifikasian, hubungan, atribut dan operasi mereka.

  - Diagram class
    
    ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%202/Screenshot%20from%202020-03-04%2022-41-41.png)

  - Diagram component
    
    ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%202/Screenshot%20from%202020-03-04%2022-42-19.png)

  - Diagram composite structure
    
    ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%202/Screenshot%20from%202020-03-04%2022-42-36.png)

  - Diagram penempatan
    
    ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%202/Screenshot%20from%202020-03-04%2022-42-50.png)

  - Diagram objek
    
    ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%202/Screenshot%20from%202020-03-04%2022-43-00.png)

  - Diagram packege
    
    ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%202/Screenshot%20from%202020-03-04%2022-43-14.png)

  - Diagram profile
    
    ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%202/Screenshot%20from%202020-03-04%2022-43-32.png)

o Diagram behavior dan aplikasinya

    Digunkan untuk menggambarkan perilaku suatu sistem, mereka digunakan secara luas untuk menggambarkan fungsional sistem perangkat lunak.

  - Diagram aktivitas
    
    ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%202/Screenshot%20from%202020-03-04%2022-53-19.png)

  - Diagram state machine
    
    ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%202/Screenshot%20from%202020-03-04%2022-53-31.png)

  - Diagram use case
    
    ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%202/Screenshot%20from%202020-03-04%2022-53-43.png)

o Diagram interaksi dan aplikasinya

    Diagram interaksi adalah bagian dari diagram perilaku dan menekankan aliran kontrol dan data diantara sistem yang dimodelkan.

  - Diagram komunikasi
    
    ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%202/Screenshot%20from%202020-03-04%2022-54-01.png)

  - Diagram interaction overview
    
    ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%202/Screenshot%20from%202020-03-04%2022-54-16.png)

  - Diagram sequence
    
    ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%202/Screenshot%20from%202020-03-04%2022-54-28.png)

  - Diagram timing

### Web applications

Aplikasi web UML dapat digunakan untuk memodelkan antarmuka pengguna aplikasi web dan memperjelas tujuan situs web.

    Rekayasa web berbasis UML bertujuan menawarkan profil UML yang sesuai dengan kebutuhan pengembangan web dengan lebih baik. 

Berikut ini adalah contohnya:
o Representasi aplikasi web menggunakan serangkaian model
  - Model kasus penggunaan aplikasi web
  - Model implementasi aplikasi web
  - Model penerapan aplikasi web
  - Model keamanan aplikasi web
  - Peta situs aplikasi web
o Untuk memodelkan halaman, hyperlink, dan konten dinamis di sisi klien dan server.
o Untuk memodelkan aspek sisi server dari halaman web dengan satu kelas dan aspek sisi klien dengan yang lain dan membedakan keduanya dengan menggunakan mekanisme ekstensi UML untuk menentukan stereotip dan ikon untuk setiap server dan halaman klien.
o Stereotip dalam UML digunakan untuk mendefinisikan semantik baru untuk elemen pemodelan.
o Formulir dalam HTML juga dapat dimodelkan menggunakan berbagai konstruksi UML.
o UML dapat digunakan untuk mengekspresikan eksekusi logika bisnis sistem dalam elemen dan teknologi khusus-Web tersebut.

### Sistem Embedded (Tertanam)

Beberapa konsep kunci UML terkait dengan sistem tertanam:
o UML bukan satu bahasa, tetapi satu set notasi, sintaksis dan semantik untuk memungkinkan pembuatan rumpun bahasa untuk aplikasi tertentu.
o Mekanisme ekstensi di UML seperti profil, stereotip, tag, dan batasan dapat digunakan untuk aplikasi tertentu.
o Pemodelan use-case untuk menggambarkan lingkungan sistem, skenario pengguna, dan kasus pengujian.
o UML memiliki dukungan untuk spesifikasi, desain, dan pemodelan sistem berorientasi objek.
o Minat terhadap UML dari sistem tertanam dan komunitas waktu nyata.
o UML mendukung dekomposisi dan penyempurnaan struktural berbasis objek.

### Class attributes (fields)

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%205/Screenshot%20from%202020-03-04%2023-27-00.png)

- Nama visabilitas : type [count] = default_falue
- Visabilitas :
  + public
  # protected
  - private
  ~ package (default)
  / derived
- Static atribut bergaris bawah
- Attribut derived (diturunkan) : tidak disimpan, tetapi dapat dihitung dari nilai atribut lainnya.
- Contoh atribut :
  -balance : double = 0.00

### Class operation/ method

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%205/Screenshot%20from%202020-03-04%2023-27-11.png)

- Nama visabilitas (parameter) : return_type
- Visabiliti : 
  + public
  # protected
  - private
  ~ package (default)
- Static atribut bergaris bawah
- Tipe parameter yang terdaftar sebagai (nama: tipe)
- Menghilangkan konstruktor return_type dan ketika return type adalah void
- Contoh method :
  +distance(p1: Point, p2:Point): double

### Komen

    Direpresentasikan sebagai catatan terlipat, dilampirkan ke kelas / metode yang sesuai / dll oleh garis putus-putus

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%205/Screenshot%20from%202020-03-04%2023-33-59.png)

### Relasi diantara class

* Generalisasi: hubungan warisan
  - Warisan antar kelas
  - Implementasi antar muka
* Asosiasi: hubungan penggunaan
  - Ketergantungan (dependency)
  - Kengumpulan (aggregation) 
  - Komposisi (composition)

### Relasi Generalization (inheritance)

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%205/Screenshot%20from%202020-03-05%2000-45-47.png)

- Hierarki yang ditarik dari atas ke bawah
- Panah menagarah keinduk
- Garis / panah menunjukkan apah orangtua adalah (n) :
  * Class : garis solid, panah hitam
  * Kelas abstract : garis solid, panah putih
  * Interface : garis putus - putus, panah putih
- Sering menghilangkan hubungan generalisasi yang sepele / jelas, seperti menggambar kelas Object sebagai orangtua

### Relasi Associational

1. Multiplicity (berapa banyak yang digunakan)
   - *    : 0, 1, atau lebih
   - 1    : 1 tepat
   - 2..4 : diantara 2 dan 4, inklusif
   - 3..* : 3 atau lebih (juga ditulis sebagai "3..")
2. Name (hubungan apa yang dimiliki objek)
3. Navigability (arah)

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%205/Screenshot%20from%202020-03-05%2000-54-08.png)
   
### Multiplicity dari asosiasi

* one-to-one
  
  ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%205/Screenshot%20from%202020-03-05%2000-57-19.png)

  Setiap siswa harus membawa tepat satu kartu ID

* one-to-many

  ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%205/Screenshot%20from%202020-03-05%2000-57-33.png)

  Satu daftar persegi panjang dapat berisi banyak persegi panjang

### Tipe Asosiasi

* Agregasi : "adalah bagian dari"
  - Dilambangkan dengan berlian putih

    ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%205/Screenshot%20from%202020-03-05%2001-04-14.png)

* Komposisi : "seluruhnya terbuat dari"
  - Versi agregasi yang lebuh kuat
  - Bagian hidup dan mati dari keseluruhan
  - Dilambangkan dengan berlian hitam

    ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%205/Screenshot%20from%202020-03-05%2001-04-25.png)

* Dependensi : "digunakan sementara"
  - Disimbolkan dengan garis putus- putus
  - Sering kali merupakan detail implementasi, bukan bagian intrinsik dari keadaan objek itu.

    ![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%205/Screenshot%20from%202020-03-05%2001-04-35.png)

Contoh komposisi atau agregasi

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%205/Screenshot%20from%202020-03-05%2001-05-09.png)

Jika movie theater hilang
   begitu juga box office => komposisi
   tetapi film mungkin masih ada => agregasi

Contoh Diagram Kelas

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%205/Screenshot%20from%202020-03-05%2001-13-52.png)

Contoh UML : people

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%205/Screenshot%20from%202020-03-05%2001-14-28.png)

Diagram kelas :voter

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%205/Screenshot%20from%202020-03-05%2004-26-11.png)

Contoh UML : video store

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%205/Screenshot%20from%202020-03-05%2004-26-23.png)

Contoh UML : student

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/materi%201/artikel%205/Screenshot%20from%202020-03-05%2004-26-37.png)
