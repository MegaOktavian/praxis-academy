# Kelanjutan OOP

### Inheritance Revisited

Dengan Inheritance, satu atau lebih kelas turunan dapat mewarisi atribut dan metode dari kelas dasar. Ini mengurangi duplikasi, dan berarti bahwa setiap perubahan yang dilakukan pada kelas dasar akan secara otomatis diterjemahkan ke kelas turunan. Sebagai ulasan:

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/latihan%201/Screenshot%20from%202020-03-05%2001-45-34.png)

kelas turunan tidak memerlukan metode __init__ mereka sendiri karena kelas dasar __init__ dipanggil secara otomatis. Namun, jika mendefinisikan __init__ di kelas turunan, ini akan menimpa basis :

    class Animal:
        def __init__(self,name,legs):
            self.name = name
            self.legs = legs

    class Bear(Animal):
        def __init__(self,name,legs=4,hibernate='yes'):
            self.name = name
            self.legs = legs
            self.hibernate = hibernate

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/latihan%201/Screenshot%20from%202020-03-05%2001-50-53.png)

### Multiple Inheritance

Terkadang masuk akal bagi kelas yang diturunkan untuk mewarisi kualitas dari dua atau lebih kelas dasar. Python memungkinkan untuk ini dengan pewarisan berganda.

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/latihan%201/Screenshot%20from%202020-03-05%2003-04-24.png)

Kelas turunan dari objek Bensin dan Listrik :

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/latihan%201/Screenshot%20from%202020-03-05%2003-16-18.png)

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/latihan%201/Screenshot%20from%202020-03-05%2003-16-47.png)

### Mengapa memakai self ?

 Python menggunakan self untuk menemukan set atribut dan metode yang tepat untuk diterapkan pada objek. Ketika kita mengatakan :

    prius.recharge ()

Apa yang sebenarnya terjadi adalah bahwa Python pertama-tama mencari kelas milik prius (Hybrid), dan kemudian meneruskan prius ke metode Hybrid.recharge ().

Ini sama dengan menjalankan:

    Hybrid.recharge (prius)

### Method Resolution Order (MRO)

Banyak hal menjadi rumit ketika Anda memiliki beberapa kelas dasar dan tingkat warisan. Ini diselesaikan dengan menggunakan Method Resolution Order.

    MRO adalah rencana formal yang Python ikuti saat menjalankan metode objek.

Sebagai ilustrasi, jika kelas B dan C masing-masing berasal dari A, dan kelas D berasal dari B dan C, kelas mana yang "pertama dalam garis" ketika sebuah metode dipanggil pada D?
Pertimbangkan yang berikut ini:

    class A:
        num = 4
        
    class B(A):
        pass

    class C(A):
        num = 5
        
    class D(B,C):
        pass

Secara skematis, hubungannya terlihat seperti ini :

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/latihan%201/Screenshot%20from%202020-03-05%2003-40-36.png)

Di sini num adalah atribut kelas yang dimiliki oleh keempat kelas.  Jika D.num dipanggil :

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/latihan%201/Screenshot%20from%202020-03-05%2003-43-36.png)

### super()

Fungsi built-in super () Python menyediakan jalan pintas untuk memanggil kelas dasar, karena secara otomatis mengikuti MRO.

Dalam bentuknya yang paling sederhana dengan pewarisan tunggal, super () dapat digunakan sebagai pengganti nama kelas dasar:

    class MyBaseClass:
        def __init__(self,x,y):
            self.x = x
            self.y = y
        
    class MyDerivedClass(MyBaseClass):
        def __init__(self,x,y,z):
            super().__init__(x,y)
            self.z = z

Dalam bentuk yang lebih dinamis, dengan banyak pewarisan seperti "diagram berlian" yang ditunjukkan di atas, super () dapat digunakan untuk mengelola definisi metode dengan benar:

    class A:
        def truth(self):
            return 'All numbers are even'
        
    class B(A):
        pass

    class C(A):
        def truth(self):
            return 'Some numbers are even'

![0104](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-04/latihan%201/Screenshot%20from%202020-03-05%2004-01-30.png)