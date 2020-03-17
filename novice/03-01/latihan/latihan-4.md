# MongoDB Reactive Stream Java Drive

### Install 

    <dependencies>
        <dependency>
            <groupId>org.mongodb</groupId>
            <artifactId>mongodb-driver-reactivestreams</artifactId>
            <version>1.11.0</version>
        </dependency>
    </dependencies>

### Reactive Stream

Pusaka ini merupakan implementasi dari spesifikasi aliran reaktif dan API aliran reaktif terdiri dari komponen berikut :
1. Publisher
2. Subscriber
3. Subscription

__Publisher__ adalah penyedia sejumlah elemen sequencing yang berpotensi tidak terbatas, ditebitkan sesuai permintaan yang diterima dari subscriber(s).

Menanggapi panggilan ke Publisher.subscribe(Subscriber) kemungkinan urutan invocation untuk metode pada Subscriber diberikan oleh protokol berikut :

    onSubscribe onNext* (onError | onComplete)?

### Contoh Blocking dan Non Blocking

Karena Subscriber dirilis ketika metode onComplete  dari Subscriber dipanggil, dapat menggunakan ini untuk memblokir dengan memanggil metode wait. Berikut 2 contoh penggunaan permintaan otomatis PrintDocumentSubscriber.
Yang pertama adalah non-blocking dan blok kedua menunggu untuk menyelesaikan Publisher :

    // Create a publisher
    Publisher<Document> publisher = collection.find();

    // Non blocking
    publisher.subscribe(new PrintDocumentSubscriber());

    Subscriber<Document> subscriber = new PrintDocumentSubscriber();
    publisher.subscribe(subscriber);
    subscriber.await(); // Block for the publisher to complete

### Membuat Koneksi

Contok berikut menunjukkan beberapa cara untuk terhubung ke dtaabase mydb di mesin lokal, menggunakan  MongoClients.create helper.

    // To directly connect to the default server localhost on port 27017
    MongoClient mongoClient = MongoClients.create();

    // Use a Connection String
    MongoClient mongoClient = MongoClients.create("mongodb://localhost");

    // or a Connection String
    MongoClient mongoClient = MongoClients.create(new ConnectionString("mongodb://localhost"));

    // or provide custom MongoClientSettings
    ClusterSettings clusterSettings = ClusterSettings.builder().hosts(asList(new ServerAddress("localhost"))).build();
    MongoClientSettings settings = MongoClientSettings.builder().clusterSettings(clusterSettings).build();
    MongoClient mongoClient = MongoClients.create(settings);

    MongoDatabase database = mongoClient.getDatabase("mydb");

### Mendapatkan koneksi

Misalnya, dokumen berisi bidang info yang merupakan dokumen embedded.

    {
    "name" : "MongoDB",
    "type" : "database",
    "count" : 1,
    "info" : {
                x : 203,
                y : 102
                }
    }

Untuk membuat dokumen menjadi java driver, gunakan kelas dokumen. Dapat menggunakan kelas ini untuk membuat dokumen yang disematkan juga.

    Document doc = new Document("name", "MongoDB")
                .append("type", "database")
                .append("count", 1)
                .append("info", new Document("x", 203).append("y", 102));

Untuk memasukkan dokumen kedalam koleksi dapat menggunakan :

    collection.insertOne(doc).subscribe(new OperationSubscriber<Success>());


### Menambahkan Beberapa Dokumen

Untuk menambahkan beberapa dokumen dapat menggunakan metode __insertMany()__. Contoh berikut akan menambahkan beberapa dokumen formulir :

    { "i" : value }

Membuat dokumen didalam loop :

    List<Document> documents = new ArrayList<Document>();
    for (int i = 0; i < 100; i++) {
        documents.add(new Document("i", i));
    }

