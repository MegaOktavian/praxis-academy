from datetime import date
import time
import calendar

kalender = calendar.month(2020, 3)
tanggal = time.asctime( time.localtime(time.time()) )
sekarang = date.today()
waktu = time.time() 

print('\nBulan Maret : \n', kalender)
print('\nSekarang tanggal : \n', tanggal)
print('Tahun ini:', sekarang.year)
print('Bulan ini:', sekarang.month)
print('Tanggal hari ini:', sekarang.day)
print('Pukul : ', waktu)
