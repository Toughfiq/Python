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

Startwith() sendiri digunakan untuk validasi data atau filtering dan pengolahan string itu sendiri
berikut adalah beberapa contoh penggunaan startswith()
'''
#mencari/memvalidasi format data
nomor_hp = "08123456789"
if nomor_hp.startswith("08"):
    print("Nomor Indonesia")
#dapat juga digunakan untuk memfilter string dengan awalan tertentu
kata = ["Python", "Java", "Ruby", "Rust"]
hasil = [k for k in kata if k.startswith("R")]
print(hasil)  # Output: ['Ruby', 'Rust']
#startwith() juga dapat digunakan untuk mengecek url
url = "https://www.example.com"
if url.startswith("https://"):
    print("URL aman")
#Parsing file atau log
log = "[ERROR] File not found"
if log.startswith("[ERROR]"):
    print("Ada kesalahan!")

#namun startwith memiliki keterbatasan dalam mencari pada list,tuple atau set, namun dapat digunakan any()
kata_tuple = ("Ruby", "Rust", "Racket")
hasil = any(kata.startswith("Ru") for kata in kata_tuple)
print(hasil)  # Output: True

#rjust()
#ljust()
#center() 
'''
ketiga format diatas akan merapihkan  pencetakan teks 
r untuk rata kanan, l untuk rata kiri dan center untuk rata tengah.

'''