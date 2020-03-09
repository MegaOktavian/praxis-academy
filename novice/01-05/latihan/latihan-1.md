# Serialisasi Data
## Pickle

    Modul pickle digunakan untuk membuat serial dan menderialisasi struktur objek python.

    Pickling adalah proses dimana hierarki objek python dikonversi menjali aliran byte.

    Unpickling adalah kebalikan dari proses Pickling dimana aliran byte diubah menjadi hierarki objek.

### Modul Antarmuka

    dumps() : fungsi ini dipanggil untuk mengelompokkan hierarki objek.

    load() : fungsi ini dipanggil untuk menghilangkan aliran data serial.

### Konstanta yag disediakan oleh modul pickle

1. pickle.HIGHEST_PROTOCOL
   Adalah nilai integer yang mewakili versi protokol tertinggi yang tersedia.
2. pickle.DEFAULT_PROTOCOL
   Adalah nili int yang mewakili protokol default yang digunakan untuk pengawetan yang nilainya mungkin kurang dari nilai protokol tertinggi.

### Fungsi yang disediakan oleh modul pickle :

1. pickle.dump(obj, file, protocol = None, *, fix_imports = True)
   Setara dengan Pickler(file, protocol).dump(obj). Ini digunakan untuk menulis reprsentasi pickle objek file objek file terbuka.

    Argumen protokol ini adalah bilangan bulat yang memberi tahu pickler untuk menggunakan protokol yang diberikan.

    Protokol yang didukung adalah 0 hingga HIGHEST_PROTOCOL.

    Jika tidak ditentukan, standarnya adalah DEFAULT_PROTOCOL.

    Jika angka negatif ditentukan, HIGHEST_PROTOCOL dipilih.

Contoh :


    # Python program to illustrate 
    # pickle.dump() 
    import pickle 
    from StringIO import StringIO 
    
    class SimpleObject(object): 
    
        def __init__(self, name): 
            self.name = name 
            l = list(name) 
            l.reverse() 
            self.name_backwards = ''.join(l) 
            return
    
    data = [] 
    data.append(SimpleObject('pickle')) 
    data.append(SimpleObject('cPickle')) 
    data.append(SimpleObject('last')) 
    
    # Simulate a file with StringIO 
    out_s = StringIO() 
    
    # Write to the stream 
    for o in data: 
        print 'WRITING: %s (%s)' % (o.name, o.name_backwards) 
        pickle.dump(o, out_s) 
        out_s.flush() 

Output :

    WRITING: pickle (elkcip)
    WRITING: cPickle (elkciPc)
    WRITING: last (tsal)

2. pickle.dumps(obj, protocol = None, *, fix_imports = True)

   Fungsi ini mengembalikan representasi pickle objek sebagi objek byte

Contoh :


    #Python program to illustrate 
    #Picle.dumps() 
    import pickle 
    
    data = [ { 'a':'A', 'b':2, 'c':3.0 } ] 
    data_string = pickle.dumps(data) 
    print 'PICKLE:', data_string 

