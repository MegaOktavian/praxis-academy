# Functional Programming

    adalah gaya pengkodean yang  berfokus pada menentukan apa yang harus dilakukan, daripada melakukan beberapa tindakan.

### Karakteristik Functional Programming

1. Berfungsi sebagai objek kelas satu, yang berarti bahwa harus dapat menerapkan semua konstruk menggunakan data, untuk fungsi juga.
2. Fungsi murni; seharusnya tidak ada efek samping di dalamnya
3. Cara dan konstruksi untuk membatasi penggunaan untuk loop
4. Dukungan yang baik untuk rekursi

### Berfungsi sebagai objek kelas pertama dalam python:

Fungsi int digunakan sebagai parameter untuk memetakan fungsi :

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2014-15-22.png)

Menetapkan fungsi hello_world, dan variabel akan dieksekusi sebagai fungsi :

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2014-23-24.png)

Menyimpan fungsi dalam list :

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2014-25-12.png)

### Kemurnian fungsional python

    def naive_sum(list):
        s = 0
        for l in list:
            s += l
        return s

    naive_sum(list)

Dapat diganti menjadi :

    sum(list)

### Mengurangi Penggunaan Loop didalam python

    for x in l:
        func(x)

Dapat diubah menjadi :

    map(func, l)

Jika menerapkannya pada eksekusi fungsi berurutan, maka :

    def func1():
        pass

    def func2():
        pass

    def func3():
        pass

    executing = lambda f: f()
    map(executing, [func1, func2, func3])

### Rekursi Python

    Rekursi adalah metode pemecahan masalah ke dalam sub-masalah yang pada dasarnya dari jenis yang sama dengan masalah asli.

Rekursi pada dasarnya perlu memenuhi dua syarat. Harus ada suatu kondisi dimana ekursi harus berakhir, dan itu harus memanggil dirinya sendiri untuk semua kondisi lainnya. Kondisi akhir harus membatasi, yaitu fungsinya harus memanggil fungsi yang lebih kecil darinya.

Contoh menghasilkan angka fibonacci melalui rekursi :

    def fib(n):
        if n == 0: return 0
        elif n == 1: return 1
        else: return fib(n-1)+fib(n-2)

Mengubah kode prosedural menjadi fungsional :

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2014-42-52.png)

Kode prosedural dapat ditulis secara fungsional. Contoh diatas alih - alih memberikan nstruksi eksplisit tentang cara melakukannya, malah memberikan instruksi tentang apa yang harus dilakukan.


![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2014-46-41.png)

Python mampu mendukung pemrograman fungsional relatif mudah karena semua yang ada didalam python adalah objek. Itu berarti bahwa definisi fungsi dapat ditugaskan ke variabel yang diedarkan.

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2015-00-50.png)

### Lambda

Sintaks "lamda" memungkinkan untuk membuat fungsi dengan cara deklaratif. Istilah lain untuk konsep ini adalah "fungsi anonim", karena fungsi lamda dapat digunakan in-line tanpa pernah benar - benar membutuhkan nama.

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2015-04-03.png)

    "callable" adalah segala sesuatu yang dapat dipanggil dengan tanda kurung 
    - kelas praktis, fungsi dan metode.

Penggunaan paling umum adalah untuk mendeklarasikan prioritas relatif melalui kunci argumen ketika menyortir struktur data.

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2015-08-57.png)

    Kelemahan dari fungsi lamda inline adalah mereka muncul tanpa nama dalam tumpukan jejak, yang membuat proses debug lebih sulit.

### Functools

Peta menerapkan fungsi mengembalikan urutan hasil, dan mengurangi menggunakan fungsi untuk mengumpulkan setiap item dalam urutan menjadi nilai tunggal.

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2015-14-53.png)

Ada tumpukan fungsi lainnya yang memanipulasi fungsi dengan cara lain, tertama parsial yang mengunci beberapa parameter ke fungsi. Juga dikenal sebagaoi "currying".

    def power(base, exp):
        return base ** exp
    cube = partial(power, exp=3)
    cube(5)  # returns 125

