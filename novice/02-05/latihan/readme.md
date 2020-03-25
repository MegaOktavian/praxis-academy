#### Membuat database bernama, tabel dan memasukkan data


    MariaDB [(none)]> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | mysql              |
    | performance_schema |
    +--------------------+
    3 rows in set (0.001 sec)

    MariaDB [(none)]> create database data_kampus;
    Query OK, 1 row affected (0.118 sec)

    MariaDB [(none)]> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | data_kampus        |
    | information_schema |
    | mysql              |
    | performance_schema |
    +--------------------+
    4 rows in set (0.001 sec)

    MariaDB [(none)]> use data_kampus;
    Database changed

    MariaDB [data_kampus]> show tables;
    Empty set (0.000 sec)

    MariaDB [data_kampus]> create table mahasiswa(
        -> nim varchar(11) not null primary key,
        -> nama varchar(100) not null,
        -> alamat varchar (100) not null,
        -> prodi varchar(30) not null
        -> );
    Query OK, 0 rows affected (0.458 sec)

    MariaDB [data_kampus]> show tables;
    +-----------------------+
    | Tables_in_data_kampus |
    +-----------------------+
    | mahasiswa             |
    +-----------------------+
    1 row in set (0.001 sec)

    MariaDB [data_kampus]> create table prodi(
        -> kode_prodi varchar(5) not null primary key,
        -> nama_prodi varchar(30) not null
        -> );
    Query OK, 0 rows affected (0.300 sec)

    MariaDB [data_kampus]> show tables;
    +-----------------------+
    | Tables_in_data_kampus |
    +-----------------------+
    | mahasiswa             |
    | prodi                 |
    +-----------------------+
    2 rows in set (0.001 sec)

    MariaDB [data_kampus]> desc mahasiswa;
    +--------+--------------+------+-----+---------+-------+
    | Field  | Type         | Null | Key | Default | Extra |
    +--------+--------------+------+-----+---------+-------+
    | nim    | varchar(11)  | NO   | PRI | NULL    |       |
    | nama   | varchar(100) | NO   |     | NULL    |       |
    | alamat | varchar(100) | NO   |     | NULL    |       |
    | prodi  | varchar(30)  | NO   |     | NULL    |       |
    +--------+--------------+------+-----+---------+-------+
    4 rows in set (0.003 sec)

    MariaDB [data_kampus]> ALTER TABLE mahasiswa CHANGE prodi nama_prodi varchar(30) not null;
    Query OK, 0 rows affected (0.198 sec)
    Records: 0  Duplicates: 0  Warnings: 0

    MariaDB [data_kampus]> desc mahasiswa;
    +------------+--------------+------+-----+---------+-------+
    | Field      | Type         | Null | Key | Default | Extra |
    +------------+--------------+------+-----+---------+-------+
    | nim        | varchar(11)  | NO   | PRI | NULL    |       |
    | nama       | varchar(100) | NO   |     | NULL    |       |
    | alamat     | varchar(100) | NO   |     | NULL    |       |
    | nama_prodi | varchar(30)  | NO   |     | NULL    |       |
    +------------+--------------+------+-----+---------+-------+
    4 rows in set (0.002 sec)

    MariaDB [data_kampus]> desc prodi;
    +------------+-------------+------+-----+---------+-------+
    | Field      | Type        | Null | Key | Default | Extra |
    +------------+-------------+------+-----+---------+-------+
    | kode_prodi | varchar(5)  | NO   | PRI | NULL    |       |
    | nama_prodi | varchar(30) | NO   |     | NULL    |       |
    +------------+-------------+------+-----+---------+-------+
    2 rows in set (0.002 sec)

    MariaDB [data_kampus]> ALTER TABLE mahasiswa CHANGE nama_prodi kode_prodi varchar(5) not null after nim;
    Query OK, 0 rows affected (1.091 sec)              
    Records: 0  Duplicates: 0  Warnings: 0

    MariaDB [data_kampus]> desc mahasiswa;
    +------------+--------------+------+-----+---------+-------+
    | Field      | Type         | Null | Key | Default | Extra |
    +------------+--------------+------+-----+---------+-------+
    | nim        | varchar(11)  | NO   | PRI | NULL    |       |
    | kode_prodi | varchar(5)   | NO   |     | NULL    |       |
    | nama       | varchar(100) | NO   |     | NULL    |       |
    | alamat     | varchar(100) | NO   |     | NULL    |       |
    +------------+--------------+------+-----+---------+-------+
    4 rows in set (0.002 sec)

    MariaDB [data_kampus]> ALTER TABLE mahasiswa ADD FOREIGN KEY (kode_prodi) REFERENCES prodi(kode_prodi);
    Query OK, 0 rows affected (1.032 sec)              
    Records: 0  Duplicates: 0  Warnings: 0

    MariaDB [data_kampus]> desc mahasiswa;
    +------------+--------------+------+-----+---------+-------+
    | Field      | Type         | Null | Key | Default | Extra |
    +------------+--------------+------+-----+---------+-------+
    | nim        | varchar(11)  | NO   | PRI | NULL    |       |
    | kode_prodi | varchar(5)   | NO   | MUL | NULL    |       |
    | nama       | varchar(100) | NO   |     | NULL    |       |
    | alamat     | varchar(100) | NO   |     | NULL    |       |
    +------------+--------------+------+-----+---------+-------+
    4 rows in set (0.003 sec)

    MariaDB [data_kampus]> insert into prodi values('00025','Ilmu Komputer'),('01033','Teknik Informatika');
    Query OK, 2 rows affected (0.127 sec)
    Records: 2  Duplicates: 0  Warnings: 0

    MariaDB [data_kampus]> desc prodi;
    +------------+-------------+------+-----+---------+-------+
    | Field      | Type        | Null | Key | Default | Extra |
    +------------+-------------+------+-----+---------+-------+
    | kode_prodi | varchar(5)  | NO   | PRI | NULL    |       |
    | nama_prodi | varchar(30) | NO   |     | NULL    |       |
    +------------+-------------+------+-----+---------+-------+
    2 rows in set (0.002 sec)

    MariaDB [data_kampus]> select * from prodi;
    +------------+--------------------+
    | kode_prodi | nama_prodi         |
    +------------+--------------------+
    | 00001      | Sistem Informasi   |
    | 00025      | Ilmu Komputer      |
    | 01033      | Teknik Informatika |
    +------------+--------------------+
    3 rows in set (0.001 sec)

    MariaDB [data_kampus]> insert into mahasiswa values('17000160009','00001','Mega Oktaviani Fadillah','Yogyakarta'),('17000171010','00025','Anzerilia Puri','Solo');
    Query OK, 2 rows affected (0.127 sec)
    Records: 2  Duplicates: 0  Warnings: 0

    MariaDB [data_kampus]> select * from mahasiswa;
    +-------------+------------+-------------------------+------------+
    | nim         | kode_prodi | nama                    | alamat     |
    +-------------+------------+-------------------------+------------+
    | 17000160009 | 00001      | Mega Oktaviani Fadillah | Yogyakarta |
    | 17000171010 | 00025      | Anzerilia Puri          | Solo       |
    +-------------+------------+-------------------------+------------+
    2 rows in set (0.001 sec)

    MariaDB [data_kampus]> 
