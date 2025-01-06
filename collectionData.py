
'''
tipe data collection
'''

'''
Dalam python sama seperti R language yang dapat membuat list dengan berbagai macam tipe data 
primitf kedalam sebuah colection 
'''

list_data = ['apple', 10, True, 'banana', 15.5]
print(list_data)
listBuah = ["apel", "pisang", "manggis", "durian", "nangka", "jeruk", "nanas", "buni", "mengkudu", "menteng", "bengkoang", "jambu Air", "jambu Biji"]
'''
adapun lagi metode slicing
slicing memiliki pola sebagai berikut :
sequence [start:stop:step]
start adalah index pertama yang anda ambil
stop adalah index terakhir yang diambil sementara step adalah
jumlah elemen yang ingin anda lewati di antara setiap elemen slice.
by default nilai dari slice adalah 1
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
Selain list terdapat juga tuple yang menggunakan dengan "()" dan bersifat immutable sementara list dapat di append
untuk menambahkan item kedalam list. Ada pula set yang menggunakan "{}" yang wajib diisi oleh item 
immutable, set ini tidak memilki indeks dan menggunakan sistem hash table. set ini dapat diisi dengan tuple.
namun set tidak cocok untuk menciptakan matrik karena bersifat unordered.
untuk membuat matrik dapat digunakan list of list.
set dapat bersifat seperti himpunan di matematika sehingga dapat menggunakan method union atau intersection
untuk menggabungkan antar set.

'''
