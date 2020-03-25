# WSGI (Web Server Gateway Interface)

    Web Server Gateway Interface adalah konvensi pemanggilan sederhana untuk web server meneruskan permintaah untuk aplikasi web atau framework yang digutiskan menggunakan bahasa pemrograman python.

### Spesifikasi

WSGI mempunyai dua sisi :
1. Server/gateway : merupakan web server lengkap seperti Apache dan Nginx, atau server aplikasi ringan yang dapat berkomunikasi dengan server web seperti flup.
2. Aplikasi/framework : ini adalah panggilan python, yang disediakan oleh program atau kerangka kerja python.

###  WSGI Middleware

    Komponen WSGI Middleware adalah panggilan python yang merupakan aplikasi WSGI sendiri, tetapi dapat menangani permintaan dengan mendelegasikan ke aplikasi WSFI lainnya.

Komponen middleware dapat melakukan fungsi - fungsi seperti :
1. Merutekan permintaan ke objek aplikasi yang berbeda berdasarkan URL target, setelang mengubah variabel lingkungan yang sesuai.
2. Mengizinkan beberapa aplikasi atau kerangka kerja yang berjalan berdampingan dalam proses yang sama.
3. Load balencing dan pemrosesan jarak jauh, dengan meneruskan permintaan dan menanggapinya melalui jaringan.
4. Melakukan post-processing konten, seperti mererapkan stylesheet XSLT.

### Contoh
__Aplikasi yang ditulis menggunakan python :__

    def application(environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/plain')])
        yield b'Hello, World\n'

__Memanggil aplikasi :__

    from io import BytesIO

    def call_application(app, environ):
        status = None
        headers = None
        body = BytesIO()
        
        def start_response(rstatus, rheaders):
            nonlocal status, headers
            status, headers = rstatus, rheaders
            
        app_iter = app(environ, start_response)
        try:
            for data in app_iter:
                assert status is not None and headers is not None, \
                    "start_response() was not called"
                body.write(data)
        finally:
            if hasattr(app_iter, 'close'):
                app_iter.close()
        return status, headers, body.getvalue()

    environ = {...}  # "environ" dict
    status, headers, body = call_application(app, environ)

Framework yang berjalan di WSGI : appier, bobo, Bottle, CherryPy, Django, Falcon, Flask, notmm, PoorWSGI, Pycnic, Pyramid, QWeb, repoze.zepo2, TuberGears, web.py, web2py, WebCore, Webplayer dan Zope3.

__Contoh 1:__
Contoh berikut adalah operator yang diberikan ekspresi leguler dan aplikasi yang cocok. Itu memereiksa setiap ekspresi reguler pada gilirannya, dan cocok itu memindahkan kelompok yang disebutkan kedalam __wsgiorg.routing_args__ dan mengirim ke aplikasi terkait :

    class RegexDispatch(object):
        def __init__(self, patterns):
            self.patterns = patterns

        def __call__(self, environ, start_response):
            script_name = environ.get('SCRIPT_NAME', '')
            path_info = environ.get('PATH_INFO', '')
            for regex, application in self.patterns:
                match = regex.match(path_info)
                if not match:
                    continue
                extra_path_info = path_info[match.end():]
                if extra_path_info and not extra_path_info.startswith('/'):
                    # Not a very good match
                    continue
                pos_args = match.groups()
                named_args = match.groupdict()
                cur_pos, cur_named = environ.get('wsgiorg.routing_args', ((), {}))
                new_pos = list(cur_pos) + list(pos_args)
                new_named = cur_named.copy()
                new_named.update(named_args)
                environ['wsgiorg.routing_args'] = (new_pos, new_named)
                environ['SCRIPT_NAME'] = script_name + path_info[:match.end()]
                environ['PATH_INFO'] = extra_path_info
                return application(environ, start_response)
            return self.not_found(environ, start_response)

        def not_found(self, environ, start_response):
            start_response('404 Not Found', [('Content-type', 'text/plain')])
            return ['Not found']

    dispatch_app = RegexDispatch([
        (re.compile(r'/archive/(?P<year>\d{4})/$'), archive_app),
        (re.compile(r'/archive/(?P<year>\d{4})/(?P<month>\d{2})/$'),
        archive_app),
        (re.compile(r'/archive/(?P<year>\d{4})/(?P<month>\d{2})/(?P<article_id>\d+)$'),
        view_article),
    ])

__Contoh 2:__
Penggunaan __pycurl.CurlMulti__ untuk melakukan permintaan HTTP keluar dengan cara ang tidak menghalangi. Ketika metode __CurlMulti.perform()__ mendeteksi bahwa operasi I/O berikutnya akan diblokir, ia mengembalikannya ke kontrol aplikasi yang kemudian menghasilkan sampai deskriptor file yang menarik menjadi dapat dibaca atau ditulis sesuai kebutuhan. Jika deskriptor tidak siap setelah satu detik, aplikasi mengirimkan respons kepada klie dan berakhir __504 Gateway Timeout__ :

    def pyorg_proxy(environ, start_response):
        result = StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, 'http://python.org' + environ['PATH_INFO'])
        c.setopt(pycurl.WRITEFUNCTION, result.write)

        m = pycurl.CurlMulti()
        m.add_handle(c)

        while True:
            while True:
                ret, num_handles = m.perform()
                if ret != pycurl.E_CALL_MULTI_PERFORM:
                    break
            if not num_handles:
                break

            read, write, exc = m.fdset()
            if read:
                yield environ['x-wsgiorg.fdevent.readable'](read[0], 1.0)
            else:
                yield environ['x-wsgiorg.fdevent.writable'](write[0], 1.0)

            if environ['x-wsgiorg.fdevent.timeout']:
                msg = 'The request to python.org timed out.'
                start_response('504 Gateway Timeout',
                            [('Content-Type', 'text/plain'),
                                ('Content-Length', str(len(msg)))])
                yield msg
                return

        start_response('200 OK', [('Content-Type', 'application/octet-stream'),
                                ('Content-Length', str(result.len))])
        yield result.getvalue()