Untuk menyisipkan  dokumen - dokumen ini ke koleksi, kirimkan daftara dokumen ke insertMany() :

    subscriber = new ObservableSubscriber<Success>();
    collection.insertMany(documents).subscribe(subscriber);
    subscriber.await();

### Menghitung Dokumen dari Koleksi

Sekarang kita telah memasukkan 101 dokumen (100 yang kita lakukan dalam loop, ditambah yang pertama), kita dapat memeriksa untuk melihat apakah kita memiliki semuanya menggunakan metode count(). Kode berikut harus mencetak 101.

    collection.count()
            .subscribe(new PrintSubscriber<Long>("total # of documents after inserting "
                                                + " 100 small ones (should be 101): %s"));

### Meminta Koleksi

Dpat menggunnakana metode find() untuk memdapatkan koleksi.

__Menemukan dokumen pertama dalam koleksi__

Menggunakan metode first() didalam operasi find(). collection.find().first() mengembalikan dokumen pertama atau jika tidak ada dokumen yang ditemukan maka Publisher akan selesai. Ini berguna untuk query yang hanya cocok dengan satu dokumen.

    { "_id" : { "$oid" : "551582c558c7b4fbacf16735" },
    "name" : "MongoDB", "type" : "database", "count" : 1,
    "info" : { "x" : 203, "y" : 102 } }

__Menemukan semua dokumen dalam koleksi__

Untuk mengambil semua dokumen dalam koleksi, menggunakan metode find(). Metode find() mengembalikan instance FindPublisher yang menyediakan antarmuka yang lancar untuk merantai atau mengendalikan operasi find. Kode berikut mengambil semua dokumen dalam koleksi dan mencetaknya (101 dokumen) :

    subscriber = new PrintDocumentSubscriber();
    collection.find().subscribe(subscriber);
    subscriber.await();

### Mendapatkan Dokumen Tunggal dengan FIlter Query

Dapat membuat filter untuk meneruskan ke metode find() untuk mendapatkan subset dokumen dalam koleksi. Misalnya, jika kami ingin menemukan dokumen dengan nilai bidang "i" adalah 71, maka :

    import static com.mongodb.client.model.Filters.*;

    collection.find(eq("i", 71)).first().subscribe(new PrintDocumentSubscriber());

Pada akhirnya akan mencetak satu dokumen :

    { "_id" : { "$oid" : "5515836e58c7b4fbc756320b" }, "i" : 71 }

### Mendapatkan Set Dokumen dengan Query

Dapat menggunakan kueri untuk mendapatkan satu set dokumen dari koleksi. Misalnya, jika ingin mendapatkan semua dokumen dengan "i"> 50, dapat menulis :

    // now use a range query to get a larger subset
    collection.find(gt("i", 50)).subscribe(new PrintDocumentSubscriber());

yang harus mencetak dokumen di mana i > 50. Juga dap mendapatkan rentang, katakanlah 50 <i <= 100 :

    collection.find(and(gt("i", 50), lte("i", 100))).subscribe(new PrintDocumentSubscriber());

### Mensorting Dokumen

Menambahkan pengurutan ke permintaan pencarian dengan memanggil metode sort() pada FindPublisher. Di bawah ini menggunakan exists() dan menyortir desceding("i") untuk menyortir dokumen :

    collection.find(exists("i")).sort(descending("i")).subscribe(new PrintDocumentSubscriber());

### Memproyeksikan Field

Terkadang tidak membutuhkan semua data yang terkandung dalam dokumen. Pembantu Proyeksi dapat digunakan untuk membuat parameter proyeksi untuk operasi pencarian dan membatasi bidang yang dikembalikan.
Di bawah ini akan mengurutkan koleksi, mengecualikan bidang _id dan menghasilkan dokumen yang cocok pertama :

    collection.find().projection(excludeId()).subscribe(new PrintDocumentSubscriber());

### Memperbaharui Dokumen