Output : 

    PICKLE: (lp0
    (dp1
    S'a'
    p2
    S'A'
    p3
    sS'c'
    p4
    F3.0
    sS'b'
    p5
    I2
    sa.

3. pickle.load(file, *, fix_imports = True, encoding = “ASCII”, errors = “strict”)

   Fungsi ini setara dengan Unpickler(file).load(). Fungsi ini digunakan untuk membaca representasi objek pickle dari file objek file terbuka dan mengenbalikan hierarki objek yang ditentukan.

Contoh :

    # Python program to illustrate 
    # pickle.load() 
    import pickle 
    from StringIO import StringIO 
    
    class SimpleObject(object): 
    
        def __init__(self, name): 
            self.name = name 
            l = list(name) 
            l.reverse() 
            self.name_backwards = ''.join(l) 
            return
    
    data = [] 
    data.append(SimpleObject('pickle')) 
    data.append(SimpleObject('cPickle')) 
    data.append(SimpleObject('last')) 
    
    # Simulate a file with StringIO 
    out_s = StringIO() 
    
    
    # Write to the stream 
    for o in data: 
        print 'WRITING: %s (%s)' % (o.name, o.name_backwards) 
        pickle.dump(o, out_s) 
        out_s.flush() 
        
        
    # Set up a read-able stream 
    in_s = StringIO(out_s.getvalue()) 
    
    # Read the data 
    while True: 
        try: 
            o = pickle.load(in_s) 
        except EOFError: 
            break
        else: 
            print 'READ: %s (%s)' % (o.name, o.name_backwards) 

Output :

    WRITING: pickle (elkcip)
    WRITING: cPickle (elkciPc)
    WRITING: last (tsal)
    READ: pickle (elkcip)
    READ: cPickle (elkciPc)
    READ: last (tsal)

4. pickle.loads(bytes_object, *, fix_imports = True, encoding = “ASCII”, errors = “strict”)

   Fugsi ini digunakan untuk membaca objek pickle dari objek byte dan mengembalikan hierarki objek rekontruksi yang ditentukan.

Contoh :

![0105](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-05/latihan/Screenshot%20from%202020-03-08%2023-18-07.png)

### Pengecualian

1. exception pickle.PickleError
   Pengecualian ini mewarisi Exception. Ini adalah kelas dasar untuk smeua pengecualian lain yang diangkat dalam pickler

2. exception pickle.PicklingError
   Pengecualian ini mewarisi PickleError. Pengecualian ini muncul ketika objek yang tidak dapat di klik ditemukan di pickler.

3. exception pickle.UnpicklingError
   Pengecualian ini mewarisi PickleError. Pengecualian ini muncul ketika ada masalah seperti korupsi data atau pelanggaran keamanan saat membongkar objek.

### Kelas yang di ekspor

1. class pickle.Pickler(file, protocol = None, *, fix_imports = True)
   
   Kelas ini mengambil file biner untuk menulis aliran data pickle.

    dump(objek) : fungsi ini digunakan untuk menulis representasi pickle objek ke file terbuka yang diberikan dalam konstruktor

    persistent_id(obj) : jika persistent_id() mereturn None, objek adalah pickle seperti biasa.

    Fast : mode cept menonaktifkan penggunaan memo dan mempercepat proses pengawetan dengantidak menghasilkan kode PUT yang berlebihan.

    Dispatch_table : adalah kelas dan nilainya adalah fungsi reduksi. Secara default, objek pickler tidak aka memiliki atribut dispatch_table dan sebagai gantinya akan menggunakan tabel pengiriman global yang dikelola oleh modul copyreg.

Contoh :

    f = io.BytesIO()
    p = pickle.Pickler(f)
    p.dispatch_table = copyreg.dispatch_table.copy()
    p.dispatch_table[SomeClass] = reduce_SomeClass

2. class pickle.Unpickler(file, *, fix_imports = True, encoding = “ASCII”, errors = “strict”)

   Kelas ini emngambil file biner untuk membaca aliran data pickle.

    load() : digunakan untuk membaca representasi objek pickle dari file objek file terbuka dan mengembalikan objek dari ghierarki objek rekonstruksi yang ditentukan.

    persistent_load(pid) : memunculkan UnpicklingError secara default.

    find_class(module, name) : fungsi ini mengimpor modul jika diperlukan dan mengembalikan objek bernama name, dimana argumen modul dan nama adlah objek str.

### Instance kelas pickling

1. object.__getnewargs_ex__() 
   Metode ini menentukan nilai yang diteruskan ke metode __new __() setelah dibongkar. Metode harus mengembalikan pasangan (args, kwargs) di mana args adalah tuple dari argumen posisional dan kwargs kamus argumen bernama untuk membangun objek.
2. object.__getnewargs__()
   Metode ini hanya mendukung argumen positif. Itu harus mengembalikan tuple argumen args yang akan diteruskan ke metode __new __() setelah dibongkar.
3. object.__getstate__()
   Jika metode ini didefinisikan oleh kelas, itu disebut dan objek yang dikembalikan diambil sebagai konten untuk instance, bukan isi kamus instance.
4. object.__setstate__(state)
   Jika metode ini didefinisikan oleh kelas, itu disebut dengan status tidak dikunci. Status acar harus berupa kamus dan item-itemnya ditugaskan ke kamus instance baru.
5. object.__reduce__()
   Metode __reduce __() tidak mengambil argumen dan akan mengembalikan string atau lebih disukai tupel.
6. object.__reduce_ex__(protocol)
   Metode ini mirip dengan metode __reduce__. Dibutuhkan argumen integer tunggal. Penggunaan utama untuk metode ini adalah untuk memberikan nilai pengurangan yang kompatibel dengan mundur untuk rilis Python yang lebih lama.

Contoh pickle :

Mengabadikan objek dengan memanggil fungsi dumps() yang melewatkan objek yang akan diambil sebagai parameter .

![0105](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-05/latihan/Screenshot%20from%202020-03-09%2000-15-13.png)

![0105](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-05/latihan/Screenshot%20from%202020-03-09%2000-16-47.png)

## Unpickling

    Unpickling adalah proses yang mengambil array biner dan mengonversinya menjadi hierarki objek disebut

Proses unpickling dilakukan dengan menggunakan fungsi load() dari modul pickle dan mengembalikan hierarki objek lengkap dari array byte sederhana. Mari kita coba menggunakan fungsi muat pada contoh di atas:

![0105](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-05/latihan/Screenshot%20from%202020-03-09%2000-24-47.png)

    Tidak semua objek dapat dipilih (seperti koneksi DB). Beberapa objek tidak dapat di pickle dan mencoba untuk mem-pickle objek yang unpickable.

Contoh :

    import pickle

    my_custom_pickle = bytes("this is unpicklable", encoding="UTF-8")

    # this next statement will raise a _pickle.UnpicklingError
    my_new_object = pickle.loads(my_custom_pickle)

Terdapat dua metode untuk menentukan apa yang ingin untuk pickle dan bagaimana menginisialisasi ulang objek yang belum di pickle sebelumnya. Metode ini adalah  setstate() dan getstate().

Contoh :

    import pickle

    class my_zen_class:
        number_of_meditations = 0
        def __init__(self, name):
            self.number_of_meditations = 0
            self.name = name

        def meditate(self):
            self.number_of_meditations = self.number_of_meditations + 1
        
        def __getstate__(self):
            # this method is called when you are 
            # going to pickle the class, to know what to pickle

            state = self.__dict__.copy()

            # You will never get the Buddha state if you count 
            # meditations, so 
            # don't pickle this counter, the next time you will just 
            # start meditating from scratch :)
            del state['number_of_meditations']

            return state

        def __setstate__(self, state):
            # this method is called when you are going to 
            # unpickle the class,
            # if you need some initialization after the 
            # unpickling you can do it here.

            self.__dict__.update(state)

    # I start meditating
    my_zen_object = my_zen_class("Dave")
    for i in range(100):
        my_zen_object.meditate()

    # Now I pickle my meditation experience
    print(str.format("I'm {0}, and I've meditated {1} times'", my_zen_object.name, my_zen_object.number_of_meditations))
    my_pickled_zen_object = pickle.dumps(my_zen_object)
    my_zen_object = None

    # Now I get my meditation experience back
    my_new_zen_object = pickle.loads(my_pickled_zen_object)

    # As expected, the number_of_meditations property 
    # has not been restored because it hasn't been pickled
    print(str.format("I'm {0}, and I don't have a beginner mind yet because I've meditated only {1} times'", my_new_zen_object.name, my_new_zen_object.number_of_meditations))

![0105](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-05/latihan/Screenshot%20from%202020-03-09%2000-37-43.png)

## pickle — Python object serialization

    "Pickling" adalah proses di mana hierarki objek Python diubah menjadi stream byte, dan "unpickling" adalah operasi terbalik, di mana stream byte (dari file biner atau objek byte-like) dikonversi kembali menjadi hierarki objek. 

### Perbandingan pickle dengan marshall

o Modul acar melacak objek yang telah diserialkannya, sehingga nantinya referensi ke objek yang sama tidak akan diserialisasi lagi. Marshal tidak melakukan ini.

    Objek rekursif adalah objek yang berisi referensi untuk diri mereka sendiri. 

o Marshal tidak dapat digunakan untuk membuat serialisasi kelas yang ditentukan pengguna dan instance-nya. Pickle dapat menyimpan dan mengembalikan instance kelas secara transparan, namun definisi kelas harus dapat diimpor dan hidup dalam modul yang sama seperti ketika objek disimpan.
o Format serialisasi marshal tidak dijamin portabel di versi Python. Karena tugas utamanya dalam kehidupan adalah untuk mendukung file .pyc, pelaksana Python berhak untuk mengubah format serialisasi dengan cara yang tidak kompatibel dengan mundur jika diperlukan.

### Perbandingan pickle dengan json

o JSON adalah format serialisasi teks, sementara pickle adalah format serialisasi biner.
o JSON mudah dibaca oleh manusia, sedangkan acar tidak.
o JSON bersifat interoperable dan banyak digunakan di luar ekosistem Python, sementara pickle bersifat spesifik-Python.
o JSON, secara default hanya bisa mewakili subset dari tipe bawaan Python, dan tidak ada kelas khusus. Pickle dapat mewakili sejumlah besar tipe Python.

### Pickling Class Instances

Dalam kebanyakan kasus, tidak ada kode tambahan yang diperlukan untuk membuat instance dapat dipilih. Secara default, pickle akan mengambil kelas dan atribut instance melalui introspeksi. Ketika sebuah instance kelas tidak di unpickle, metode __init __() biasanya tidak dipanggil. Perilaku default pertama kali membuat instance yang tidak diinisialisasi dan kemudian mengembalikan atribut yang disimpan. Kode berikut menunjukkan implementasi dari perilaku ini:

    def save(obj):
        return (obj.__class__, obj.__dict__)

    def load(cls, attributes):
        obj = cls.__new__(cls)
        obj.__dict__.update(attributes)
        return obj

### Persistence of External Objects

Untuk kepentingan persistence objek, modul acar mendukung gagasan referensi ke objek di luar aliran data pickle. Objek tersebut direferensikan oleh ID persisten, yang harus berupa string karakter alfanumerik (untuk protokol 0) atau hanya objek arbitrer (untuk protokol yang lebih baru).

Berikut ini adalah contoh komprehensif yang menunjukkan bagaimana ID persisten dapat digunakan untuk pickle objek eksternal dengan referensi :

# Simple example presenting how persistent ID can be used to pickle
# external objects by reference.

    import pickle
    import sqlite3
    from collections import namedtuple

    # Simple class representing a record in our database.
    MemoRecord = namedtuple("MemoRecord", "key, task")

    class DBPickler(pickle.Pickler):

        def persistent_id(self, obj):
            # Instead of pickling MemoRecord as a regular class instance, we emit a
            # persistent ID.
            if isinstance(obj, MemoRecord):
                # Here, our persistent ID is simply a tuple, containing a tag and a
                # key, which refers to a specific record in the database.
                return ("MemoRecord", obj.key)
            else:
                # If obj does not have a persistent ID, return None. This means obj
                # needs to be pickled as usual.
                return None


    class DBUnpickler(pickle.Unpickler):

        def __init__(self, file, connection):
            super().__init__(file)
            self.connection = connection

        def persistent_load(self, pid):
            # This method is invoked whenever a persistent ID is encountered.
            # Here, pid is the tuple returned by DBPickler.
            cursor = self.connection.cursor()
            type_tag, key_id = pid
            if type_tag == "MemoRecord":
                # Fetch the referenced record from the database and return it.
                cursor.execute("SELECT * FROM memos WHERE key=?", (str(key_id),))
                key, task = cursor.fetchone()
                return MemoRecord(key, task)
            else:
                # Always raises an error if you cannot return the correct object.
                # Otherwise, the unpickler will think None is the object referenced
                # by the persistent ID.
                raise pickle.UnpicklingError("unsupported persistent object")


    def main():
        import io
        import pprint

        # Initialize and populate our database.
        conn = sqlite3.connect(":memory:")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE memos(key INTEGER PRIMARY KEY, task TEXT)")
        tasks = (
            'give food to fish',
            'prepare group meeting',
            'fight with a zebra',
            )
        for task in tasks:
            cursor.execute("INSERT INTO memos VALUES(NULL, ?)", (task,))

        # Fetch the records to be pickled.
        cursor.execute("SELECT * FROM memos")
        memos = [MemoRecord(key, task) for key, task in cursor]
        # Save the records using our custom DBPickler.
        file = io.BytesIO()
        DBPickler(file).dump(memos)

        print("Pickled records:")
        pprint.pprint(memos)

        # Update a record, just for good measure.
        cursor.execute("UPDATE memos SET task='learn italian' WHERE key=1")

        # Load the records from the pickle data stream.
        file.seek(0)
        memos = DBUnpickler(file, conn).load()

        print("Unpickled records:")
        pprint.pprint(memos)


    if __name__ == '__main__':
        main()

![0105](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-05/latihan/Screenshot%20from%202020-03-09%2002-43-20.png)

### Dispatch Tables

Jika seseorang ingin mengkustomisasi pickle beberapa kelas tanpa mengganggu kode lain yang tergantung pada acar, maka seseorang dapat membuat pickler dengan tabel dispatch pribadi.

Tabel dispatch global yang dikelola oleh modul copyreg tersedia sebagai copyreg.dispatch_table. Oleh karena itu, orang dapat memilih untuk menggunakan salinan copyreg.dispatch_table yang dimodifikasi sebagai tabel dispatch pribadi.
Contoh :

    f = io.BytesIO()
    p = pickle.Pickler(f)
    p.dispatch_table = copyreg.dispatch_table.copy()
    p.dispatch_table[SomeClass] = reduce_SomeClass

menciptakan instance pickle.Pickler dengan tabel pengiriman pribadi yang menangani kelas SomeClass khusus. Atau, kodenya :

    class MyPickler(pickle.Pickler):
        dispatch_table = copyreg.dispatch_table.copy()
        dispatch_table[SomeClass] = reduce_SomeClass
    f = io.BytesIO()
    p = MyPickler(f)

melakukan hal yang sama, tetapi semua instance MyPickler secara default akan berbagi tabel pengiriman yang sama. Kode yang setara menggunakan modul copyreg adalah

    copyreg.pickle(SomeClass, reduce_SomeClass)
    f = io.BytesIO()
    p = pickle.Pickler(f)

### Menangani Objek Stateful

Kelas TextReader membuka file teks, dan mengembalikan nomor baris dan konten baris setiap kali metode readline () dipanggil. Jika instance TextReader di-pickled, semua atribut kecuali anggota objek file disimpan. Ketika instance dihapuskan, file dibuka kembali, dan membaca dilanjutkan dari lokasi terakhir. Metode __setstate __() dan __getstate __() digunakan untuk mengimplementasikan perilaku ini.

class TextReader:
    """Print and number lines in a text file."""

    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename)
        self.lineno = 0

    def readline(self):
        self.lineno += 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]
        return "%i: %s" % (self.lineno, line)

    def __getstate__(self):
        # Copy the object's state from self.__dict__ which contains
        # all our instance attributes. Always use the dict.copy()
        # method to avoid modifying the original state.
        state = self.__dict__.copy()
        # Remove the unpicklable entries.
        del state['file']
        return state

    def __setstate__(self, state):
        # Restore instance attributes (i.e., filename and lineno).
        self.__dict__.update(state)
        # Restore the previously opened file's state. To do so, we need to
        # reopen it and read from it until the line count is restored.
        file = open(self.filename)
        for _ in range(self.lineno):
            file.readline()
        # Finally, save the file.
        self.file = file

