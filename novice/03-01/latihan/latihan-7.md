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

# Perintah Database 1

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

# Perintah Database 2

1. Jalankan cockroach demo :

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%202/Screenshot%20from%202020-03-17%2022-14-07.png)

2. Lihat semua tabel didatabase menggunakan perintah :

    show tables;

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%202/Screenshot%20from%202020-03-17%2022-16-33.png)

3. Membuat tabel drivers :

    CREATE TABLE drivers (
        id UUID NOT NULL,
        city STRING NOT NULL,
        name STRING,
        dl STRING UNIQUE,
        address STRING,
        CONSTRAINT "primary" PRIMARY KEY (city ASC, id ASC)
    );

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%202/Screenshot%20from%202020-03-17%2022-19-55.png)

4. Menampilkan semua kolom dari tabel :

    SHOW COLUMNS FROM drivers;

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%202/Screenshot%20from%202020-03-17%2022-20-35.png)


5. Menyisipkan data kedalam tabel :
   Menyisipkan data sesuai urutan data :

    INSERT INTO drivers VALUES
    ('c28f5c28-f5c2-4000-8000-000000000026', 'new york', 'Petee', 'ABC-1234', '101 5th Ave');

   Menyisipkan data dalam urutan yang berbeda daridaftar kolom secara eksplisit :

    INSERT INTO drivers (name, city, dl, address, id) VALUES
    ('Adam Driver', 'chicago', 'DEF-5678', '201 E Randolph St', '1eb851eb-851e-4800-8000-000000000006');

   Menyisipkan data lebih dari satu :

    INSERT INTO drivers VALUES
    ('8a3d70a3-d70a-4000-8000-00000000001b', 'seattle', 'Eric', 'GHI-9123', '400 Broad St'),
    ('9eb851eb-851e-4800-8000-00000000001f', 'new york', 'Harry Potter', 'JKL-456', '214 W 43rd St');

   Nilai __default__ digunakan kolom etrtentu dari pernyataan, atau ketika secara eksplisit meminta nilai default. Sebagai contoh :

    INSERT INTO drivers (id, city) VALUES
    ('70a3d70a-3d70-4400-8000-000000000016', 'chicago');

    INSERT INTO drivers (id, city, name, dl, address) VALUES
    ('b851eb85-1eb8-4000-8000-000000000024', 'seattle', DEFAULT, DEFAULT, DEFAULT);

    SELECT * FROM drivers WHERE id in ('70a3d70a-3d70-4400-8000-000000000016', 'b851eb85-1eb8-4000-8000-000000000024');

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%202/Screenshot%20from%202020-03-17%2022-26-55.png)

### Membuat Indeks

__Indeks__ membantu menemukan data tanpa harus melihat melalui setiap baris tabel. Mereka secara otomatis dibuat untuk kunci utama tabel dan kolom apa saja dengan UNIQE constrait.

Dapat memilih menggunakan urutan naik (ASC) atau turun (DESC).

    CREATE INDEX name_idx ON users (name DESC);

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%202/Screenshot%20from%202020-03-17%2022-34-13.png)

Tampilkan indeks yang telah dibuat :

    SHOW INDEX FROM users;

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%202/Screenshot%20from%202020-03-17%2022-34-32.png)

Menampilkan data tabel name dari database users sejumlah 10 data :

    SELECT name FROM users LIMIT 10;

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%202/Screenshot%20from%202020-03-17%2022-36-58.png)

Menampilkan seluruh kolom dari database users sebanyak 10 data :

   SELECT * FROM users LIMIT 10;

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%202/Screenshot%20from%202020-03-17%2022-37-11.png)

Menampilkan data menggunakan filter atau keadaan tertentu :

   SELECT id, name FROM users WHERE city = 'chicago';

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%202/Screenshot%20from%202020-03-17%2022-39-32.png)

Atau

   SELECT city, type, current_location FROM vehicles ORDER BY city, type DESC;

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%202/Screenshot%20from%202020-03-17%2022-40-11.png)