### Dekorator

Salah satu cara untuk mendeklarasikan dekorator adalah menggunakan tanda @ yang pada dasarnya untuk melewai fungsi yang didekorasi sebagai argumen kepada dekorator. Berikut adalah contoh dekorator yang mengatur kembali sebuah kode dan mengembalikan niali sukses pertama, atau menyerah dan meningkatkan pengecualian baru terbaru setelah 3 upaya.

    def retry(func):
        def retried_function(*args, **kwargs):
            exc = None
            for _ in range(3):
                try:
                return func(*args, **kwargs)
                except Exception as exc:
                print("Exception raised while calling %s with args:%s, kwargs: %s. Retrying" % (func, args, kwargs).

            raise exc
        return retried_function

    @retry
    def do_something_risky():
        ...

    retried_function = retry(do_something_risky)  # No need to use `@`

Dekorator memberikan jenis dan nilai input dan output yang sama persis - tetapi ini bukan keharusan. Dekorator dapat menambah artau menghapus argumen atau mengubah tipenya. Mereka juga dapat dikonfigurasi melalui parameter itu sendiri.

### FUngsi Murni (Pure Function)

Contoh non-fungsional : 

    dictionary = ['fox', 'boss', 'orange', 'toes', 'fairy', 'cup']
    def puralize(words):
    for i in range(len(words)):
        word = words[i]
        if word.endswith('s') or word.endswith('x'):
            word += 'es'
        if word.endswith('y'):
            word = word[:-1] + 'ies'
        else:
            word += 's'
        words[i] = word

    def test_pluralize():
        pluralize(dictionary)
        assert dictionary == ['foxes', 'bosses', 'oranges', 'toeses', 'fairies', 'cups']

Untuk menjadikannya fungsi murni, dapat ditulis ulang menjadi :

    dictionary = ['fox', 'boss', 'orange', 'toes', 'fairy', 'cup']
    def puralize(words):
    result = []
    for word in words:
        word = words[i]
        if word.endswith('s') or word.endswith('x'):
            plural = word + 'es')
        if word.endswith('y'):
            plural = word[:-1] + 'ies'
        else:
            plural = +  's'
        result.append(plural)
        return result

    def test_pluralize():
        result = pluralize(dictionary)
        assert result == ['foxes', 'bosses', 'oranges', 'toeses', 'fairies', 'cups']

### Memahami (dan Menghindari) Mutabilitas

Ketika membagikan dict/list/set, mereka dapat bermutasi secara tak terduga dalam beberapa konteks lain. Ini berantarakan untuk debug. parameter default yang dapat berubah - ubah adalah kasus klasik dari ini.

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2016-16-55.png)

### Membatasi Penggunaan Kelas

    from collections import namedtuple
    VerbTenses = namedtuple('VerbTenses', ['past', 'present', 'future'])
    # versus
    class VerbTenses(object):
        def __init__(self, past, present, future):
            self.past = past,
            self.present = present
            self.future = future

Jika ingin menyediakan sumber status dan banyak tampilan ke kondisi itu dengan cara mengubahnya, maka gunakanlah kelas.

Atribut kelas yang dapat diubah sangat berbahaya, karena mereka memiliki definisi kelas, bukan turunannya sehingga dapat berakhir secara tidak sengaja bermutasi pada kelas yang sama.

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2016-24-51.png)

# Konsep Functional Programming

    Bahasa deklaratif memberitahu omputer hasil apa yang diinginkan. Sedangkan bahasa impretatif memberitahu komputer langkah apa yang harus diambil untuk menyelesaikan masalah.

Fitur - fitur Haskell :
1. Pure function : tidak memiliki efek samping, mereka tidak mengubah keadaaan program. Dengan input yang sama, fungsi murni akan selalu menghasilkan output yang sama.
2. Immutability : data tidak dapat diubah setelah dibuat.
3. Higher order function : fungsi dapat menerima fungsi lain sebagai parameter dan fungsi dapat mengembalikan fungsi baru sebagai output.

### Pure Function