Adaptor berikut memungkinkan aplikasi yang menggunakan ekstensi __x-wsgiorg.fdevent__ utnuk berjalan di server yang tidak mendukungnya, tanpa memodifikasi kode aplikasi :

    def with_fdevent(application):
        def wrapper(environ, start_response):
            select_args = [None]

            def readable(fd, timeout=None):
                assert (not select_args[0])
                select_args[0] = ([fd], [], [fd], timeout)
                return ''

            def writable(fd, timeout=None):
                assert (not select_args[0])
                select_args[0] = ([], [fd], [fd], timeout)
                return ''

            environ['x-wsgiorg.fdevent.readable'] = readable
            environ['x-wsgiorg.fdevent.writable'] = writable

            timeout = False

            class TimeoutWrapper(object):
                def __nonzero__(self):
                    return timeout

            environ['x-wsgiorg.fdevent.timeout'] = TimeoutWrapper()

            for result in application(environ, start_response):
                assert (not (result and select_args[0]))
                if result or (not select_args[0]):
                    yield result
                else:
                    ready = select.select(*select_args[0])
                    timeout = (ready == ([], [], []))
                    select_args[0] = None

        return wrapper

__Contoh 3:__
Ini adalahcather pengecualaian sederhana yang menggunakan kunci :

import sys, traceback

    class CatchExceptions(object):
        def __init__(self, app):
            self.app = app
        def __call__(self, environ, start_response):
            if not environ.get('x-wsgiorg.developer_user'):
                return self.app(environ, start_response)
            try:
                return self.app(environ, start_response)
            except:
                start_response('500 Server Error', [('content-type', 'text/plain')],
                            sys.exc_info())
                return [traceback.format_exc()]

Berikut ini adalah middeleware ip-address yang menetapkan kunci :

    class IPDeveloper(object):
        def __init__(self, app, ips=('127.0.0.1',)):
            self.app = app
            self.ips = ips
        def __call__(self, environ, start_response):
            if environ.get('REMOTE_ADDR') in self.ips:
                environ['x-wsgiorg.developer_user'] = environ['REMOTE_ADDR']
            return self.app(environ, start_response)

