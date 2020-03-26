# Template Processor

![0303](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-03/readme1/Screenshot%20from%202020-03-25%2020-22-57.png)

Template processor (yang juga dikenal __template engine__ atau __template parser__) adalah software yang dirancang untuk menggabungkan template dengan model data untuk menghasilka dokumen. Fitur - fiturnya :
- Variabel dan fungsi
- Pengganti teks
- Inklusi file
- Evaluasi bersyarat dan loop

### Embedded Template Engines

Sementara pengolah template biasanya merupakan bagian terpisah dari perangkat lunak, digunakan sebagai bagian dari suatu sistem atau kerangka kerja, bahasa templating sederhana biasanya dimasukkan dalam fitur pemrosesan string dari bahasa pemrograman untuk tujuan umum, dan dalam program pemrosesan teks, terutama editor teks atau pengolah kata.

### Elemen Sistem

__Model data__
Ini dapat berupa database relasional, file sumber seperti XML, forma alternatif dari file flat database, spreadsheet atau berbagai sumber data lainnya.

__Sumber template__
- Menurut bahasa pemrograman yang sudah ada sebelumnya
- Menurut bahasa template yang ditentukan secara khusus
- Sesuai dengan fitur aplikasi perangkat lunak hosting
- Menurut kombinasi hibrida dari beberapa atau semua hal di atas

__Mesin template__
Mesin template bertanggung jawab untuk :
- Menghubungkan ke model data;
- Memproses kode yang ditentukan dalam templat sumber
- Mengarahkan output ke pipa, file teks, atau aliran tertentu

__Dokumen Hasil__
Ini dapat terdiri dari seluruh dokumen atau fragmen dokumen.

### Penggunaan

__Mesin template__
adalah jenis khusus dari modul pemrosesan template yang menunjukkan semua fitur utama dari bahasa pemrograman modern. Tujuan utamanya adalah untuk memproses template dan data untuk menghasilkan teks. Penggunaan instilah ini diterapkan untuk pengembangan web menggunakan sistem template we, dan diterapkan dalam konteks lain.

__Pembuatan dokumen__
Kerangka kerja pembuatan dokumen biasanya menggunakana pemrosesan template sebagai model utama untuk menghasilkan dokumen.

__Pembuatan kode sumber__
Alat pembuatan kode sumber mendukung pembuatan kode sumber dari model data abstrak untuk domain aplikasi tertentu, organisasi tertentu, atau dalam menyederhanakan proses prosuksi untuk komputer programmer.

__Fungsi perangkat lunak__
Sebuah web template engine memproses web template dan sumber data untuk menghasilkan satu atau lebih keluaran halaman web atau fragmen halaman.

### Keuntungan menggunakan template engine
- Mendorong organisasi kode sumber ke dalam lapisan yang berbeda secara operasional (misal : MVC)
- Meningkatkan produktivitas dengan mengurangi upaya reproduksi yang tidak perlu
- Meningkatkan kerja tim dengan memungkinkan pemisahan pekerjaan berdasarkan pada keahlian (misal : artistik vs teknis)

# Sistem Web Teplate

Sistem web template dalam penerbitan web memungkinkan perancang dan pengembang web bekerja dengan template web untuk secara otomatis menghasilkan halaman web khusus, seperti hasil dari pencarian. Ini menggunakan kembali elemen halaman web statis sambil mendefinisikan elemen dinamis berdasarkan parameter permintaan web. Sistem template web terdiri dari :
- Sebuah mesin template : elemen pengolahan primer dari sistem.
- Content resource : berbagai jenis aliran data input, seperti dari database relasional, file XML, direktori LDAP, dan jenis data lokal atau jaringan lainnya.
- STemplate resource : template web ditentukan sesuai dengan bahasa template.

Contoh :
Tampilan template 

    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml">
        <head><title>Sites</title></head>
        <body><h1 data-xp="title"><!-- placeholder --></h1></body>
    </html>

