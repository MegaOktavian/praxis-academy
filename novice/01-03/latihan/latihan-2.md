# Object Oriented Programming

Mendesain program menjadi fungsi misalkan clok dari pernyataan yang memanipulasi data disebut pemrograman procedure-oriented. Kelas dan objek adalah dua aspek utama dari pemrograman berorientasi objek. Sebuah class menciptakan jenis baru dimana objek adalah instances (atribut) dari kelas. Analoginya jika kamu mempunyai varibel tipe int yang diterjemahkan dengan mengatakan bahwa variabel yang menyimpan bilangan bulat adalah variabel yang merupakan instances (objek) dari int class. Objek dapat menyimpan data menggunakan variabel biasa milik objek. 
    Variabel yang dimiliki suatu objek atau kelas disebut fields (bidang).
Objek juga memiliki fungsionalitas dengan menggunakan fungsi yang dimiliki class. Fungsi semacam ini disebut Method kelas. 
    Bidang dan method dapat disebut atribut kelas.

### Class

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/latihan%202/Screenshot%20from%202020-03-04%2004-15-46.png)

Membuat class baru diikuti blok pernyataan yang membentuk lekukan kelas. Blok ini kosong yang diindikasi dengan pass statement. Kemudian membuat objek atau instance menggunakan nama kelas diikuti (). Kemudian mengkonfirmasi jenis variable dengan mencetaknya.

### Method

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/latihan%202/Screenshot%20from%202020-03-04%2004-15-58.png)

Disini method say_hi tidak mengambil parameter tetapi masih memiliki self definisi fungsi.

### Method _init_

Method __init__ dijalankan segera sebagai objek dari suatu kelas adalah initialization (yaitu dibuat).

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/latihan%202/Screenshot%20from%202020-03-04%2004-16-06.png)

__init__ metode mengambil parameter name (bersama dengan self). Dibuat juga fields baru bernama name.Disini terdapat dua variabel berbeda walaupun memiliki nama yang sama yaitu name. self.name berarti ada sesuatu yang disebut "name" yang merupakan bagian dari objek yang disebut "self" dan yang "name" yang satunya adalah variabel lokal. Kemudian membuat instance baru bernama p dari kelas Person, diikuti oleh argumen dalam tanda kurung. Kemudian menggunakan self_name yang ditunjukan dengan say_hi.

### Variabel Class dan Objek

    Variabel class - mereka dapat diakses oleh semua instance dari kelas itu. Hanya ada satu salinan variabel  kelas dan ketika salah satu objek membuat perubahan ke variabel kelas, perubahan ini akan diperlihatkan oleh semua instance lainnya.

    Variabel objek dimiliki oleh setiap individu / instance dari kelas. Dalam hal ini setiap objek memiliki salinan bidangnya sendiri yaitu mereka tidak dibagikan dan tidak terkait dengan bidang apapun dengan nama yang sama dalam contoh yang berbeda.

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/latihan%202/Screenshot%20from%202020-03-04%2004-40-00.png)

population  milik kelas Robot yang merupakan variabel kelas. variabel name milik objek dan karenanya variabel name merupakan variabel objek. variabel kelas population sebagai Robot.population dan bukan sebagai self.population. Variabel objek name menggunakan notasi self.name dalam metode objek tersebut.

how_many adalah metode yang dimiliki kelas dan bukan milik objek. Ini berarti didefinisikan sebagai classmethod atau staticmethod, tergantung pada kelas yang diikuti. Karena ini merujuk ke variabel kelas, maka gunakan classmethod.

metode how_many ditandai sebagai metode kelas menggunakan decorator. Dekorator diumpamakan sebagai jalan pintas untuk memanggil fungsi pembungkus, sehingga menerapkan @classmethod dekorator sama dengan memanggil : 

    how_many = classmethod(how_many)

__init__ digunakan untuk menginisialisasi Robot instance dengan nama. Dalam metode ini ditambahkan population jumlah dengan 1 karena ada satu robot lagi yang ditambahkan. Variabel dan objek yang sama hany menggunakan self. ini disebut _referensi_ _atribut_.

### Inheritance