Untuk mendapatkannya, jangan mengubah nilai input atau data yang ada diluar cakupan fungsi. Ini akan membuat fungsi yang ditulis lebih mudah untuk diuji. 

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2016-41-40.png)

Daftar asli number tidak berubah, dan tidak mereferensikan variabel lain diluar fungsi.

### Immutability

Ada beberapa tipe data yang tid dapat diubah, salah satunya adalah tuple.

Berikut adalah contoh tipe data yang dapat diubah - ubah :

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2016-47-45.png)

Kesaahan yang terjadi adalah TypeError: 'tuple' object does not support item assignment.

Berikut ini mungkin tule tampak seperti objek yang dapat berubah. Misalnya jika ingin mengubah daftar immutable_collection dari [4, 5] menjadi [4, 5, 6] : 

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2016-53-33.png)

Ini berfungsi karena objek List adalah objek yang dapat diubah.

### Higher Order Functions

    Higher Order Functions menerima fungsi sebagai argumen atau mengembalikan fungsi untuk diproses lebih lanjut.

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2016-56-03.png)

Bagaimana jika kita ingin menulis ke file 5 kali, atau mencatat pesan 5 kali? Alih-alih menulis 3 fungsi berbeda yang semuanya loop, kita dapat menulis 1 Fungsi Orde Tinggi yang menerima fungsi-fungsi tersebut sebagai argumen :

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2016-58-28.png)

Sekarang bayangkan kita ditugasi membuat fungsi yang menambah angka dalam daftar dengan 2, 5, dan 10.

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2017-00-07.png)

Meskipun sepele untuk menulis fungsi add5 dan add10, sudah jelas bahwa mereka akan beroperasi dengan fungsi yang sama : mengulang daftar dan menambahkan incrementer. Jadi alih-alih membuat banyak fifferent increment functions, kami membuat 1 Higher Order Function :

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2017-02-03.png)

### Ekspresi Lamda

Ekspresi lamda memungkinkan untuk mendefinisikan fungsi jauh lebih cepat. Membuat Higher Order Function hof_product yang mengembalikan fungsi yang mengalikan angka dengan nilai yang telah ditentukan :

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2017-07-59.png)

Ekspresi lamda dimulai dengan kata kunci lamda diikuti oleh argumen fungsi. Setelah titik dua adalah kode yang dikembalikan oleh lamda.

## Built-in Higher Order Functions

### Map

Fungsi map memungkinkan untuk menerapkan fungsi untuk setiap elemen dalam suatu objek iterable.
Misalnya, jika kami memiliki daftar nama dan ingin menambahkan salam kepada Strings, kami dapat melakukan hal berikut :

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2017-13-07.png)

### Filter

Fungsi filter mengetes setiap elemen dalam suatu objek iterable dengan fungsi yang kembali baik True atau False.

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2017-15-06.png)

### Menggabungkan map dengan filter

Karena setiap fungsi mengembalikan iterator, dan keduanya menerima objek yang dapat diubah, kita dapat menggunakannya bersama untuk beberapa manipulasi data yang sangat ekspresif.

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2017-22-15.png)

Ekspresi dalam arbitrary_numbers dapat dipecah menjadi 3 bagian :
o range(1, 21) adalah objek iterable yang mewakili angka dari 1, 2, 3, 4 ... 19, 20.
o filter(lambda num: num % 3 == 0, range(1, 21)) adalah sebuah iterator untuk urutan nomor 3, 6, 9, 12, 15 dan 18.
o Ketika mereka dipotong dadu oleh ekspresi peta kita bisa mendapatkan iterator untuk urutan nomor 27, 216, 729, 1728, 3375 dan 5832.

### Daftar Pemahaman

Mari kita coba contoh sebelumnya dengan map dan filter dengan pemahaman daftar sebagai gantinya :

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2017-38-07.png)

Jika ingin memfilter objek, maka perlu menggunakan kata kunci if :

![0201](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-01/latihan/Screenshot%20from%202020-03-09%2017-39-44.png)

Setiap ekspresi map dan filter dapat dinyatakan sebagai pemahaman daftar.