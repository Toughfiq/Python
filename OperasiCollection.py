#len () -> akan menghitung banyaknya item dalam list, set maupun string.
#contoh penggunaan len() terdapat di file collectionData.py 

#min(), max() menghitung nilai minimum dan maksimum dari suatu list
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

#count berfungsi untuk menghitung berapa kali suatu objek muncul dalam list 
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))
string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))

#in dan not in diperuntukkan untuk mengetahui nilai atau objek yang ada dalam list
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

#multiple value assignment
#tahap ini akan sedikit mirip dengan mysql dan juga pembuatan matriks

data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)
#perlu diperhatikan pada line 27 harus dipastikan jumlah variable yang akan di assign berjumlah
#sama dengan isi dari pada isi list itu sendiri atau akan menjadi error

'''
jika ingin mengulang assign value maka dapat dilakukan sebagai berikut
'''
data = ['shirt', 'white', 'L', 'sweater', 'black', 'M']

apparel = data[::3]  # Indeks 0, 3 → ['shirt', 'sweater']
color = data[1::3]   # Indeks 1, 4 → ['white', 'black']
size = data[2::3]    # Indeks 2, 5 → ['L', 'M']

print(data)
print(apparel)  # Output: ['shirt', 'sweater']
print(color)    # Output: ['white', 'black']
print(size)     # Output: ['L', 'M']

#sorting pada python