__Contoh 4:__
Transformasi output memparsing halaman dengan llxml.etree.HTML (dari perpustakaan lxml) dan mengganti semua tag <i> dengan tag <em>. Middleware :

    import lxml.etree

    class EmTagMiddleware(object):
        def __init__(self, app):
            self.app = app
        def __call__(self, environ, start_response):
            parent_wants_parsed = environ.get('x-wsgiorg.want_parsed_response')
            environ['x-wsgiorg.want_parsed_response'] = True
            written_output = []
            captured_headers = []
            def repl_start_response(status, headers, exc_info=None):
                if exc_info:
                    raise exc_info[0], exc_info[1], exc_info[2]
                captured_headers[:] = [status, headers]
                return written_output.append
            app_iter = self.app(environ, repl_start_response)
            parsed = None
            if captured_headers and not written_output:
                method = getattr(app_iter, 'x_wsgiorg_parsed_response', None)
                if method:
                    parsed = method(lxml.etree._Element)
            if parsed is None:
                # Have to manually parse, because:
                #  a) start_response was called lazily
                #  b) the start_response writer was used
                #  c) app_iter.x_wsgiorg_parsed_response didn't exist
                #  d) that method returned None
                try:
                    for item in app_iter:
                        written_output.append(item)
                finally:
                    if hasattr(app_iter, 'close'):
                        app_iter.close()
                parsed = self.parse_body(''.join(written_output))
            status, headers = captured_headers
            new_body = self.transform_body(parsed)
            for i in range(len(headers)):
                if headers[i][0].lower() == 'content-length':
                    del headers[i]
                    break
            if parent_wants_parsed:
                new_app_iter = self.make_app_iter(new_body)
            else:
                serialized_body = serialize(new_body)
                headers.append(('Content-Length', str(len(serialized_body))))
                new_app_iter = [serialized_body]
            return new_app_iter

        def parse_body(self, body):
            return lxml.etree.HTML(body)

        def transform_body(self, root):
            for el in root.xpath('//i'):
                el.tag = 'em'
            return root

        def make_app_iter(self, body):
            return LazyLXML(body)

    def serialize(element):
        return lxml.etree.tostring(element)

    class LazyLXML(object):
        def __init__(self, body):
            self.body = body
            self.have_yielded = False
        def __iter__(self):
            return self
        def next(self):
            if self.have_yielded:
                raise StopIteration
            self.have_yielded = True
            return serialize(self.body)
        def x_wsgiorg_parsed_response(self, type):
            if type is lxml.etree._Element:
                return self.body
            return None

Contoh sederhana memparsing input form normal wsgi.input :

    import cgi
    import urllib
    from cStringIO import StringIO

    def parse_form(environ):
        content_type = environ.get('CONTENT_TYPE', '')
        assert content_type in ['application/x-www-form-urlencoded', 'multipart/form-data']
        wsgi_input = environ['wsgi.input']
        method = getattr(wsgi_input, 'x_wsgiorg_parsed_response', None)
        if method:
            parsed = method(cgi.FieldStorage)
            if parsed is not None:
                return parsed
        form = cgi.FieldStorage(fp=wsgi_input, environ=environ, keep_blank_values=True)
        environ['wsgi.input'] = FakeFormInput(form)
        return form

    class FakeFormInput(object):
        def __init__(self, form):
            self.form = form
            self.serialized = None
        def x_wsgiorg_parsed_response(self, type):
            if type is cgi.FieldStorage:
                return self.form
            return None
        def read(self):
            if self.serialized is None:
                self._serialize()
            return self.serialized.read()
        def readline(self, *args):
            if self.serialized is None:
                self._serialize()
            return self.serialized.readline(*args)
        def readlines(self, *args):
            if self.serialized is None:
                self._serialize()
            return self.serialized.readlines(*args)
        def __iter__(self):
            if self.serialized is None:
                self._serialize()
            return iter(self.serialized)
        def _serialize(self):
            # XXX: Doesn't deal with file uploads, and multipart/form-data generally
            data = urllib.urlencode(self.form.list, True)
            self.serialized = StringIO(data)

