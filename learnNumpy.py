#kita akan mencoba menggunakan numpy disini 
import numpy as np

# Membuat matriks 3x3
import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
#Print matriks A
print(f"ini adalah matriks A = \n", A)
# Akses elemen (baris ke-2, kolom ke-3)
print(f"elemen di indeks 1,2 = \n", A[1, 2])  # Output: 6
# Transpose matriks
print(f"Ini adalah hasi dari transpose matriks =\n", A.T)
# Menjumlahkan matriks
B = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])
print(f"ini adalah matriks B = \n", B)
C = A + B
print(f"ini adalah hasil penjumlahan matriks = \n", C)
'''
Beberapa operasi penting dalam NumPy:

A.shape → Mengetahui ukuran matriks (baris, kolom)
A.T → Transpos matriks
np.dot(A, B) → Perkalian matriks
np.linalg.inv(A) → Invers matriks (jika matriks persegi dan inversible)
np.linalg.det(A) → Determinan matriks

'''