Untuk memasukkan komponen dari basis data :

    <?php
    $doc = new DOMDocument;
    $doc->preserveWhiteSpace = false;
    $doc->Load('view.html');
    $titlenode = $doc->createTextNode("Like this");
    $xpath = new DOMXPath($doc);
    $xpath->registerNamespace("h", "http://www.w3.org/1999/xhtml"); 
    $query = "//h:*[@data-xp='title']/comment()";
    $entries = $xpath->query($query);
    foreach ($entries as $entry) {
        $entry->parentNode->replaceChild($titlenode, $entry);
    }
    echo $doc->saveXML();
    ?>

### Jenis Sistem Template
- Server-side : penggantian run-time terjadi di web server.
- Client-side : substitusi run-time terjadi di browser web.
- Edge-side : substansi run-time terjadi pada proxy antara server web dan browser.
- Server luar : halaman web statis diproduksi secara offline dan diunggah ke server web. Tidak ada penggantian run-time.
- Didistribusikan : pengganian run-time menjadi beberapa server.

### Static site generators

![0303](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-03/readme1/Screenshot%20from%202020-03-25%2021-52-03.png)

Editor HTML sering menggunakan sistem templat web untuk hanya menghasilkan halaman web statis. Ini dapat dilihat sebagai desain web yang sudah jadi, digunakan untuk memproduksi secara massal situs web "cookie-cutter" untuk penyebaran cepat. 

![0303](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-03/readme1/Screenshot%20from%202020-03-25%2021-54-26.png)

### Server-side systems

![0303](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-03/readme1/Screenshot%20from%202020-03-25%2021-56-42.png)

Orang-orang mulai menggunakan halaman server-side dynamic yang dihasilkan dari template dengan perangkat lunak yang sudah ada yang disesuaikan untuk tugas ini. Perangkat lunak awal ini adalah preprosesor dan bahasa makro, diadaptasi untuk penggunaan web, berjalan pada CGI. Selanjutnya, teknologi sederhana namun relevan adalah eksekusi langsung yang dibuat pada modul ekstensi, dimulai dengan SSI.

Banyak sistem template biasanya digunakan sebagai sistem server-side template:

![0303](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-03/readme1/Screenshot%20from%202020-03-25%2021-57-23.png)

Secara teknis, metodologi menanamkan bahasa pemrograman ke dalam HTML (atau XML, dll.), Yang digunakan dalam banyak "bahasa skrip yang disertakan di sisi server" juga merupakan templat. Semuanya adalah bahasa kompleks Tertanam.

![0303](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-03/readme1/Screenshot%20from%202020-03-25%2021-58-32.png)

Ada juga preprosesor yang digunakan sebagai mesin templat sisi server. Contoh:

![0303](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-03/readme1/Screenshot%20from%202020-03-25%2021-58-40.png)

### Edge-side systems

"Edge-side" mengacu pada server web yang berada di ruang antara klien (browser) dan server asal. Mereka sering disebut sebagai server "reverse-proxy". Server-server ini umumnya bertugas mengurangi beban dan lalu lintas pada server asal dengan melakukan caching konten seperti gambar dan fragmen halaman, dan mengirimkannya ke browser secara efisien.

### Client-side systems

![0303](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-03/readme1/Screenshot%20from%202020-03-25%2021-58-55.png)

Banyak peramban web dapat menerapkan lembar gaya XSLT ke data XML yang mengubah data menjadi dokumen XHTML, sehingga menyediakan fungsionalitas templat di peramban itu sendiri.
Sistem lain menerapkan fungsionalitas templat di peramban menggunakan JavaScript atau bahasa skrip sisi klien lainnya, termasuk :
- Mustache
- Squirrelly
- Handlebars

### Distributed systems
Contoh :
- Ajax
- Rich Internet application

# Full Stack Python

Mesin template menerima string tokenized dan menghasilkan string yang diberikan dengan nilai menggantikan token sebagai output. Template biasanya digunakan sebagai format perantara yang ditulis oleh pengembang untuk menghasilkan satu atau lebih format output yang diinginkan secara terprogram, biasanya HTML, XML atau PDF.