Untuk memperbarui paling banyak satu dokumen (mungkin 0 jika tidak ada yang cocok dengan filter), gunakan metode updateOne untuk menentukan filter dan memperbaharui dokumen. Di sini memperbarui dokumen pertama yang memenuhi filter i sama dengan 10 dan mengatur nilai i ke 110 :

    collection.updateOne(eq("i", 10), new Document("$set", new Document("i", 110)))
            .subscribe(new PrintSubscriber<UpdateResult>("Update Result: %s"));

Untuk memperbarui semua dokumen yang cocok dengan filter, gunakan metode updateMany. Di sini menambah nilai i dengan 100 di mana i kurang dari 100.

    collection.updateMany(lt("i", 100), new Document("$inc", new Document("i", 100)))
            .subscribe(new PrintSubscriber<UpdateResult>("Update Result: %s"));

Metode pembaruan mengembalikan UpdateResult, yang menyediakan informasi tentang operasi termasuk jumlah dokumen yang diubah oleh pembaruan.

### Menghapus dokumen

Untuk menghapus paling banyak satu dokumen (mungkin 0 jika tidak ada yang cocok dengan filter) gunakan metode deleteOne :

    collection.deleteOne(eq("i", 110))
            .subscribe(new PrintSubscriber<DeleteResult>("Delete Result: %s"));

Untuk menghapus semua dokumen yang cocok dengan filter, gunakan metode deleteMany. Di sini menghapus semua dokumen di mana i lebih besar atau sama dengan 100 :

    collection.deleteMany(gte("i", 100)
            .subscribe(new PrintSubscriber<DeleteResult>("Delete Result: %s"));

Metode hapus mengembalikan DeleteResult, yang menyediakan informasi tentang operasi termasuk jumlah dokumen yang dihapus.
Operasi massal

### operasi massal:


Perintah-perintah ini memungkinkan untuk pelaksanaan operasi insert / update / delete massal. Ada dua jenis operasi massal:
1. Operasi massal yang dipesan.
   Menjalankan semua operasi dalam urutan dan kesalahan pada kesalahan tulis pertama.
2. Operasi massal tidak teratur.
   Menjalankan semua operasi dan melaporkan semua kesalahan.
   Operasi massal tidak teratur tidak menjamin urutan eksekusi.

Mari kita lihat dua contoh sederhana menggunakan operasi yang dipesan dan yang tidak dipesan:
    // 1. Ordered bulk operation - order is guaranteed
    subscriber = new PrintSubscriber<BulkWriteResult>("Bulk write results: %s");
    collection.bulkWrite(
    Arrays.asList(new InsertOneModel<>(new Document("_id", 4)),
                    new InsertOneModel<>(new Document("_id", 5)),
                    new InsertOneModel<>(new Document("_id", 6)),
                    new UpdateOneModel<>(new Document("_id", 1),
                                        new Document("$set", new Document("x", 2))),
                    new DeleteOneModel<>(new Document("_id", 2)),
                    new ReplaceOneModel<>(new Document("_id", 3),
                                        new Document("_id", 3).append("x", 4)))
    ).subscribe(subscriber);
    subscriber.await();

    // 2. Unordered bulk operation - no guarantee of order of operation
    subscriber = new PrintSubscriber<BulkWriteResult>("Bulk write results: %s");
    collection.bulkWrite(
    Arrays.asList(new InsertOneModel<>(new Document("_id", 4)),
                    new InsertOneModel<>(new Document("_id", 5)),
                    new InsertOneModel<>(new Document("_id", 6)),
                    new UpdateOneModel<>(new Document("_id", 1),
                                        new Document("$set", new Document("x", 2))),
                    new DeleteOneModel<>(new Document("_id", 2)),
                    new ReplaceOneModel<>(new Document("_id", 3),
                                        new Document("_id", 3).append("x", 4))),
    new BulkWriteOptions().ordered(false)
    ).subscribe(subscriber);
    subscriber.await();