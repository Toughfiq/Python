# zfill()
'''
zfill berguna untuk menambahkan
nilai nol (0) di depan sebuah string dengan panjang tertentu
biasa digunakan untuk merapikan nomor sehingga memiliki format yang konsisten.
'''
new = "13"
tambahZ = new.zfill(5)
print(tambahZ)
# zfill hanya bisa menggunakan format data string, namun jika ingin menggunakan format int
#maka dapat dilihat pada pemberian contoh di bawah ini.
#contoh menggunakan looping pada zfill
i = 1
iLoop = str(i).zfill(3)

while i < 101:
    print(iLoop)
    i += 1
    iLoop = str(i).zfill(3)
#startwith()
'''
Metode startswith() 
bertujuan untuk menemukan suatu kata pada awal string. Metode ini mengembalikan nilai True
'''
#rjust()

#ljust()
#center() 