### Memperbaharui baris dalam tabel

    UPDATE promo_codes SET (description, rules) = ('EXPIRED', '{"type": "percent_discount", "value": "0%"}') WHERE expiration_time < '2019-01-22 03:04:05+00:00';

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%202/Screenshot%20from%202020-03-17%2022-44-25.png)

    SELECT code, description, rules FROM promo_codes LIMIT 10;

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%202/Screenshot%20from%202020-03-17%2022-45-08.png)

### Menghapus baris  dalam tabel

    DELETE FROM promo_codes WHERE description = 'EXPIRED';

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%202/Screenshot%20from%202020-03-17%2022-45-41.png)

### Menghapus tabel :

    DROP TABLE drivers;

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%202/Screenshot%20from%202020-03-17%2022-47-33.png)


# Toleransi dan Pemulihan Kesalahan

1. Membuat 6 node :

    cockroach start --insecure --store=fault-node1 --listen-addr=localhost:26257 --http-addr=localhost:8080 --join=localhost:26257,localhost:26258,localhost:26259 --background

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-17%2023-04-51.png)

    cockroach start --insecure --store=fault-node2 --listen-addr=localhost:26258 --http-addr=localhost:8081 --join=localhost:26257,localhost:26258,localhost:26259 --background

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-17%2023-05-13.png)

    cockroach start --insecure --store=fault-node3 --listen-addr=localhost:26259 --http-addr=localhost:8082 --join=localhost:26257,localhost:26258,localhost:26259 --background

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-17%2023-05-44.png)

    cockroach start --insecure --store=fault-node4 --listen-addr=localhost:26260 --http-addr=localhost:8083 --join=localhost:26257,localhost:26258,localhost:26259 --background

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-17%2023-06-01.png)

    cockroach start --insecure --store=fault-node5 --listen-addr=localhost:26261 --http-addr=localhost:8084 --join=localhost:26257,localhost:26258,localhost:26259 --background

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-17%2023-06-21.png)

    cockroach start --insecure --store=fault-node6 --listen-addr=localhost:26262 --http-addr=localhost:8085 --join=localhost:26257,localhost:26258,localhost:26259 --background

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-17%2023-06-41.png)

2. Gunakan perintah cockroach init untuk melakukan klaster :

    cockroach init --insecure --host=localhost:26257

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-17%2023-09-27.png)

### Mengatur Penyeimbangan Beban

1. Menginstall HAProxy :

    sudo apt-get install haproxy

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-17%2023-22-18.png)

2. Jalankan perintah  cockroach gen haproxy, tentukan port dari sembarang simpul: :

    cockroach gen haproxy --insecure --host=localhost --port=26257

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-17%2023-27-11.png)

   Perintah ini menghasilkan file haproxy.cfg yang dikonfigurasikan secara otomatis untuk bekerja dengan node dari cluster yang sedang berjalan.

3. Di haproxy.cfg, ubah bind: 26257 menjadi bind: 26000. Ini mengubah port tempat HAProxy menerima permintaan ke port yang belum digunakan oleh sebuah node. :

    sed -i.saved 's/^    bind :26257/    bind :26000/' haproxy.cfg

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-17%2023-29-07.png)

4. Mulai HAProxy, dengan tanda -f menunjuk ke file haproxy.cfg: :

    haproxy -f haproxy.cfg &

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-17%2023-29-38.png)

### Menjalankan Sampel

1. Muat skema ycsb dan data awal, arahkan ke port HAProxy: :

    cockroach workload init ycsb --splits=50 'postgresql://root@localhost:26000?sslmode=disable'

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-17%2023-34-23.png)

2. Jalankan beban kerja ycsb, arahkan ke port HAProxy: :

    cockroach workload run ycsb --duration=20m --concurrency=3 --max-rate=1000 --tolerate-errors 'postgresql://root@localhost:26000?sslmode=disable'

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-17%2023-34-47.png)