Salah satu keuntungan utama OOP adalah penggunaan kembali kode dan salah satu cara ini dicapai melalui mekanisme pewarisan (Inheritance). Inheritance dapat dibayangkan sebagai penerapan hubungan type dan subtype antar kelas.

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/latihan%202/Screenshot%20from%202020-03-04%2004-52-38.png)

Untuk menggunakan pewarisan, tentukan nama kelas dasar dalam sebuah tuple mengikuti nama kelas dalam definisi kelas. Metode __init__ dari kelas dasar secara eksplisit disebut menggunakan self variabel sehingga dapat dianalisi bagian kelas dasar dari sebuah instance dalam subkelas. Python tidak secara otomatis memanggil konstruktor dari kelas dasar SchoolMember, tetapi harus secara eksplisit menyebutnya sendiri. Sebaliknya, jika belum mendefinisikan metode __init__ dalam sebuah subkelas, Python akan memanggil konstruktor dari kelas dasar secara otomatis.

# Classes

### Classes

Kelas menyediakan cara menggabungkan data dan fungsionalitas bersama. Membuat kelas baru menciptakan tipe objek baru, memungkinkan instance baru dari tipe itu dibuat. Setiap instance kelas dapat memiliki atribut yang melekat padanya untuk mempertahankan statenya.

    Namespace adalah pemetaan dari nama ke objek.

Misalnya dalam "z.real" dimana "real adalah atribut objek "z".

Atribut hanya dapat dibaca atau ditulis. Atribut yang dapat ditulis juga dapat dihapus dengan pernyataan. Misalnya menghapus dengan del statment. del modname.the_answer akan menghapus atribut the_answer dari objek yang bernama modname.

    Lingkup (Scope) adalah wilayah tekstual dari program Python dimana namespace secara langsung dapat diakses yang berarti bahwa referensi yang tidak memenuhi syarat untuk suatu nama berusaha untuk menemukan nama tersebut di namespace.

Ada 3 cakupan bersarang yang namespacenya dapat diakses :
* Ruang lingkup terdalam- yang dicari pertama kali, berisi nama - nama lokal
* Lingkup dari setiap fungsi penutup terdekat, berisi nama non-lokal, tetapi juga non-global
* Lingkup next-to-last berisi nama global modul saat ini
* Ruang lingkup terluar adalah namespace yang mengandung nama bawaan

    Pernyataan global dapat digunakan untuk menunjukkan bahwa variabel tertentu hidup di global scope.

Berikut adalah contoh yang menunjukkan cara mereferensikan cakupan dan namespace yang berbeda, dan bagaimana global dan nonlocal mempengaruhi pengikan variabel

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/latihan%202/Screenshot%20from%202020-03-04%2009-02-40.png)

Sintak definisi class sebagai berikut :

    class ClassName:
        <statement-1>
        .
        .
        .
        <statement-N>

Definisi class seperti definisi fungsi harus dieksekusi sebelum mereka memiliki efek. Pernyataan didalam definisi kelas biasanya akan menjadi definisi fungsi. Definisi fungsi didalam kelas biasanya memiliki bentuk khusus daftar argumen, didikte oleh konvensi pemanggilan untuk metode.

### Class Objects

Class object mendukung dua jenis operasi yaitu referensi atribut dan instantiasi.

    Referensi atribut menggunakan syntax standar yang digunakan untuk semua referensi atribut dengan Python : obj.name. Nama atribut yang valid adalah semua nama yang ada di namespace kelas ketika objek kelas dibuat.

    class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

MyClass.i dan MyClass.f adalah referensi atribut yang valid, masing - masing mengembalikan integer dan fungsi objek. Atribut kelas juga dapat ditetapkan, sehingga dapat mengubah nilai dari MyClass.i berdasarkan penugasan. __doc__ juga merupakan atribut yang valid, mengembalikan docstring milik kelas "A simple example class"

    Instansiasi kelas menggunakan notasi fungsi. Hanya berpura - pura bahwa objek kelas adalah fungsi tanpa parameter yang mengembalikan instance baru dari kelas. Misal : 

    X = MyClass()

Membuat instance baru dari kelas dan menetapkan objek ini ke variabel lokal x.

Operasi instansi ("memanggil" objek kelas) membuat objek kosong. Banyak kela yang suka membuat objek dengan instance yang disesuaikan dengan kondisi awal tertentu. Oleh karen aitu kelas dapat mendefinisikan kode khusus yang dinamai __init__(), seperti :

    def __init__ (self):
        self.data = []