Mesin template memungkinkan pengembang untuk menghasilkan jenis konten yang diinginkan, seperti HTML, sambil menggunakan beberapa data dan konstruksi pemrograman seperti kondisional dan loop untuk memanipulasi output. File templat yang dibuat oleh pengembang dan kemudian diproses oleh mesin templat terdiri dari markup prapenulisan dan blok tag templat tempat data dimasukkan.

Misalnya :

    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Matt Makai">
    <meta name="description" content="Template engines provide programmatic output of formatted content such as HTML, XML or PDF.">
    <link rel="shortcut icon" href="//static.fullstackpython.com/fsp-fav.png">

Base.html Jinja template yang digunakan untuk menghasilkan Full Stack Python memungkinkan setiap halaman di situs memiliki HTML yang konsisten tetapi secara dinamis menghasilkan bagian-bagian yang perlu diubah di antara halaman ketika generator situs statis dijalankan. Kode di bawah ini dari templat base.html menunjukkan bahwa deskripsi meta terserah pada template anak untuk dihasilkan.

    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Matt Makai">
    {% block meta_header %}{% endblock %}
    <link rel="shortcut icon" href="//static.fullstackpython.com/fsp-fav.png">

Implementasi mesin template akan jatuh di suatu tempat pada spektrum antara memungkinkan eksekusi kode arbitrer dan hanya memberikan seperangkat kemampuan terbatas melalui tag templat. Visual kasar kode dalam spektrum templat dapat dilihat di bawah ini untuk empat mesin templat Python utama.

![0303](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-03/readme1/Screenshot%20from%202020-03-25%2022-39-01.png)


# Jinja

Jinja2 adalah mesin template berfitur lengkap untuk Python. Ini memiliki dukungan unicode penuh, lingkungan eksekusi kotak pasir terintegrasi opsional, banyak digunakan dan berlisensi BSD.

    {% extends "layout.html" %}
    {% block body %}
    <ul>
    {% for user in users %}
        <li><a href="{{ user.url }}">{{ user.username }}</a></li>
    {% endfor %}
    </ul>
    {% endblock %}

jinja2 adalah salah satu mesin templat yang paling banyak digunakan untuk Python. Ini terinspirasi oleh sistem templating Django tetapi memperluasnya dengan bahasa ekspresif yang memberi para pembuat template seperangkat alat yang lebih kuat. Selain itu, ia menambahkan eksekusi kotak pasir dan pelolosan otomatis opsional untuk aplikasi di mana keamanan menjadi penting.

### Pengaturan Jinja

Jinja2 dikonfigurasi oleh Flask sebagai berikut:
- Autoescaping diaktifkan untuk semua templat yang berakhiran .html, .htm, .xml dan .xhtml saat menggunakan render_template ().
- Autoescaping diaktifkan untuk semua string saat menggunakan render_template_string ().
- Sebuah templat memiliki kemampuan untuk memilih masuk / keluar autoescaping dengan tag {% autoescape%}.
- Flask menyisipkan beberapa fungsi dan pembantu global ke dalam konteks Jinja2, selain nilai-nilai yang ada secara default.

### Filter Standar

__tojson__
Fungsi ini mengubah objek yang diberikn ke repreentasi json. Ini membantu menghasilkan JavaScript dengan cepat.

    <script type=text/javascript>
        doSomethingWith({{ user.username|tojson }});
    </script>

    It is also safe to use the output of |tojson in a single-quoted HTML attribute:

    <button onclick='doSomethingWith({{ user.username|tojson }})'>
        Click me
    </button>

Output dari __tojson__ dalam atribut HTML yang dikutip tunggal :

    <script type=text/javascript>
        doSomethingWith({{ user.username|tojson }});
    </script>

    It is also safe to use the output of |tojson in a single-quoted HTML attribute:

    <button onclick='doSomethingWith({{ user.username|tojson }})'>
        Click me
    </button>

