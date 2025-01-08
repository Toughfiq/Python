
'''
=========================TIPE DATA COLLECTION==================
'''

'''
Dalam python sama seperti R language yang dapat membuat list dengan berbagai macam tipe data 
primitif kedalam sebuah colection 
'''
'''
========================= List ==================================
'''
list_data = ['apple', 10, True, 'banana', 15.5]
print(list_data)
#akan mem-print isi dari var list_data

listBuah = ["apel", "pisang", "manggis", "durian", "nangka", "jeruk", "nanas", "buni", "mengkudu", "menteng", "bengkoang", "jambu Air", "jambu Biji"]
'''
adapun lagi metode slicing
slicing memiliki pola sebagai berikut :
sequence [start:stop:step]
start adalah index pertama yang anda ambil
stop adalah index terakhir yang diambil, stop bersifat adalah tidak di ikutsertakan ke dalam print item.
Step adalah jumlah elemen yang ingin anda lewati di antara setiap elemen slice.
by default nilai dari step adalah 1 
'''
print(listBuah[5:12])
# mencetak list tertentu dengan indexing
#ini akan membuat start point di index ke 5 dan dan bertakhir di index ke 11.
print(listBuah[::2])
#ini akan menghasilkan indexing dengan nilai lompat 2
#sementara step minus akan mengambil data dari belakang seperti ini
print(listBuah[::-1])
#ini akan mem print seberapa panjang list yang disertakan hasil yang di print akan menjadi 13
print(len(listBuah))
'''
========================== Tuple====================
'''
'''
Selain trdapat juga tuple yang menggunakan dengan "()" dan bersifat immutable sementara list dapat di append
untuk menambahkan item kedalam list
'''

tuple_data = ('apple', 10, True, 'banana', 15.5)

print(tuple_data)
#ini akan mem- print nilai darituple yang telah dibuat 

'''
========================= Dictionary====================
'''
dict_data = {'nama': 'John Doe', 'umur': 30, 'tinggi': 175, 'tinggi_cm': 1750}
'''

. Ada pula set yang menggunakan "{}" yang wajib diisi oleh item 
immutable, set ini tidak memilki indeks dan menggunakan sistem hash table. set ini dapat diisi dengan tuple.
set bersifat unique yang berarti tidak dapat diisi dengan value yang sama. sehingga set sangat cocok digunakan untuk cleansing data.

namun set tidak cocok untuk menciptakan matrik karena bersifat unordered.
untuk membuat matrik dapat digunakan list of list.

set dapat bersifat seperti himpunan di matematika sehingga dapat menggunakan method union atau intersection
untuk menggabungkan antar set.

'''
