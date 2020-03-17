# SQL (Structured Query Language)

    SQL adalah bahasa komputer database yang dirancang untuk pengambilan dan mengatur data dalam database relationship.

Berikut struktur SQL

![0209](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-05/latihan/Screenshot%20from%202020-03-14%2018-09-51.png)

### DDL (Data Definition Language)

No. | Command dan Deskripsi
--- | --------------------- 
1. | __Create__
   | Membuat tabel baru, view tabel, atau objek lain di database.
2. | __Alter__
   | Memodifikasi yang ada, obje database, seperti tabel.
3. | __Drop__
   | Menghapus semua tabel. tampilan tabel atau objek lain dalam database.

### DML (Data Manipulation Language)

No. | Command dan Deskripsi
--- | --------------------- 
1. | __Select__
   | Mengambil record tertentu dari satu atau beberapa tabel.
2. | __Insert__
   | Membuat record baru
3. | __Update__
   | Memodifikasi record
4. | __Delete__
   | Menghapus record

### DCL (Data Control Language)

No. | Command dan Deskripsi
--- | --------------------- 
1. | __Grant__
   | Memberikan ijin user
2. | __Revoke__
   | Mengembalikan ijin grant dari user

### RDBMS (Relation Database Management System)

RDBMS adalah dasar dari SQL, dan semua sistem database modern seperti MS SQL Server, IBM DB2,  Oracle, MySQL, dan Microsoft Access.

    Tabel - Data dalam RDBMS disimpan dalam objek basis data yang.

    Fields - Setiap tabel yang dipecah menjadi entitas yang lebih kecil. Misal tabel CUSTOMERS dipecah menjadi ID, NAME, AGE, ADDRESS dan SALARY.

    Kolom - Entitas vertikal dalam tabel yang berisi semua informasi yang terkait dengan bidang tertentu dalam tabel.

    Nilai NULL dalam tabel - Nilai dalam bidang yang tampak kosong, yang berarti bidang dengan nilai NULL adalah bidang tanpa nilai.

### SQL Constrait

    Constrait adalah aturan yang diberlakukan pada kolom data di atas tabel. Ini digunakan untuk membatasi tipe data yang bisa masuk ke tabel. Ini memastikan keakuratan dan keandalan data dalam database.

Batasan dapat berupa level kolom atau level tabel. Batasan level kolom diterapkan hanya untuk satu kolom sedangkan, batasan level tabel diterapkan ke seluruh tabel.

Berikut ini adalah beberapa kendala yang paling umum digunakan dalam SQL -
* NOT NULL Constraint - Memastikan bahwa sebuah kolom tidak dapat memiliki nilai NULL.
* DEFAULT Constraint - Memberikan nilai default untuk kolom saat tidak ada yang ditentukan.
* UNIQ Constrait - Memastikan bahwa semua nilai dalam kolom berbeda.
* PRIMARY Key - Unik mengidentifikasi setiap baris / catatan dalam tabel database.
* FOREIGN Key - Secara unik mengidentifikasi baris / catatan dalam tabel database lain.
* CHECK Constrait - Kendala CHECK memastikan bahwa semua nilai dalam kolom memenuhi kondisi tertentu.
* INDEX - Digunakan untuk membuat dan mengambil data dari database dengan sangat cepat.

### Integritas data

Kategori integritas data berikut ada di setiap RDBMS -
* Entity Integrity - Tidak ada baris duplikat dalam tabel.
* Integritas Domain - Menegakkan entri yang valid untuk kolom tertentu dengan membatasi jenis, format, atau rentang nilai.
* Integritas referensial - Baris tidak dapat dihapus, yang digunakan oleh catatan lain.
* Integritas Buatan Pengguna - Menegakkan beberapa aturan bisnis tertentu yang tidak termasuk dalam entitas, domain, atau integritas referensial.

### Normalisasi Basis Data

Normalisasi basis data adalah proses pengorganisasian data secara efisien dalam suatu basis data. Ada dua alasan proses normalisasi :
1. Menghilangkan data yang berlebihan, misalnya, menyimpan data yang sama di lebih dari satu tabel.
2. Memastikan ketergantungan data masuk akal.

Kedua alasan ini adalah tujuan yang layak karena mengurangi jumlah ruang yang dikonsumsi basis data dan memastikan bahwa data disimpan secara logis. Normalisasi terdiri dari serangkaian pedoman yang membantu memandu Anda dalam membuat struktur database yang baik.