__Contoh 5:__
Pengaplikasian otentikasi HTTP sederhana :

    class HTTPBasic(object):
        def __init__(self, app, user_database, realm='Website'):
            self.app = app
            self.user_database = user_database
            self.realm = realm

        def __call__(self, environ, start_response):
            def repl_start_response(status, headers, exc_info=None):
                if status.startswith('401'):
                    remove_header(headers, 'WWW-Authenticate')
                    headers.append(('WWW-Authenticate', 'Basic realm="%s"' % self.realm))
                return start_response(status, headers)
            auth = environ.get('HTTP_AUTHORIZATION')
            if auth:
                scheme, data = auth.split(None, 1)
                assert scheme.lower() == 'basic'
                username, password = data.decode('base64').split(':', 1)
                if self.user_database.get(username) != password:
                    return self.bad_auth(environ, start_response)
                environ['REMOTE_USER'] = username
                del environ['HTTP_AUTHORIZATION']
            return self.app(environ, repl_start_response)

        def bad_auth(self, environ, start_response):
            body = 'Please authenticate'
            headers = [
                ('content-type', 'text/plain'),
                ('content-length', str(len(body))),
                ('WWW-Authenticate', 'Basic realm="%s"' % self.realm)]
            start_response('401 Unauthorized', headers)
            return [body]

    def remove_header(headers, name):
        for header in headers:
            if header[0].lower() == name.lower():
                headers.remove(header)
                break

__Contoh 6:__
Penangkapan cather sederhana :

    class ExceptionCatch(object):
        def __init__(self, app):
            self.app = app
        def __call__(self, environ, start_response):
            if environ.get('x-wsgiorg.throw_errors'):
                return self.app(environ, start_response)
            try:
                return self.app(environ, start_response)
            except:
                import sys, traceback, StringIO
                exc_info = sys.exc_info()
                start_response('500 Server Error', [('content-type', 'text/plain')],
                            exc_info=exc_info)
                out = StringIO.StringIO()
                traceback.print_exc(file=out)
                return [out.getvalue()]

__Contoh 7:__
Gateway CGI sederhana yang mengimplementasikan fungsi :

    import os
    import sys

    def run_with_cgi(app, charset=None):
        environ = dict(os.environ.items())
        environ['wsgi.charset'] = charset
        environ['wsgi.input'] = sys.stdin
        environ['wsgi.errors']  = sys.stderr
        environ['wsgi.version'] = (1,0)
        environ['wsgi.multithread'] = False
        environ['wsgi.multiprocess'] = True
        environ['wsgi.run_once'] = True

        if environ.get('HTTPS','off').lower() in ('on','1'):
            environ['wsgi.url_scheme'] = 'https'
        else:
            environ['wsgi.url_scheme'] = 'http'

        headers_set = []
        headers_sent = []

        def write(data):
            if not headers_set:
                raise AssertionError('write() before start_response()')
            elif not headers_sent:
                status, response_headers = headers_sent[:] = headers_set
                sys.stdout.write('Status: %s\r\n' % status)
                for header in response_headers:
                    sys.stdout.write('%s: %s\r\n' % header)
                sys.stdout.write('\r\n')
            if isinstance(data, unicode):
                charset = environ['wsgi.charset']
                if charset is None:
                    raise AssertionError('application returned unicode without '
                                        'defined charset')
                data = data.encode(charset)
            sys.stdout.write(data)
            sys.stdout.flush()

        def start_response(status,response_headers,exc_info=None):
            if exc_info:
                try:
                    if headers_sent:
                        raise exc_info[0], exc_info[1], exc_info[2]
                finally:
                    exc_info = None
            elif headers_set:
                raise AssertionError('Headers already set!')
            headers_set[:] = [status,response_headers]
            return write

        result = app(environ, start_response)
        try:
            for data in result:
                if data:
                    write(data)
            if not headers_sent:
                write('')
        finally:
            if hasattr(result,'close'):
                result.close()

