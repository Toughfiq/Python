import array, sys
#kita akan membahas array pada kesempatan kali ini 
'''
Array paling wajar dan mudah ditemui pada python adalah berbentuk list
namun penggunaan module array akan membuat lebih efisien dalam hal memory
'''
#ini adalah contoh array, array memerlukan import module terlebih dahulu
arr1 = array.array('i', [1, 2, 4, 7, 14, 56, 128])
print (arr1)
print (id(arr1[3]))
#ini contoh list
listy = [1, 2, 4, 7, 14, 56, 128,]
print (listy)
print(id(listy[2]))
#perbedeaan mendasar antara list dan juga array adalah penggunaan memory.
# dibawah ini adalah ukuran memory yang digunakan antara list dan juga array.
print(sys.getsizeof(listy))  # Lebih besar, ini adalahg list
print(sys.getsizeof(arr1)) # Lebih kecil, sementara ini adalah array.

var_array = [i for i in range(101)]
total = sum(var_array)
result = [total / len(var_array) ]
print (result)