# Install MongoDB

1. Buka hamlaman website berikut :
   https://docs.mongodb.com/manual/installation/

2. Pilih penginstallan MongoDB sesuai sistem operasi ubuntu.

   https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
   
   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%201/Screenshot%20from%202020-03-16%2000-26-14.png)

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%201/Screenshot%20from%202020-03-16%2000-26-21.png)

3. Impor kunci publik yang digunakan oleh sistem manajemen paket. Buka terminal dan ketikkan perintah :

    wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%201/Screenshot%20from%202020-03-16%2000-36-17.png)

4. Membuat file daftar untuk MongoDB
   /etc/apt/sources.list.d/mongodb-org-4.2.list

   Untuk Ubuntu 18.04 gunakan perintah :

    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%201/Screenshot%20from%202020-03-16%2000-36-37.png)

5. Muat ulang basis data paket lokal, gunakan perintah :

    sudo apt-get update

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%201/Screenshot%20from%202020-03-16%2000-38-39.png)

6. Install pakrt MongoDB menggunakan perintah :

    sudo apt-get install -y mongodb-org

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%201/Screenshot%20from%202020-03-16%2000-43-48.png)

   untuk mencegah peningkatan yang tidak diinginkan, dapat menyematkan paket pada versi yang saat ini diinstal:

    echo "mongodb-org hold" | sudo dpkg --set-selections
    echo "mongodb-org-server hold" | sudo dpkg --set-selections
    echo "mongodb-org-shell hold" | sudo dpkg --set-selections
    echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
    echo "mongodb-org-tools hold" | sudo dpkg --set-selections

    ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%201/Screenshot%20from%202020-03-16%2000-47-20.png)

7. Memulai mongoDB menggunakan perintah :

    sudo service mongod start
   
   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%201/Screenshot%20from%202020-03-16%2000-49-13.png)

   Verifikasi bahwa MongoDB berhasil dijalankan :

    sudo service mongod status

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%201/Screenshot%20from%202020-03-16%2000-49-23.png)

   Untuk menghentikan MongoDB dapat menggunakan perintah :

    sudo service mongod stop

  Memulai ulang MongoDB :

    sudo service mongod restart

   memulai menggunakan MongoDB :

    mongo

   ![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%201/Screenshot%20from%202020-03-16%2000-54-27.png)