### Mengontrol Autoescaping

Autoescaping adalah konsp melarikan diri dari karakter khusus. Karakter khusus dalam arti HTML adalah &, >, <, " dan '. Karakter - karakter ini membawa makna khusus dalam dokumen. Karakter tersebut harus digantikan dengan "entitas" jika ingin menggunakannya untuk teks.Namun terkadang harus menonaktifkan autoescaping di template pada saat menyuntikkan HTML secara eksplisit ke halaman, misalnya  sistem yang menghasilkan HTML aman seperti markdown ke HTML converter.

Untuk menonaktifkan sistem autoescaping dalam template :

    {% autoescape false %}
        <p>autoescaping is disabled here
        <p>{{ will_not_be_escaped }}
    {% endautoescape %}

### Mendaftarkan Filter

    @app.template_filter('reverse')
    def reverse_filter(s):
        return s[::-1]

    def reverse_filter(s):
        return s[::-1]
    app.jinja_env.filters['reverse'] = reverse_filter

Dalam hal dekorator argumennya adalah opsi jika ingin mengubah nama fungsi sebagai nama filter. Setelah terdaftar, dapat menggunakan filter dalam template dengan cara yang sama seperti filter jinja2. Misalnya jika terdapat daftar Python dalam konteks yang disebut mylist :

    {% for x in mylist | reverse %}
    {% endfor %}

### Pemrosesan konteks

Untuk menyuntikkan variabel baru secara otomatis ke dalam konteks templat, pemroses konteks ada di Flask. Prosesor konteks dijalankan sebelum template diberikan dan memiliki kemampuan untuk menyuntikkan nilai-nilai baru ke dalam konteks template. Pemroses konteks adalah fungsi yang mengembalikan kamus. Kunci dan nilai kamus ini kemudian digabungkan dengan konteks templat, untuk semua templat di aplikasi:

    @app.context_processor
    def inject_user():
        return dict(user=g.user)

Prosesor konteks di atas membuat variabel yang disebut pengguna tersedia dalam templat dengan nilai g.user. Contoh ini tidak terlalu menarik karena g tersedia dalam template, tetapi ini memberikan gambaran bagaimana ini bekerja.

Variabel tidak terbatas pada nilai; pemroses konteks juga dapat membuat fungsi tersedia untuk templat (karena Python mengizinkan fungsi yang dilewatkan) :

    @app.context_processor
    def utility_processor():
        def format_price(amount, currency=u'€'):
            return u'{0:.2f}{1}'.format(amount, currency)
        return dict(format_price=format_price)

Prosesor konteks di atas membuat fungsi format_price tersedia untuk semua template :

    {{ format_price(0.33) }}

# Dokumentasi Jinja

    <title>{% block title %}{% endblock %}</title>
    <ul>
    {% for user in users %}
    <li><a href="{{ user.url }}">{{ user.username }}</a></li>
    {% endfor %}
    </ul>

### Install
Install jinja2 menggunakan pip :

    pip install Jinja2

### Penggunaan API Dasar

Cara paling dasar untuk membuat template dan membuatnya melalui __Template__.

![0303](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-03/readme1/Screenshot%20from%202020-03-25%2023-56-12.png)

Dengan menggunakan instance __Template__, didapatkan kembali objrk template baru yang menyediakan metode yang disebut render() ketika dipanggil dengan argumen dict atau kata kunci memperluas template. Argumen dict atau kata kunci  yang diteruskan ke template disebut "konteks" dari template.