# Microframework

    Microframework adalah stilah yang digunakan untuk merujuk kepada  minimalis kerangka kerja aplikasi web.

Fungsional umum :
1. Akun, otentikasi, otoritas dan peran.
2. Abstaksi basis data melalui pemetaan object-relation.
3. Validasi input dan input sanitasi.
4. Web template engine.

__Contoh Pseudocode__

    require "foo.php";

    foo::get("/hello/{name}", function($name) {
        return "Hello $name!";
    });

# Flask

    Flask adalah kerangka kerja aplikasi web WSGI yang  ringan.

Flask menawarkan saran, tetapi tidak memberlakukan dependensi atau tata letak proyek. Terserah pengembang untuk memilih alat dan perpustakaan yang ingin mereka gunakan. Ada banyak ekstensi yang disediakan oleh komunitas yang membuat penambahan fungsionalitas baru menjadi mudah.

    from flask import Flask, escape, request

    app = Flask(__name__)

    @app.route('/')
    def hello():
        name = request.args.get("name", "World")
        return f'Hello, {escape(name)}!

### Komponen

__Werkzeug__
Werkzeug adalah perpustakaan utilitas untuk bahasa pemrograman Python, dengan kata lain toolkit untuk aplikasi Web Server Gateway Interface (WSGI), dan dilisensikan di bawah Lisensi BSD. Werkzeug dapat mewujudkan objek perangkat lunak untuk fungsi permintaan, respons, dan utilitas.

__Jinja__
Jinja adalah template engine untuk bahasa pemrograman Python dan dilisensikan di bawah Lisensi BSD. Mirip dengan kerangka kerja Django, ia menangani template di sandbox.

# Install Flask

1. Membuat environment :

    mkdir myproject
    
    cd myproject
    
    python3 -m venv venv

   ![0302](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-02/readme/Screenshot%20from%202020-03-18%2019-04-06.png)

2. Mengaktifkan environment :
   
    . venv/bin/activate

   ![0302](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-02/readme/Screenshot%20from%202020-03-18%2019-04-29.png)

