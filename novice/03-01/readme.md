# NoSQL

NoSQL (merujuk pada "non SQL" atau "non relasional") basis data menyediakan mekanisme untuk penyimpanan dan pengambilan data yang dimodelkan dalam cara lain selain hubungan tabel yang digunakan dalam database.

NoSQL menekankan kesederhanaan desian, penskalaan "horisontal" yang lebih sederhana untuk mengelompokkan sebuah mesin, kontrol yang lebih baik atas availability (ketersediaan) dan membatasi ketidakcocokan impedensi object-relatkonal.

Kesesuaian khusus dari basis data NoSQL yang diberikan tergantung pada masalah yang harus dipecahkan.

Hambatan NoSQL adalah penggunaan bahasa query yang rendah, kurangnya antarmuka standar, dan investasi besar sebelumnya dalam relasional yang ada basis data. Sebagai gantinya NoSQL menawarkan konsep "konsistensi sampai akhir" dimana perubahan basis data disebarkan ke semua simpul sehingga query untuk data mungkin tidak segera mengembalikan data yang diperbahari atau apat mengakibatkan pembacaan data yang hilang dan bentuk lain dari kehilangan data.

### Tipe dan contohnya

Tipe | Contoh penting dari tipe ini
---- | ----------------------------
Key-Value Cache | Apache Ignite, Couchbase, Coherence, eXtreme Scale, Hazelcast, Infinispan, Memcached, Redis, Velocity
Key-Value Store | ArangoDB, Aerospike, Couchbase, Redis
Key-Value Store (Eventually-Consistent) | Oracle NoSQL Database, Dynamo, Riak, Voldemort
Key-Value Store (Ordered) | FoundationDB, InfinityDB, LMDB, MemcacheDB
Tuple Store | Apache River, GigaSpaces
Object Database | Objectivity/DB, Perst, ZopeDB
Document Store | ArangoDB, BaseX, Clusterpoint, Couchbase, CouchDB, DocumentDB, eXist-db, IBM Domino, MarkLogic, MongoDB, Qizx, RethinkDB, Elasticsearch
Wide Column Store | Amazon DynamoDB, Bigtable, Cassandra, Scylla, HBase, Hypertable
Native Multi-model Database | ArangoDB, Cosmos DB, OrientDB, MarkLogic

### Key-value (KV) store

KV menggunakan array asosiatif sebagai model data fundamental. Dalam model ini, data direpresentasikan sebagai kumpulan pasangan nilai kunci sehingga setiap kunci yang mungkin muncul paling banyak satu kali dalam koleksi.

Model KV dapat dipeluas ke model yang dapat diatur secara terpisah yang mempertahankan kunci dalam urutan leksikografis.

### Document Store

Salah satu karakteristik pendefinisian lain dari basis data berorientasi dokumen adalah bahwa selain pencarian kunci yang dilakukan oleh penyimpanan key-value, basis data juga menawarkan API atau bahasa permintaan yang mengambil dokumen berdasarkan isinya.

Berbagai implementasi menawarkan cara pengorganisasian dan / atau pengelompokan dokumen yang berbeda:
1. Koleksi
2. Tag
3. Metadata tidak terlihat
4. Hirarki direktori

Dibandingkan dengan database relasional, misalnya, koleksi dapat dianggap analog dengan tabel dan dokumen analog dengan catatan. Tetapi mereka berbeda : setiap catatan dalam tabel memiliki urutan bidang yang sama, sedangkan dokumen dalam koleksi mungkin memiliki bidang yang sama sekali berbeda.

### Graph

Basis data jenis ini diranvang untuk data yang hubungannya terwakili dengan baik sebagai grafik yang terdiri dari elemen - elemen yang saling berhubungan dengan sejumlah terbatas hubungan diantara mereka. Jenis data dapat berupa hubungan sosial, jalur transportasi umum, peta jalan, topologi jaringan, dll.

### ACID (Atomicity, Consistency, Isolation, Durability)

Database mendukung properti ACID atau bergabung dengan operasi jika dokumentasi untuk database membuat klaim.

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/Screenshot%20from%202020-03-15%2022-54-47.png)

# NewSQL

NewQL adalah kelas sistem manajemen basis data relasional yang berupaya memberikan skalabilitas sistem NoSQL unutuk beban kerja pemrosesan transaksi online )OLTP) sambil mempertahankan jaminan ACID dari sistem basis data tradisional.

Sistem NewSQL dapat dikelompokkan menjadi 3 kategori :
1. Arsitektur baru
   Sistem NewSQL mengadopsi berbagai arsitektur internal. beberapa sistem menggunakan sekelompok node shared-nothing, dimana node mengelola subset data.
