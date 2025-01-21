import array
#kita akan membahas array pada kesempatan kali ini 
'''
Array paling wajar dan mudah ditemui pada python adalah berbentuk list
namun penggunaan module array akan membuat lebih efisien dalam hal memory
'''
arr1 = array.array('i', [1, 2, 4, 7, 14, 56, 128])
print (arr1)
print (id(arr1[3]))
listy = [1, 2, 4, 7, 14, 56, 128,]
print (listy)
print(id(listy[2]))