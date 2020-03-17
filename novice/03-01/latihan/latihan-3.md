# Operasi MongoDB CRUD

### Create

mongoDB menyediakan metode berikut untuk memasukkan dokumen  ke dalam koleksi :

    db.collection.insertOne()
    db.collection.insertMany()

Semua operasi penulisan di MongoDB adalah atom pada tingkat satu dokumen :

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%203/Screenshot%20from%202020-03-16%2003-30-07.png)

### Read

Operasi read menfambil dokumen dan koleksi : yaitu meminta koleksi untuk dokumen. MongoDB  menyediakan metode berikut untuk membaca dokumen dari koleksi :

    db.collection.find()

Dapat menentukan query atau kriteria yang mengidentifikasi dokumen untuk dikembalikan :

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%203/Screenshot%20from%202020-03-16%2003-41-47.png)

### Update

Operasi update memodifikasi dokumen yang ada dalam koleksi. MongoDB  menyediakan metode berikut untuk memperbaharui dokumen dari koleksi :

    db.collection.updateOne()
    db.collection.updateMany()
    db.collection.replaceOne()

Dapat menuliskan kriteria atau filter yang mengidentifikasi dokumen yang akan diperbaharui. Filter ini menggunakan sintaks yang sama dengan operasi read.

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%203/Screenshot%20from%202020-03-16%2003-41-58.png)

### Delete

Operasi delete menghapus dokumen dari koleksi. MongoDB  menyediakan metode berikut untuk menghapus dokumen dari koleksi :

    db.collection.deleteOne()
    db.collection.deleteMany()

Dapat menuliskan kriteria atau filter yang mengidentifikasi dokumen yang akan dihapus. Filter ini menggunakan sintaks yang sama dengan operasi read.

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%203/Screenshot%20from%202020-03-16%2003-42-14.png)