Contoh mengizinkan pickling dan merekonstruksi kelas yang diberikan :

    import io
    import pickle

    class MyClass:
        my_attribute = 1

    class MyPickler(pickle.Pickler):
        def reducer_override(self, obj):
            """Custom reducer for MyClass."""
            if getattr(obj, "__name__", None) == "MyClass":
                return type, (obj.__name__, obj.__bases__,
                            {'my_attribute': obj.my_attribute})
            else:
                # For any other object, fallback to usual reduction
                return NotImplemented

    f = io.BytesIO()
    p = MyPickler(f)
    p.dump(MyClass)

    del MyClass

    unpickled_class = pickle.loads(f.getvalue())

    assert isinstance(unpickled_class, type)
    assert unpickled_class.__name__ == "MyClass"
    assert unpickled_class.my_attribute == 1

Contoh penerapan subclass bytearray yang dapat berpartisipasi dalam pickling buffer out-of-band :

    class ZeroCopyByteArray(bytearray):
        def __reduce_ex__(self, protocol):
            if protocol >= 5:
                return type(self)._reconstruct, (PickleBuffer(self),), None
            else:
                # PickleBuffer is forbidden with pickle protocols <= 4.
                return type(self)._reconstruct, (bytearray(self),)

        @classmethod
        def _reconstruct(cls, obj):
            with memoryview(obj) as m:
                # Get a handle over the original buffer object
                obj = m.obj
                if type(obj) is cls:
                    # Original buffer object is a ZeroCopyByteArray, return it
                    # as-is.
                    return obj
                else:
                    return cls(obj)