2. Mesin SQL
   Mesin penyimpanan dioptimalkan untuk SQL. Sistem ini menyiakan antarmuka pemrograman yang sama dengan SQL, tetapi skalanya lebih baik daripada mesin bawaan.
3. Sharding transparan
   Sistem ini secara otomatis memecah basis data menjadi beberapa node menggunakan algoritma konsesnsus Raft atau Paxos.

Basis data NweSQL memecah masalah basis data tanpa melepas kelebihan basis data tradisionlal. Dengan kata lain NewSQl adala h sistem bass data relasional yang menggabungkan OLTP, kinerja tinggi, dan skalabilitas NoSQl. Mereka menggunakan SQl untuk menelan informasi baru, melakukan banyak transaksi pada saat yang sama, dan memodifikasi isi basis data.

Kategori utama dari NewSQL meliputi arsitektur baru, middleware sharding transparan, mesin SQL dan DbaaS.
- __Partitioning / Sharding__ : hampir semua sistem manajemen database NewSQL keluar dengan membagi database menjadi subset terpisah yang dikenal sebagai partisi atau pecahan. Tbel secara horisontal dibagi menjadi beberapa fragmen dengan batas berdasarkan nilai kolom. Fragmen terkait dari tabel yang berpartisipasi bergabung membuat partisi.  
- __Replication__ : fitur ini memungkinkan pengguna basis data untuk membuat dan memelihara salinan basis data atau bagian dari basis data. Salinan basis data disimpan disitus jauh di sebelah situs utama atau disitus yang jauh. 
- __Second Indexes__ : indeks sekunder memungkinkan pengguna basis data secara efisin mengakses catatan basis data dengan menggunakan nilai yang berbeda selainkunci utama.
- __Concurrency control__ : fitur ini mengatasi masalah yang mungkin terjadi dalam sistem multi-user ketika banyak pengguna yang mengakses atau memodifikasi data secara bersamaa.
- __Crash recovery__ : database NewSQL memiliki mekanisme yang memungkinkan mereka untuk memulihkan data dan berpindah ke keadaan yang konsisten ketika sistem crash.

Sistem Basis Data NeSQL : ClustrixDB, NuoDB, CockroachDB, Pivatol GemFire XD, Altibase, MemSQL, VolDB, c-treeACE, Percona TokuDB, Apache Trafodion, TIBCO ActiveSpaces, ActorDB.

# MongoDB

### Dokumen Database

catatan dalam MongoDB adalah dokumen, yang merupakan struktur data yang terdiri dari pasangan hidang dan nilai. Nilai - nilai bidang dapat mencakup dokumen lain, array, dan array dokumen.

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/Screenshot%20from%202020-03-15%2022-54-48.png)

MongoDB memberikan knerja tinggi, khususnya :
- Dukungan untuk model data embedded mengurangi aktivitas I / O pada sistem basis data.
- Indeks mendukung permintaan yang lebih cepat dan dapat menyertakan kunci dari dokumen dan array yang disematkan.

### Model Data

Tantangan utama dalam pemodelan data adalah menyeimbangkan kebutuhan aplikasi, karakteristik kinerja mesin database, dan pola pengambilan data. Saat merancang model data, selalu pertimbangkan penggunaan aplikasi data (mis. Kueri, pembaruan, dan pemrosesan data) serta struktur yang melekat dari data itu sendiri.

### Skema Fleksibel

Tidak seperti database SQL, di mana harus menentukan dan mendeklarasikan skema tabel sebelum memasukkan data, koleksi MongoDB, secara default tidak memerlukan dokumennya untuk memiliki skema yang sama. Itu adalah:
1. Dokumen dalam satu kumpulan tidak perlu memiliki kumpulan bidang yang sama dan tipe data untuk bidang dapat berbeda antar dokumen dalam koleksi.
2. Untuk mengubah struktur dokumen dalam koleksi, seperti menambahkan bidang baru, menghapus bidang yang ada, atau mengubah nilai bidang ke jenis baru, perbarui dokumen ke struktur baru.

### Embedded Data

Dokumen embedded menangkap hubungan antara data dengan menyimpan data terkait dalam satu struktur dokumen. Dokumen MongoDB memungkinkan untuk menyematkan struktur dokumen dalam bidang atau array dalam dokumen. Model data yang didenormalisasi ini memungkinkan aplikasi untuk mengambil dan memanipulasi data terkait dalam satu operasi basis data.

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/Screenshot%20from%202020-03-16%2000-04-07.png)

### Reference

Reference menyimpan hubungan antara data dengan menyertakan tautan atau referensi dari satu dokumen ke dokumen lainnya. Aplikasi dapat menyelesaikan referensi ini untuk mengakses data terkait. Secara umum, ini adalah model data yang dinormalisasi.

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/Screenshot%20from%202020-03-16%2000-05-06.png)