Ketika sebuah kelas mendefinisikan sebuah metode __init__(), instantiasi kelas secara otomatis memanggil __init__() untuk instance kelas yang dibuat baru. Inisialisasi dapat diperoleh dengan :

    x = MyClass()

Metode __init__() mungkin memiliki argumen untuk fleksibilitas yang lebih besar.

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/latihan%202/Screenshot%20from%202020-03-04%2014-43-30.png)

### Instance Object

    Instance objek adalah atribut.

Ada dua jenis nama atribut yang valid, atribut data, dan metode.

    Atribut data tidak perlu dinyatakan seperti variabel lokal. Misalnya, jika x adalah instance dari MyClass dibuat diatas, potongan kode akan mencetak nilai 16.

    x.counter = 1
    while x.counter < 10:
        x.counter = x.counter
    print(x.counter)
    del x.counter


    Metode adalah fungsi "milik" sebuah objek.

Nama metode yang valid dari instance object bergantung pada kelasnya. Menurut definisi, semua atribut kelas yang merupakan objek fungsi menentukan metode yang disesuaikan dari instance-nya. x.f adalah referensi metode yang valid, karena MyClass.f merupakan fungsi, tetapi x.f bukan hal yang sama seperti MyClass.f yang merupakan method object buka function object.

### Method Object

    x.f()

Misalnya di MyClass, ini akan mengembalikan string 'hello world'. Namun itu tidak memanggil segera metode: x.f adalah method object, dan dapat disipan dan dipanggil dilain waktu.

    xf = x.f
    while True:
        print(xf())

Akan terus mencetak hello world sampai waktu berakhir. x.f() dipanggil tanpa argumen diatas meskipun definisi fungsi untuk f() argumen tertentu.

Memanggil metode dengan daftar argumen n sama dengan memanggil fungsi yang sesuai dengan daftar argumen yang dibuat dengan menyisipkan instance object metode sebelum argumen pertama.

### variabel Class dan Intsance

    Variabel instance adalah untuk data unik untuk setiap instance.

    Variabel kelas adalah untuk atribut dan metode yang dibagikan oleh semua instance kelas.

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/latihan%202/Screenshot%20from%202020-03-04%2015-20-13.png)

Berbagi data dapat memiliki efek yang mengejutkan dengan melibatkan objek yang dapat berubah seperti list dan dictionary. Misalnya daftar trick dalam kode berikut tidak boleh digunakan sebagai variabel kelas karena hanya satu daftar yang akan dibagikan oleh semua instance Dog : 

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/latihan%202/Screenshot%20from%202020-03-04%2015-33-47.png)

Desain kelas yang benar menggunakan variabel instan sebagai gantinya :

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/latihan%202/Screenshot%20from%202020-03-04%2015-38-30.png.png)

### Random Remarks

Jika nama atribut yang sama muncul dikedua instance dan dikelas, maka pencarian atribut memproritaskan instance :

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/latihan%202/Screenshot%20from%202020-03-04%2016-06-01.png)

Objek fungsi apa pun yang merupakan atribut kelas menentukan metode untuk instance dari kelas itu. Tidak perlu bahwa definisi fungsi secara teks tertutup dalam definisi kelas: menetapkan objek fungsi ke variabel lokal di kelas juga ok. Sebagai contoh:

    # Function defined outside the class
    def f1(self, x, y):
        return min(x, x+y)

    class C:
        f = f1

        def g(self):
            return 'hello world'

        h = g

Metode dapat memanggil metode lain dengan menggunakan atribut metode dari argumen mandiri:

    class Bag:
    def __init__(self):
        self.data = []
    
    def add(self, x):
        self.data.append(x)
    
    def addtwice(self, x):
        self.add(x)
        self.add(x)

### Inheritance

Sintak

    class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>

Nama BaseClassName harus didefinisikan dalam lingkup yang berisi definisi kelas turunan. Di tempat nama kelas dasar, ekspresi sewenang-wenang lainnya juga diperbolehkan. Ini bisa berguna, misalnya, ketika kelas dasar didefinisikan dalam modul lain:

    class DerivedClassName(modname.BaseClassName):