### Restricting Globals

Secara default, unpickling akan mengimpor semua kelas atau fungsi yang ditemukannya dalam acar data.

![0105](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-05/latihan/Screenshot%20from%202020-03-09%2003-14-55.png)

Pada contoh diatas, unpickler klik impor fungsi os.system () dan kemudian terapkan argumen string "echo hello world".

    import builtins
    import io
    import pickle

    safe_builtins = {
        'range',
        'complex',
        'set',
        'frozenset',
        'slice',
    }

    class RestrictedUnpickler(pickle.Unpickler):

        def find_class(self, module, name):
            # Only allow safe classes from builtins.
            if module == "builtins" and name in safe_builtins:
                return getattr(builtins, name)
            # Forbid everything else.
            raise pickle.UnpicklingError("global '%s.%s' is forbidden" %
                                        (module, name))

    def restricted_loads(s):
        """Helper function analogous to pickle.loads()."""
        return RestrictedUnpickler(io.BytesIO(s)).load()

Untuk kode paling sederhana, gunakan fungsi dump () dan load ().

![0105](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-05/latihan/Screenshot%20from%202020-03-09%2003-22-20.png)

![0105](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/01-05/latihan/Screenshot%20from%202020-03-09%2003-22-53.png)

### Data Serialization

    adalah proses konversi data terstruktur ke format yang memungkinkan berbagi atau penyimpanan data dalam bentuk yang memungkinkan pemulihan struktur aslinya.