Pedoman normalisasi dibagi menjadi bentuk normal; pikirkan bentuk sebagai format atau cara struktur database diletakkan. Tujuan dari bentuk normal adalah untuk mengatur struktur database, sehingga sesuai dengan aturan bentuk normal pertama, kemudian bentuk normal kedua dan akhirnya bentuk normal ketiga.

## Sytax

SQL SELECT Statement

    SELECT column1, column2....columnN
    FROM   table_name;

SQL DISTINCT Clause

    SELECT DISTINCT column1, column2....columnN
    FROM   table_name;

SQL WHERE Clause

    SELECT column1, column2....columnN
    FROM   table_name
    WHERE  CONDITION;

SQL AND/OR Clause

    SELECT column1, column2....columnN
    FROM   table_name
    WHERE  CONDITION-1 {AND|OR} CONDITION-2;

SQL IN Clause

    SELECT column1, column2....columnN
    FROM   table_name
    WHERE  column_name IN (val-1, val-2,...val-N);

SQL BETWEEN Clause

    SELECT column1, column2....columnN
    FROM   table_name
    WHERE  column_name BETWEEN val-1 AND val-2;

SQL LIKE Clause

    SELECT column1, column2....columnN
    FROM   table_name
    WHERE  column_name LIKE { PATTERN };

SQL ORDER BY Clause

    SELECT column1, column2....columnN
    FROM   table_name
    WHERE  CONDITION
    ORDER BY column_name {ASC|DESC};

SQL GROUP BY Clause

    SELECT SUM(column_name)
    FROM   table_name
    WHERE  CONDITION
    GROUP BY column_name;

SQL COUNT Clause

    SELECT COUNT(column_name)
    FROM   table_name
    WHERE  CONDITION;

SQL HAVING Clause

    SELECT SUM(column_name)
    FROM   table_name
    WHERE  CONDITION
    GROUP BY column_name
    HAVING (arithematic function condition);

SQL CREATE TABLE Statement

    CREATE TABLE table_name(
    column1 datatype,
    column2 datatype,
    column3 datatype,
    .....
    columnN datatype,
    PRIMARY KEY( one or more columns )
    );

SQL DROP TABLE Statement

    DROP TABLE table_name;

SQL CREATE INDEX Statement

    CREATE UNIQUE INDEX index_name
    ON table_name ( column1, column2,...columnN);

SQL DROP INDEX Statement

    ALTER TABLE table_name
    DROP INDEX index_name;

SQL DESC Statement

    DESC table_name;

SQL TRUNCATE TABLE Statement

    TRUNCATE TABLE table_name;

SQL ALTER TABLE Statement

    ALTER TABLE table_name {ADD|DROP|MODIFY} column_name {data_ype};

SQL ALTER TABLE Statement (Rename)

    ALTER TABLE table_name RENAME TO new_table_name;

SQL INSERT INTO Statement

    INSERT INTO table_name( column1, column2....columnN)
    VALUES ( value1, value2....valueN);

SQL UPDATE Statement

    UPDATE table_name
    SET column1 = value1, column2 = value2....columnN=valueN
    [ WHERE  CONDITION ];

SQL DELETE Statement

    DELETE FROM table_name
    WHERE  {CONDITION};

SQL CREATE DATABASE Statement

    CREATE DATABASE database_name;

SQL DROP DATABASE Statement

    DROP DATABASE database_name;

SQL USE Statement

    USE database_name;

SQL COMMIT Statement

    COMMIT;

SQL ROLLBACK Statement

    ROLLBACK;

## Expressions

### SELECT

Syntax :

    SELECT column1, column2, columnN 
    FROM table_name 
    WHERE [CONDITION|EXPRESSION];

Boolean Expressions

Syntax :

    SELECT column1, column2, columnN 
    FROM table_name 
    WHERE SINGLE VALUE MATCHING EXPRESSION;

Contoh perintah :

![0205](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-05/latihan/Screenshot%20from%202020-03-14%2018-41-37.png)

Numeric Expression

Syntax : 

    SELECT numerical_expression as  OPERATION_NAME
    [FROM table_name
    WHERE CONDITION] ;

Contoh perintah :

SQL> SELECT COUNT(*) AS "RECORDS" FROM CUSTOMERS;

![0205](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-05/latihan/Screenshot%20from%202020-03-14%2018-43-22.png)

Date Expressions

![0205](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-05/latihan/Screenshot%20from%202020-03-14%2018-44-45.png)

