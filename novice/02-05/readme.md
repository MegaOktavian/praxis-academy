# Database

    Database adalah sebuah koleksi terorganisir dari data yang umumnya disimpan dan diakses secara elektronik dari sistem komputer.

    Database Management System (DBMS) adalah perangkat lunak yang berinteraksi denan pengguna akhir, aplikasi, dan database itu sendiri untuk menangkap dan menganalisis data.

DBMS menyediakan beberapa fungsi yang memungkinkan pengelolaan database dan datanya yang dapat diklasifikasikan kedalam empat kelompok fungsional utama :
- __Definisi data__ : pembuatan, modifikasi dan penghapusan definisi yang menentukan organisasi data.
- __Update__ : penyisipan, modifikasi dan penghapusan data aktual.
- __Retrieval (Pengambilan)__ : memberikan informasidalam bentuk yang langsung dapat dugunakan atau untuk diproses lebih lanjut oleh aplikasi lain.

## Bahasa Basis Data

### DCL (Data Control Language)

DCL mengontrol akses data, DCL adalah sintax yang digunakan untuk mengontrol akses data yang disimpan dalam database. Contoh :
- __GRANT__ untuk mengizinkan pengguna tertentu melakukan tugasnya yang ditentukan.
- __REVOKE__ untuk menghapus aksebilitas pengguna ke objek database.

### DDL (Data Definition Language)

DDL mendefinisikan tipe data seperti create, alter, atau drop tabel dan relationship diantara mereka. DDl adalah sintax yang digunakan untuk mendefinisikan struktur data, terutama skema basis data.

__CREATE__

Digunakan untuk membangun database, tabel, indeks baru, atau prosedur yang tersimpan. CREATE TABLE statement :

    CREATE TABLE [table name] ( [column definitions] ) [table parameters]

Contoh :
CREATE TABLE employees (
    id            INTEGER       PRIMARY KEY,
    first_name    VARCHAR(50)   not null,
    last_name     VARCHAR(75)   not null,
    fname         VARCHAR(50)   not null,
    dateofbirth   DATE          not null
);

__DROP__

Untuk menghilangkan database, tabel, indeks, atau vie yang ada. Syntax :

    DROP objecttype objectname.

Contoh :

DROP TABLE employees;

__ALTER__

Memodifikasi objek database yang ada. Syntax :

    ALTER objecttype objectname parameters.

Contoh :

ALTER TABLE sink ADD bubbles INTEGER;
ALTER TABLE sink DROP COLUMN bubbles;

__TRUNCATE__

Digunakan untuk menghapus semua data dari tabel. Syntax :

TRUNCATE TABLE table_name;

### DML (Data Manipulation Language)

Melakukan tugas - tugas seperti menyisipkan, mmperbaharui, dan menghapus data. DML memiliki kemampuan fungsional yang diatur oleh kata awal dari sebuah penyataan :
1. SELECT ... FROM ... WHERE ...
2. SELECT ... INTO ...
3. INSERT INTO ... VALUES ...
4. UPDATE ... SET ... WHERE ...
5. DELETE FROM ... WHERE ...

Contoh :

INSERT INTO employees (first_name, last_name, fname) VALUES ('John', 'Capita', 'xcapit00');

### DQL (Data Query Language)

Memungkinkan pencaran informasi dan menghitung informasi turunan.

## SQL (Structured Query Language)

Adalah bahasa domain-spesific yang digunakan dalam pemrograman dan dirancang untuk megelola data yang disimpan dalam relational database management system (RDBMS), atau untuk pemrosesan dalam relational database management system (RDBMS).

Syntax :

![0205](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-05/readme/Screenshot%20from%202020-03-24%2022-28-21.png)

## Model Basis Data

Adalah jenis model data yang menentukan struktur logis dasi sebuah basis data dan fundamental menentukan dimana cara data yang dapat disimpan, diatur dan dimanipulasi. 

### Flat Model

![0205](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-05/readme/Screenshot%20from%202020-03-24%2022-36-37.png)

Flat model terdiri dari larik elemen data tunggal dua dimensi, di mana semua anggota kolom tertentu dianggap memiliki nilai yang sama, dan semua anggota baris diasumsikan terkait satu sama lain. Misalnya, kolom untuk nama dan kata sandi yang dapat digunakan sebagai bagian dari basis data keamanan sistem. Setiap baris akan memiliki kata sandi spesifik yang terkait dengan pengguna individu. Kolom tabel sering memiliki tipe yang terkait dengannya, mendefinisikannya sebagai data karakter, informasi tanggal atau waktu, bilangan bulat, atau angka floating point. Format tabel ini adalah pendahulu untuk model relasional.

