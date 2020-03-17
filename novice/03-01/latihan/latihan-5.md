# Menggunakan Motor dengan Tornado

Menginstall module motor dengan menggunakan pip :

    pip install tornado motor

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%205/Screenshot%20from%202020-03-16%2005-23-50.png)

Memulai mongoDB menggunakan perintah :

    mongo

![0301](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-01/latihan/latihan%205/Screenshot%20from%202020-03-16%2005-28-59.png)

Mengimpor modul :

    import motor.motor_tornado

### Hierarki Objek

Motor seperti PyMongo, merepresentasikan data dengan hierarki objek 4 tingkat:
1. MotorClient mewakili proses mongod, atau sekelompok dari mereka.
2. MotorDatabase : Setiap mongod memiliki satu set database (set file data yang berbeda pada disk).
3. MotorCollection: Database memiliki satu set koleksi, yang berisi dokumen.
4. MotorCursor: Mengeksekusi find() pada MotorCollection mendapat MotorCursor, yang mewakili sekumpulan dokumen yang cocok dengan kueri.

### Membuat Client

Dapat menggunakan satu instance MotorClient pada saat aplikasi dimulai :

    client = motor.motor_tornado.MotorClient()

Dapat menentukan host dan port seperti :

    client = motor.motor_tornado.MotorClient('localhost', 27017)

Motor juga mendukung koneksi URL :

    client = motor.motor_tornado.MotorClient('mongodb://localhost:27017')

Menguhungkan ke set replika seperti :

    client = motor.motor_tornado.MotorClient('mongodb://host1,host2/?replicaSet=my-replicaset-name')