Gaya flat :

    { "Type" : "A", "field1": "value1", "field2": "value2", "field3": "value3" }

Gaya nested : 

    {"A"
    { "field1": "value1", "field2": "value2", "field3": "value3" } }

### File sederhana (data flat)

Jika data yang akan diserialisasi berada dalam file dan berisi data datar, Python menawarkan dua metode :

1. repr
   Metode repr di Python mengambil parameter objek tunggal dan mengembalikan representasi input yang dapat dicetak:

        # input as flat text
        a =  { "Type" : "A", "field1": "value1", "field2": "value2", "field3": "value3" }

        # the same input can also be read from a file
        a = open('/tmp/file.py', 'r')

        # returns a printable representation of the input;
        # the output can be written to a file as well
        print(repr(a))

        # write content to files using repr
        with open('/tmp/file.py') as f:f.write(repr(a))

2. ast.literal_eval
   Metode literal_eval dengan aman mem-parsing dan mengevaluasi ekspresi untuk tipe data Python. Jenis data yang didukung adalah: strings, numbers, tuples, lists, dicts, booleans, dan None.

    with open('/tmp/file.py', 'r') as f: inp = ast.literal_eval(f.read())

### FIle CSV

Modul CSV dengan Python mengimplementasikan kelas untuk membaca dan menulis data tabular dalam format CSV.