### Memeriksa workload

1. Buka tampilan Admin UI :

     http://localhost:8080

2. Cek SQL Query :

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-17%2023-58-19.png)

3. Cek SQL Connections :

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-17%2023-58-28.png)

4. Memlihat basis data ycsb :

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-17%2023-58-57.png)

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-17%2023-59-02.png)

5. Cek balance di __Overview__ :

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-18%2000-03-43.png)

### Mensimulasikan kegagalan simpul tunggal

1. Di terminal baru, edit zona replikasi default untuk mengurangi jumlah waktu menunggu cluster sebelum mempertimbangkan node mati untuk minimum yang diizinkan 1 menit dan 15 detik :

    cockroach sql --insecure --host=localhost:26000 --execute="SET CLUSTER SETTING server.time_until_store_dead = '1m15s';"

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-18%2007-15-30.png)

2. Kemudian gunakan perintah berhenti kecoak untuk menghentikan simpul:

    cockroach quit --insecure --host=localhost:26261

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-18%2007-16-50.png)

   Periksa kontinuitas beban dan kesehatan cluster

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-18%2007-17-39.png)

   Tonton cluster yang memperbaiki sendiri

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-18%2007-21-38.png)

### Mempersiapkan dua kegagalan simpul simultan

1. Mulai ulang simpul mati, menggunakan perintah yang sama yang di gunakan untuk memulai simpul pada awalnya :

    cockroach start --insecure --store=fault-node5 --listen-addr=localhost:26261 --http-addr=localhost:8084 --join=localhost:26257,localhost:26258,localhost:26259 --background

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-18%2007-28-31.png)

2. Gunakan perintah ALTER RANGE ... CONFIGURE ZONE untuk mengubah faktor replikasi default cluster menjadi 5 :

    cockroach sql --execute="ALTER RANGE default CONFIGURE ZONE USING num_replicas=5;" --insecure --host=localhost:26000

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-18%2007-37-29.png)

3. Kembali di dasbor Ikhtisar UI, saksikan jumlah replika bertambah dan bahkan keluar di semua 6 simpul :

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-18%2007-42-57.png)


### Mensimulasikan dua kegagalan simpul simultan

    cockroach quit --insecure --host=localhost:26260

    cockroach quit --insecure --host=localhost:26261

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-18%2007-45-56.png)

### Periksa kontinuitas beban dan kesehatan cluster

1. Cek kembali di Tampilan Admin UI :

2. Untuk memverifikasi ini lebih lanjut, gunakan perintah kecoa sql untuk menghitung jumlah baris di tabel ycsb.usertable dan memverifikasi bahwa itu masih melayani berbunyi :

    cockroach sql --insecure --host=localhost:26257 --execute="SELECT count(*) FROM ycsb.usertable;"

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-18%2007-49-32.png)

   Dan juga :

    cockroach sql --insecure --host=localhost:26257 --execute="INSERT INTO ycsb.usertable VALUES ('asdf', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);"

    cockroach sql --insecure --host=localhost:26257 --execute="SELECT count(*) FROM ycsb.usertable;"

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-18%2007-50-53.png)

### Bersihkan

1. Di terminal tempat beban kerja YCSB dijalankan, tekan CTRL + c.

2. KStop HAProxy :

    pkill haproxy

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-18%2007-52-21.png)

3. Gunakan perintah berhenti kecoak untuk mematikan 4 simpul yang tersisa :

    cockroach quit --insecure --host=localhost:26257

    cockroach quit --insecure --host=localhost:26258

    cockroach quit --insecure --host=localhost:26259

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-18%2007-54-53.png)

4. Hapus penyimpanan data node dan file konfigurasi HAProxy :

    rm -rf fault-node1 fault-node2 fault-node3 fault-node4 fault-node5 fault-node6 haproxy.cfg haproxy.cfg.saved

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%207/part%203/Screenshot%20from%202020-03-18%2007-56-16.png)
