# mongoShell

Menjalankan MongoDB berjalan di localhost gunakan perintah :

    mongo

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%201/Screenshot%20from%202020-03-16%2000-54-27.png)

untuk menamplkan basis data yang sedang digunakan ketikkan berintah :

    db

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%202/Screenshot%20from%202020-03-16%2001-13-17.png)

Untuk memunculkan daftar database yang tersedia bagi pengguna menggunakan perintah :

    show dbs

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%202/Screenshot%20from%202020-03-16%2001-16-27.png)


Untuk berpindah satabase dapat menggunakan perintah :

    use <database>, misalkan: use admin

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%202/Screenshot%20from%202020-03-16%2001-18-36.png)

Contoh, berikut ini membuat database myNewDatabase dan myCollection collection selama operasi insertOne ():

    use myNewDatabase
    db.myCollection.insertOne( { x: 1 } );

- db merujuk ke database saat ini.
- myCollection adalah nama koleksi.

Jika mongo shell tidak menerima nama koleksi, dapat menggunakan sintaks db.getCollection() sebagai alternatif. Misalnya, jika nama koleksi berisi spasi atau tanda hubung, dimulai dengan angka, atau konflik dengan fungsi bawaan:

    db.getCollection("3 test").find()
    db.getCollection("3-test").find()
    db.getCollection("stats").find()

Untuk memformat hasil yang dicetak, Anda dapat menambahkan .pretty() ke operasi, seperti berikut ini:

    db.myCollection.find().pretty()

Selain itu, dapat menggunakan metode cetak eksplisit berikut di mongo shell:
- print() untuk mencetak tanpa memformat
- print(tojson (<obj>)) untuk dicetak dengan format JSON dan setara dengan printjson ()
- printjson () untuk mencetak dengan format JSON dan setara dengan mencetak (tojson (<obj>))

Jika mengakhiri garis dengan tanda kurung terbuka ('('), tanda kurung buka ('{'), atau tanda kurung terbuka ('['), maka baris berikutnya mulai dengan ellipsis ("...") hingga masukkan kurung tutup yang sesuai (')'), kurung kurawal ('}') atau kurung tutup (']'). Cangkang mongo menunggu tanda kurung tutup, kurung kurawal, atau braket penutup sebelum mengevaluasi kode, seperti dalam contoh berikut :

    > if ( x > 0 ) {
    ... count++;
    ... print (x);
    ... }

atau :

    > if (x > 0
    ...
    ...
    >