Contoh sederhana untuk membaca:

    # Reading CSV content from a file
    import csv
    with open('/tmp/file.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

Contoh sederhana untuk menulis:

    # Writing CSV content to a file
    import csv
    with open('/temp/file.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(iterable)

### YAML (data bersarang)
Ada banyak modul pihak ketiga untuk mengurai dan membaca / menulis struktur file YAML dengan Python. Salah satu contohnya adalah di bawah ini :

    # Reading YAML content from a file using the load method
    import yaml
    with open('/tmp/file.yaml', 'r', newline='') as f:
        try:
            print(yaml.load(f))
        except yaml.YAMLError as ymlexcp:
            print(ymlexcp)

### File JSON (data bersarang)
Modul JSON Python dapat digunakan untuk membaca dan menulis file JSON.
Menulis

    # Reading JSON content from a file
    import json
    with open('/tmp/file.json', 'r') as f:
        data = json.load(f)

Menulis

    # Writing JSON content to a file using the dump method
    import json
    with open('/tmp/file.json', 'w') as f:
        json.dump(data, f, sort_keys=True)

### XML (data bersarang)
Penguraian XML dengan Python dimungkinkan menggunakan paket xml.
Contoh:

    # reading XML content from a file
    import xml.etree.ElementTree as ET
    tree = ET.parse('country_data.xml')
    root = tree.getroot()

### Biner : NumPy Array (data datar)
Array NumPy Python dapat digunakan untuk membuat serial dan deserialisasi data ke dan dari representasi byte.

import NumPy as np

    # Converting NumPy array to byte format
    byte_output = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]).tobytes()

    # Converting byte format back to NumPy array
    array_format = np.frombuffer(byte_output)

### Biner : Pickle (data bersarang)
Modul serialisasi data asli untuk Python disebut Pickle.
Ini sebuah contoh:

    import pickle

    #Here's an example dict
    grades = { 'Alice': 89, 'Bob': 72, 'Charles': 87 }

    #Use dumps to convert the object to a serialized string
    serial_grades = pickle.dumps( grades )

    #Use loads to de-serialize an object
    received_grades = pickle.loads( serial_grades )