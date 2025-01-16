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


