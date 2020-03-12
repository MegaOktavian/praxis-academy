# Dependency Injection (DI)

Dimana terdapat kelas A yang menggunakan sebuah fungsi dari kelas B, maka itu dikatakan kelas A memiliki keterantungan terhadap kelas B.

![0204](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/02-04/latihan/Screenshot%20from%202020-03-11%2023-31-06.png)

Di Java, sebelum kita menggunakan sebuah metode dari kelas lain, terlebih dahulu kita harus membuat objek kelas tersebu.

    Mentransfer sebuah task untuk membuat objek untuk yang lain dan langsung menggunakan ketergantungan (dependendi) disebut dependency.

Ada 3 jenis ketergantungan :
1. constructor injection : Dependendi disediakan melalui konstruktor kelas
2. setter injection : client memperlihatkan metode setter yang digunakan injektor untuk menyuntikkan dependensi.
3. interface injection : depensi menyediakan metode injektor yang akan menyuntikkan dependensi ke setiap client yang diteruskan kesana. Client harus mengimplementasikan antarmuka yang memperlihatkan metode setter yang menerima ketergantungan.

### Inversion of control

Ini mnyatakan bahwa suatu kelas tidak boleh mengkonfigurasi dependensinya secara statis tetapi harus dikonfigurasi oleh beberapa kelas lain dari luar.

Kelas harus berkosentrasi pada memenuhi tanggung jawabnya dan bukan pada menciptakan objek yang diperlukan untuk memenuhi tanggung jawab itu. Disinilah Dependency Injection berperan dimana menyediakan kelas dengan objek yang diperlukan.

Keuntungan Memakai DI :
1. Membantu pengujian.
2. Kode pelat ketel dikurangi, karena inisialisasi dependensi dilakukan oleh komponen injektor.
3. Memperluas aplikasi menjadi lebih mudah.
4. Membantu mengaktifkan kopling longgar, yang penting dalam pemrograman aplikasi.

Kekurangan dari DI :
1. Agak sulit untuk dipelajari, dan jika digunakan secara berlebihan dapat menyebabkan masalah manajemen dan masalah lainnya.
2. Banyak kesalahan waktu kompilasi didorong ke run-time.
3. Kerangka kerja injeksi ketergantungan diimplementasikan dengan refleksi atau pemrograman dinamis. Ini dapat menghambat penggunaan otomatisasi IDE, seperti "temukan referensi", "tunjukkan hierarki panggilan" dan refactoring yang aman.

Library dan Framwork yang diimplentasikan DI
o Spring (Java)
o Google Guice (Java)
o Dagger (Java dan Android)
o Castle Windsor (.NET)
o Unity (.NET)

Contoh :

Jika memiliki kelas Employee dan karyawan memiliki Address, maka dpat menentukan kelas Employee sebagai berikut :

    class Employee {
        private Address address;

        // constructor 
        public Employee( Address newAddress ) {
            this.address = newAddress;
        }

        public Address getAddress() {
        return this.address;
        }
        public void setAddress( Address newAddress ) {
            this.address = newAddress;
        }
    }

Kode ini menunjukkan kepunyaan antara employee dan address. Sekarang menciptakan hubungan kepemilikan di antara mereka :

    Address someAddress = ....
    Employee oscar = new Employee( someAddress ); 

Maslaah utama muncul ketika menguji satu objek tertentu, diperlukan membuat instance dan instance objek lain untuk melakukan itu. Untu mengundari itu, dapat menggunakan konstruktor :

    public Employee(){
    }

Menggunakan konstrunktor no args. Kemudian dapat mengatur alamat kapanpun :

    Address someAddress = ....
    Employee oscar = new Employee();
    oscar.setAddress( someAddress ); 

Jika dimiliki beberapa atribut atau jika objek sulit dibuat, tambahkan atribut Depatement :

    class Employee {
        private Address address;
        private Department department;

    ....

Jika Anda memiliki 300 karyawan, dan semuanya harus memiliki departemen yang sama, dan ditambah departemen yang sama harus dibagi antara beberapa objek lain (seperti daftar departemen perusahaan, atau peran yang dimiliki masing-masing departemen, dll) maka akan mengalami kesulitan dengan visibilitas objek Departemen dan untuk membaginya melalui semua jaringan objek.

Asumsikan file properti untuk injector dependensi fiktif :

    #mock employee
    employee.address = MockAddress.class
    employee.department = MockDepartment.class

    #production setup 
    employee.address = RealAddress.class
    employee.department = RealDepartment.class

Kerangka Dependency Injector akan mengatur objek yang benar, sehingga tidak perlu kode setAddress atau setDepartment. Ini akan dilakukan dengan refleksi atau oleh pembuatan kode atau teknik lainnya.

### IoC dan DI

Contoh bagaimana pengaturan aplikasi Django menggunakan setting.py :