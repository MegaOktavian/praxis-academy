# Menjalankan CrockroachDB

1. Jalankan perintah berikut di terminal :

  cockroach

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-16%2022-41-43.png)

   Kemudian : 

  cockroach start-single-node --insecure --listen-addr=localhost:26257 --http-addr=localhost:8080

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-16%2022-41-47.png)

2. Buka Browser dan jalankan :
   http://localhost/8080

   Akan muncul tampilan :

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-16%2022-42-26.png)

3. Untuk menghentikan perintah cukup tekan Ctrl+C maka cockroach akan berhenti :

  ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-16%2022-44-29.png)

4. Hapus direktori cockroach-data

  ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-16%2022-45-07.png)

  ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-16%2022-47-39.png)

# Mengkonekkan dengan SQL Shell

1. Ketikkan perintah berikut untuk memulai dan membuat tabel dengan skema yang sesuai untuk beban kerja yang ditentukan :

  cockroach workload init movr

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-16%2023-14-20.png)

2. Jalankan SQL, menggunakan perintah :

  cockroach sql --insecure

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-16%2023-14-43.png)

# Perintah Database

__Perintah untuk menampilkan database :__

  SHOW databases;

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-16%2023-15-15.png)

 __Perintah untuk menampilkan tabel dari database movr :__

  SHOW TABLES FROM movr;

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-16%2023-15-51.png)

__Melihat semua isi data sebanyak 10 data pada tabel users database movr :__

   SELECT * FROM movr.users LIMIT 10;

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-16%2023-16-27.png)

__Membuat database menggunakan perintah :__

  CREATE DATABASE crdb_uni;
  
  SET database = crdb_uni;

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2000-02-51.png)

__Membuat tabel students menggunakan perintah :__

  CREATE TABLE students (id UUID PRIMARY KEY DEFAULT gen_random_uuid(), name STRING);

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2000-04-20.png)

__Melihat skema tabel students menggunakan perintah :__

  SHOW CREATE students;

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2000-07-06.png)

__Membuat tabel courses menggunakan perintah :__

  CREATE TABLE courses (sys_id UUID DEFAULT gen_random_uuid(), course_id INT, name STRING, PRIMARY KEY (sys_id, course_id));

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2000-07-28.png)

__Melihat skema tabel courses menggunakan perintah :__

  SHOW CREATE TABLE courses;

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2000-07-45.png)

__Mengubah struktur tabel courses menggunakan perintah :__

  ALTER TABLE courses ADD COLUMN schedule STRING;

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2000-10-43.png)

__Melihat skema tabel courses menggunakan perintah :__

  SHOW CREATE TABLE courses;

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2000-11-06.png)


# Local Cluster (Insecure)

### Menjalankan cluster :

1. Menggunakan cockroach start untuk node pertama :

  cockroach start --insecure --store=node1 --listen-addr=localhost:26257 --http-addr=localhost:8080 --join=localhost:26257,localhost:26258,localhost:26259 --background

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2000-45-04.png)

2. Node kedua :

  cockroach start --insecure --store=node2 --listen-addr=localhost:26258 --http-addr=localhost:8081 --join=localhost:26257,localhost:26258,localhost:26259 --background

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2000-46-28.png)

3. Gunakan perintah __cockroach init__ untuk melakukan inisialisasi, mengirimkan permintaan ke sembarang node :

  cockroach init --insecure --host=localhost:26257

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2000-51-01.png)

   Setiap node akan mencetak setiap rincian startup yang bermanfaat untuk log-nya. Misalkan : 

  grep 'node starting' node1/logs/cockroach.log -A 11

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2000-52-43.png)

### Menggunakan SQL Client

1. Jalankan perintah cockroach sql terhadap node 1 :

  cockroach sql --insecure --host=localhost:26257

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2001-39-25.png)

2. Jalankan beberapa peryanyaan dasar :

  CREATE DATABASE bank;
  
  CREATE TABLE bank.accounts (id INT PRIMARY KEY, balance DECIMAL);
  
  INSERT INTO bank.accounts VALUES (1, 1000.50);
  
  SELECT * FROM bank.accounts;

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2001-41-01.png)

3. Keluar dari shell SQL pada node 1 dan buka shell baru pada node 2 :

  \q
  
  cockroach sql --insecure --host=localhost:26258

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2001-43-06.png)

4. Jalankan query Select yang sama :

  SELECT * FROM bank.accounts;

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2001-46-01.png)

5.  Keluar dari shell SQL pada node 1 dan buka shell baru pada node 2 :

  \q

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2001-46-42.png)

### Menjalankan Beberapa workload

1. Muat dataset awal :

  cockroach workload init movr 'postgresql://root@localhost:26257?sslmode=disable'

  ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2001-49-48.png)

2. Jalankan workload selama 5 menit :

  cockroach workload run movr --duration=5m 'postgresql://root@localhost:26257?sslmode=disable'

  ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2001-50-19.png)

### Mengakses UI Admin

1. Jalankan http://localhost:8080 pada browser.

  ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2001-51-40.png)

  Terdapat 2 node aktif.

2. Klik Metrix untuk mengakses berbagai dashbor seri waktu :

  ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2001-54-05.png)

### Memanipulasi kegagalan node

1. Diterminal baru jalankan :

  cockroach quit --insecure --host=localhost:26259'

  ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2001-58-49.png)

2. Restart node 3 :

  cockroach start --insecure --store=node3 --listen-addr=localhost:26259 --http-addr=localhost:8082 --join=localhost:26257,localhost:26258,localhost:26259 --background

  ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2001-59-43.png)

### Skala Cluster

1. Muali node 2 lagi :

  cockroach start --insecure --store=node4 --listen-addr=localhost:26260 --http-addr=localhost:8083 --join=localhost:26257,localhost:26258,localhost:26259 --background

  ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2002-01-53.png)

  cockroach workload init movr 'postgresql://root@localhost:26257?sslmode=disable'

  ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2002-02-14.png)

2. Tinjau Kembali Overview :

  ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2002-05-22.png)

### Menghentikan Cluster

1. Gunakan perintah berikut :

  cockroach quit --insecure --host=localhost:26257
  
  cockroach quit --insecure --host=localhost:26258
  
  cockroach quit --insecure --host=localhost:26259
  
  cockroach quit --insecure --host=localhost:26260
  
  cockroach quit --insecure --host=localhost:26261

  ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2002-15-37.png)

2. Menghapus cluster :

  rm -rf node1 node2 node3 node4 node5

  ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/Screenshot%20from%202020-03-17%2002-17-11.png)