Cara paling sederhana untuk mengkonfigurasi jinja2 untuk membuat template untuk aplikasi :

    from jinja2 import Environment, PackageLoader, select_autoescape
    env = Environment(
        loader=PackageLoader('yourapplication', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

ini akanmembuat lingkungan template dengan pengaturan default dan loader yang mencari template di folder template didalam paket python aplikasi. Untuk memuat template di environment, maka hanya perlu memanggil metode get_template()  yang akan mengembalikan Template yang dimuat :

    template = env.get_template('mytemplate.html')

Untuk merendernya dengan beberapa variabel, cukup panggil metode render() :

    print(template.render(the='variables', go='here'))

### Unicode

Hal penting adalah bagaimana Jinja2 menangani string literal dalam template. Implementasi naif akan menggunakan string Unicode untuk semua string literal tetapi ternyata di masa lalu hal ini bermasalah karena beberapa perpustakaan mengetik pemeriksaan terhadap str secara eksplisit. Misalnya datetime.strftime tidak menerima argumen Unicode. Untuk tidak menghancurkannya sepenuhnya, Jinja2 mengembalikan str untuk string yang cocok dengan ASCII dan untuk semua yang lain unicode:

    >>> m = Template(u"{% set a, b = 'foo', 'föö' %}").module
    >>> m.a
    'foo'
    >>> m.b
    u'f\xf6\xf6'

### API Tingkat Tinggi

__undefined([hint, obj, name, exc])__
Membuat Undefined objek baru dari name. Ini berguna untuk filter atau fungsi yang dapat mengembalikan objek yang tidak ditentukan oleh beberapa operasi. Semua parameter kecuali hint harus disediakan sebagai parameter kata kunci untuk keterbacaan yang lebih baik. Hint digunakan sebagai pesan kesalahan untuk pengecualian jika disediakan, jika tidak pesan kesalahan akan dihasilkan dari objek dan name secata otomatis. 

Cara paling umum untuk membuat objek undefined adalah dengan memberi nama saja :

    return environment.undefined(name='some_name')

Ini berarti bahwa nama some_name tidak didefinisikan. Jika namanya berasal dari atribut suatu objek, masuk akal untuk memberi tahu objek yang tidak terdefinisi objek pemegang untuk meningkatkan pesan kesalahan :

    if not hasattr(obj, 'attr'):
        return environment.undefined(obj=obj, name='attr')
    
Untuk contoh yang lebih kompleks, dapat memberikan hint. Misalnya filter first() membuat objek tidak terdefinisi seperti itu :

    return environment.undefined('no first item, sequence was empty')

__compile_expression(source, undefined_to_none=True)__
Metode pembantu praktis yang mengembalikan callable yang menerima argumen kata kunci yang muncul sebagai variabel dalam ekspresi. Jika dipanggil itu mengembalikan hasil dari ekspresi. Ini berguna jika aplikasi ingin menggunakan aturan yang sama seperti Jinja dalam "file konfigurasi" template atau situasi serupa.

Contoh penggunaan :

    >>> env = Environment()
    >>> expr = env.compile_expression('foo == 42')
    >>> expr(foo=23)
    False
    >>> expr(foo=42)
    True

Per default, nilai pengembalian dikonversi ke None jika ekspresi mengembalikan nilai yang tidak ditentukan. Ini dapat diubah dengan mengatur undefined_to_none ke False.

    >>> env.compile_expression('var')() is None
    True
    >>> env.compile_expression('var', undefined_to_none=False)()
    Undefined

__class jinja2.Template__
Objek templat yang dibuat dari konstruktor dan bukan lingkungan yang memiliki atribut lingkungan yang menunjuk ke lingkungan sementara yang mungkin dibagi dengan templat lain yang dibuat dengan konstruktor dan pengaturan yang kompatibel.

    >>> template = Template('Hello {{ name }}!')
    >>> template.render(name='John Doe') == u'Hello John Doe!'
    True
    >>> stream = template.stream(name='John Doe')
    >>> next(stream) == u'Hello John Doe!'
    True
    >>> next(stream)
    Traceback (most recent call last):
        ...
    StopIteration

__render([context])__
Metode ini menerima argumen yang sama dengan konstruktor dict: Dict, subclass dict atau beberapa argumen kata kunci. Jika tidak ada argumen yang diberikan konteksnya akan kosong. Dua panggilan ini melakukan hal yang sama :

    template.render(knights='that say nih')
    template.render({'knights': 'that say nih'})