### Hierarchical model

![0205](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-05/readme/Screenshot%20from%202020-03-24%2022-38-53.png)

Dalam model hierarkis, data diorganisasikan ke dalam struktur mirip pohon, yang menyiratkan satu induk untuk setiap catatan. Struktur hierarkis banyak digunakan dalam sistem manajemen basis data mainframe awal, seperti Sistem Manajemen Informasi (IMS) oleh IBM, dan sekarang menggambarkan struktur dokumen XML. Struktur ini memungkinkan hubungan one-to-many antara dua jenis data.

### Network model

![0205](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-05/readme/Screenshot%20from%202020-03-24%2022-41-24.png)

Model jaringan memperluas struktur hierarkis, memungkinkan hubungan banyak ke banyak dalam struktur seperti pohon yang memungkinkan banyak orang tua. Itu paling populer sebelum digantikan oleh model relasional, dan ditentukan oleh spesifikasi CODASYL.

Model jaringan mengatur data menggunakan dua konsep dasar, yang disebut record dan set. Record berisi field (yang dapat diatur secara hierarkis, seperti dalam bahasa pemrograman COBOL). Set mendefinisikan hubungan one-to-many antara record : satu pemilik, banyak anggota. Record dapat menjadi pemilik di sejumlah set, dan anggota dalam sejumlah set.

### Relational model

![0205](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-05/readme/Screenshot%20from%202020-03-24%2022-46-50.png)

Tiga istilah utama digunakan secara luas dalam model basis data relasional: relasi, atribut, dan domain. __Relasi__ adalah tabel dengan kolom dan baris. Kolom yang dinamai relasi disebut __atribut__, dan __domain__ adalah himpunan nilai atribut yang diizinkan untuk diambil.

Struktur data dasar dari model relasional adalah tabel, di mana informasi tentang entitas tertentu (misalnya, seorang karyawan) direpresentasikan dalam baris (juga disebut tupel) dan kolom. Dengan demikian, "relasi" dalam "basis data relasional" mengacu pada berbagai tabel dalam basis data; suatu relasi adalah seperangkat tupel. Kolom menyebutkan berbagai atribut entitas (nama karyawan, alamat atau nomor telepon, misalnya), dan baris adalah contoh aktual entitas (karyawan tertentu) yang diwakili oleh relasi. Akibatnya, setiap tuple dari tabel karyawan mewakili berbagai atribut dari satu karyawan.

Semua relasi dalam database relasional harus mematuhi beberapa aturan dasar untuk memenuhi syarat sebagai relasi. Pertama, urutan kolom tidak penting dalam sebuah tabel. Kedua, tidak mungkin ada tupel atau baris identik dalam sebuah tabel. Dan ketiga, masing-masing tuple akan berisi nilai tunggal untuk setiap atributnya.

### Object-oriented database models

![0205](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-05/readme/Screenshot%20from%202020-03-24%2022-48-40.png)

## Normalisasi Basis Data

Adalah proses penataan basis data relasional sesui dengan rangkaian apa yang disebut bentuk normal untuk mengurangi redundansi data dan meningkatkan inetgrasi data. 
[Untuk selengkapnya bisa baca disini.](https://en.wikipedia.org/wiki/Database_normalization)

## Object-relational mapping

    Adalah teknik pemrograman untuk mengkonversi data antara tipe sistem yang tidak kompetibel menggunakan bahasa pemrograman berorientasi objek.

Berikut contoh sederhana kode C# untuk mengeksekusi query yang ditulis dalam SQL :

    var sql = "SELECT id, first_name, last_name, phone, birth_date, sex, age FROM persons WHERE id = 10";
    var result = context.Persons.FromSqlRaw(sql).ToList();
    var name = result[0]["first_name"];

Menggunakan ORM-job API, memungkinkan pengkodean :

    var person = repository.GetPerson(10);
    var firstName = person.GetFirstName();

Kerangka kerja akan memaparkan beberapa fungsi penyaringan dan permintaan, yang memungkinkan subset dari basis penyimpanan untuk diakses dan dimodifikasi. Kode di bawah ini menanyakan orang-orang dalam database yang nilai ID-nya adalah '10'.

    var person = Person.Get(Person.Properties.Id == 10);

