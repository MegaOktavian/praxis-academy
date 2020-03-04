class Prodi:
    def __init__(self, kodeProdi, namaProdi):
        self.kodeProdi = kodeProdi
        self.namaProdi = namaProdi
        print('(Initialized Prodi: {})'.format(self.kodeProdi))

    def tell(self):
        print('Kode Prodi : "{}" Nama Prodi : "{}"'.format(self.kodeProdi, self.namaProdi), end=" ")

class Mahasiswa(Prodi):
    def __init__(self, nim, nama, kodeProdi, namaProdi, angkatan):
        Prodi.__init__(self, kodeProdi, namaProdi)
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan
        print('(Initialized Mahasiswa: {})'.format(self.nim))

    def tell(self):
        Prodi.tell(self)
        print('Nim : "{}" Nama : "{}" Angkatan : "{}"'.format(self.nim, self.nama, self.angkatan), end=" ")

m = Mahasiswa(1182, 'Sistem Informasi', 1700016009, 'Mega Oktaviani Fadillah', 2017)

print()

anggota = [m]
for anggota in anggota:
    # Works for both Teachers and Students
    anggota.tell()