3. Menghidupkan edge :

    pip install -U https://github.com/pallets/flask/archive/master.tar.gz

   ![0302](https://github.com/MegaOktavian/rhymes/blob/master/gambar%20naive/03-02/readme/Screenshot%20from%202020-03-18%2019-05-04.png)

# Konfigurasi

Konfigurasi adalah sub kelas dari kamus dan dapat dimodifikasi sama seperti kamus lainyya :

    app = Flask(__name__)
    app.config['TESTING'] = True

Nilai konfiguras tertentu juga diteruskan ke objek Flask sehingga :

    app.testing = True

Untuk memperbaharui beberapa kunci sekaligus maka dapat menggunakan __dict.update()__ :

    app.config.update(
        TESTING=True,
        SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
    )

### Environment dan Debug Features

Nilai konfigurasi ENV dan DEBUG adalah khusus karena mereka mungkin berperilaku tidak konsisten jika diubah setelah aplikasi mulai diatur. Untuk mengatur mode lingkungan dan debug dengan handal, Flask menggunakan environment features.

Lingkungan digunakan untuk menunjukkan ke Flask, ekstensi, dan program lain, seperti Sentry, dalam konteks apa Flask berjalan. Ia dikendalikan dengan variabel lingkungan FLASK_ENV dan default untuk produksi.

Mengatur FLASK_ENV ke pengembangan akan mengaktifkan mode debug. flask akan berjalan menggunakan debugger dan reloader interaktif secara default dalam mode debug. Untuk mengontrol ini secara terpisah dari lingkungan, gunakan FLASK_DEBUG.

    export FLASK_ENV=development
    flask run

### Konfigurasi dari File

Konfigurasi menjadi lebih berguna jika dapat menyimpannya dalam file terpisah, idealnya terletak di luar paket aplikasi yang sebenarnya. Ini memungkinkan pengemasan dan pendistribusian aplikasi melalui berbagai alat penanganan paket dan akhirnya memodifikasi file konfigurasi sesudahnya.
Pola yang umum adalah:

    app = Flask(__name__)
    app.config.from_object('yourapplication.default_settings')
    app.config.from_envvar('YOURAPPLICATION_SETTINGS')

Pertama memuat konfigurasi dari modul yourapplication.default_settings dan kemudian menimpa nilai-nilai dengan isi file yang variabel lingkungan mengarah ke YOURAPPLICATION_SETTINGS. Variabel lingkungan ini dapat diatur di Linux atau OS X dengan perintah ekspor di shell sebelum memulai server :

    export YOURAPPLICATION_SETTINGS=/path/to/settings.cfg
    python run-app.py

File konfigurasi itu sendiri adalah file Python yang sebenarnya. Hanya nilai dalam huruf besar yang benar-benar disimpan di objek config nanti. Jadi pastikan untuk menggunakan huruf besar untuk kunci konfigurasi.
Berikut adalah contoh file konfigurasi:

    # Example configuration
    DEBUG = False
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'

### Konfigurasi dari Environment Variables

Selain menunjuk ke file konfigurasi menggunakan variabel lingkungan, Anda mungkin merasa berguna (atau perlu) untuk mengontrol nilai konfigurasi Anda langsung dari lingkungan.

Variabel lingkungan dapat diatur di Linux atau OS X dengan perintah ekspor di shell sebelum memulai server :

    export SECRET_KEY='5f352379324c22463451387a0aec5d2f'
    export MAIL_ENABLED=false
    python run-app.py

Meskipun pendekatan ini mudah digunakan, penting untuk diingat bahwa variabel lingkungan adalah string - mereka tidak secara otomatis dideeralisasi menjadi tipe Python.

Berikut adalah contoh file konfigurasi yang menggunakan variabel lingkungan :

    import os

    _mail_enabled = os.environ.get("MAIL_ENABLED", default="true")
    MAIL_ENABLED = _mail_enabled.lower() in {"1", "t", "true"}

    SECRET_KEY = os.environ.get("SECRET_KEY")

    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application")
    
   Verifikasi bahwa tabel dan baris telah dibuat :

    cockroach sql --insecure --database=bank

    SELECT COUNT(*) FROM accounts;

### Folder Instance

Anda dapat secara eksplisit menyediakan path folder instance ketika membuat aplikasi Flask atau Anda dapat membiarkan Flask secara otomatis mendeteksi folder instance. Untuk konfigurasi eksplisit gunakan parameter instance_path :

    app = Flask(__name__, instance_path='/path/to/instance/folder')

Harap diingat bahwa jalur ini harus mutlak saat disediakan.

Jika parameter instance_path tidak disediakan, lokasi default berikut digunakan:

     Uninstalled module:

    /myapp.py
    /instance

Uninstalled package:

    /myapp
        /__init__.py
    /instance

Install module atau package :

    PREFIX/lib/python2.X/site-packages/myapp
    PREFIX/var/myapp-instance

Karena objek config menyediakan pemuatan file konfigurasi dari nama file relatif, kami memungkinkan untuk mengubah pemuatan melalui nama file menjadi relatif ke jalur instance jika diinginkan. Perilaku jalur relatif dalam file konfigurasi dapat dibalik antara "relatif ke root aplikasi" (default) ke "relatif ke instance folder" melalui switch instance_relative_config ke konstruktor aplikasi :

    app = Flask(__name__, instance_relative_config=True)

Berikut ini adalah contoh lengkap tentang cara mengkonfigurasi Flask untuk preload konfigurasi dari modul dan kemudian menimpa konfigurasi dari file dalam folder instance jika ada :

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('yourapplication.default_settings')
    app.config.from_pyfile('application.cfg', silent=True)

Path ke folder instance dapat ditemukan melalui Flask.instance_path. Flask juga menyediakan jalan pintas untuk membuka file dari folder instance dengan Flask.open_instance_resource ().

Contoh penggunaan untuk keduanya:

    filename = os.path.join(app.instance_path, 'application.cfg')
    with open(filename) as f:
        config = f.read()

    # or via open_instance_resource:
    with app.open_instance_resource('application.cfg') as f:
        config = f.read()