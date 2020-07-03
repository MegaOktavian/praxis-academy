# Menjalankan Program

### Tools yang digunakan
* Visual Studio Code
* Postman

### Modul yang harus diinstall

    pip install pipenv

![gambar 1](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2000-48-59.png)

    pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow os

![gambar 2](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-05-19.png)

![gambar 3](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-06-44.png)

### Untuk Database
1. Jalankan python di terminal

        python

2. Jalankan perintah berikut :

        from app import db
        db.create_all()
        exit()

![gambar 4](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-12-01.png)

### Running
1. Buka terminal Visual Studio Code dan aktifkan Virtual Environment

        pipenv shell

![gambar 5](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-12-18.png)

2. Jalankan file

        python app.py

![gambar 6](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-16-43.png)

### Menampilkan data menggunakan Postman
1. Untuk menampilkan semua data metode yang digunakan GET

        http://localhost:5000/product

![gambar 7](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-19-44.png)

2. Untuk menampilkan satu data dari id data (user_id)

        http://localhost:5000/product/1

![gambar 8](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-20-00.png)

### Menambahkan data menggunakan Postman
1. Untuk menampilkan data metode yang digunakan metode POST

        http://localhost:5000/product

2. Pada bagian Headers, pada *KEY* masukkan **Content-Type** dan pada *VALUE* masukkan **application/json**

![gambar 9](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-26-14.png)

3. Pada bagian Body pilih **raw**, masukkan data yang diinginkan sesuai atribut yang ada (user_id, user_name, email, password) kemudian send

![gambar 10](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-29-18.png)

4. Pada metode GET, data telah disimpan

        http://localhost:5000/product

![gambar 11](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-31-11.png)

### Mengubah data menggunakan Postman
1. Untuk mengubah data metode yang digunakan metode PUT (sesuai user_id data)

        http://localhost:5000/product/2

2. Pada bagian Headers, pada *KEY* masukkan **Content-Type** dan pada *VALUE* masukkan **application/json**

![gambar 9](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-26-14.png)

3. Pada bagian Body pilih **raw**, masukkan data yang diinginkan sesuai atribut yang ada (user_id, user_name, email, password) kemudian send

![gambar 12](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-40-46.png)

Setelah diubah

![gambar 13](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-42-11.png)

4. Pada metode GET, data telah diubah

        http://localhost:5000/product/

![gambar 14](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-42-36.png)

### Menghapus data menggunakan Postman
1. Untuk menghapus data metode yang digunakan metode DELETE (sesuai user_id data)

        http://localhost:5000/product/2

![gambar 15](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-45-26.png)

![gambar 12](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-40-46.png)

Setelah dihapus

![gambar 16](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-45-34.png)

4. Pada metode GET, data telah dihapus

        http://localhost:5000/product/

![gambar 17](https://github.com/MegaOktavian/rhymes/blob/master/projek%20bootcamp-online/1/Screenshot%20from%202020-07-03%2001-45-47.png)