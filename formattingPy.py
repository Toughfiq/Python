# zfill()
'''
zfill berguna untuk menambahkan
nilai nol (0) di depan sebuah string dengan panjang tertentu
biasa digunakan untuk merapikan nomor sehingga memiliki format yang konsisten.
'''
new = "13"
tambahZ = new.zfill(5)
print(tambahZ)
# zfill ini tidak bisa menggunakan tipe data int

#contoh menggunakan looping pada zfill
i = 1
iLoop = str(i).zfill(3)

while i < 101:
    print(iLoop)
    i += 1
    iLoop = str(i).zfill(3)
#rjust()
#ljust()
#center() 