Eksekusi dari definisi kelas turunan menghasilkan sama seperti untuk kelas dasar. Ketika objek kelas dibangun, kelas dasar diingat. Ini digunakan untuk menyelesaikan referensi atribut: jika atribut yang diminta tidak ditemukan di kelas, pencarian dilanjutkan untuk mencari di kelas dasar. Aturan ini diterapkan secara rekursif jika kelas dasar itu sendiri berasal dari beberapa kelas lain.

Python memiliki dua fungsi bawaan yang bekerja dengan inheritance :
- Gunakan isinstance() untuk memeriksa tipe instance: isinstance(obj, int) akan Benar hanya jika obj.__class__ adalah int atau beberapa kelas berasal dari int.
- Gunakan issubclass() untuk memeriksa warisan kelas: issubclass (bool, int) Benar karena bool adalah subclass dari int. Namun, issubclass(float, int) adalah False karena float bukan subclass dari int.

### Multiple Inheritance

Sintak :

    class DerivedClassName(Base1, Base2, Base3):
        <statement-1>
        .
        .
        .
        <statement-N>

Urutan dinamis diperlukan karena semua kasus pewarisan berganda menunjukkan satu atau lebih hubungan intan (di mana setidaknya satu dari kelas induk dapat diakses melalui beberapa jalur dari kelas bawah).

### Private Variables

Variabel instance "Privat" yang tidak dapat diakses kecuali dari dalam objek yang tidak ada di Python.

Name mangling sangat membantu untuk membiarkan subclass menimpa metode tanpa memutus panggilan metode intraclass. Sebagai contoh:

    class Mapping:
        def __init__(self, iterable):
            self.items_list = []
            self.__update(iterable)

        def update(self, iterable):
            for item in iterable:
                self.items_list.append(item)

        __update = update   # private copy of original update() method

    class MappingSubclass(Mapping):

        def update(self, keys, values):
            # provides new signature for update()
            # but does not break __init__()
            for item in zip(keys, values):
                self.items_list.append(item)

### Odds dan Ends

Definisi kelas kosong akan berhasil:

    class Employee:
    pass

    john = Employee()  # Create an empty employee record

    # Fill the fields of the record
    john.name = 'John Doe'
    john.dept = 'computer lab'
    john.salary = 1000

### Iterators

Pernyataan for :

    for element in [1, 2, 3]:
        print(element)
    for element in (1, 2, 3):
        print(element)
    for key in {'one':1, 'two':2}:
        print(key)
    for char in "123":
        print(char)
    for line in open("myfile.txt"):
        print(line, end='')

Pernyataan for memanggil iter() sebagai objek penampung. Fungsi return sebuah iterator object yang mendefinisikan metode __next__() yang mengakses elemen dalam wadah satu per satu. Ketika tidak ada lagi elemen, __next __ () memunculkan eksepsi StopIteration yang memberi tahu for loop untuk mengakhiri. Dapat memanggil metode __next __ () menggunakan fungsi built-in next ();

metode __iter __ () yang mengembalikan objek dengan metode __next __ (). Jika kelas mendefinisikan __next __ (), maka __iter __ () dapat mengembalikan diri:

    class Reverse:
        """Iterator for looping over a sequence backwards."""
        def __init__(self, data):
            self.data = data
            self.index = len(data)

        def __iter__(self):
            return self

        def __next__(self):
            if self.index == 0:
                raise StopIteration
            self.index = self.index - 1
            return self.data[self.index]

### Generators

Generator adalah alat sederhana dan kuat untuk membuat iterator. Mereka ditulis seperti fungsi biasa tetapi menggunakan pernyataan hasil setiap kali mereka ingin mengembalikan data. Setiap kali next () dipanggil, generator melanjutkan di mana ia tinggalkan. Sebuah contoh menunjukkan bahwa generator dapat dengan mudah dibuat:

    def reverse(data):
        for index in range(len(data)-1, -1, -1):
            yield data[index]

### Ekspresi Generator

Beberapa generator sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaksis yang mirip dengan pemahaman daftar tetapi dengan tanda kurung alih-alih tanda kurung siku. Contoh :

![0103](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-03/latihan%202/Screenshot%20from%202020-03-04%2016-17-42.png)
