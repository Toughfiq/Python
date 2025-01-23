#kita akan mencoba menggunakan numpy disini 
import numpy as np

# Membuat matriks 3x3
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Akses elemen (baris ke-2, kolom ke-3)
print(A[1, 2])  # Output: 6

# Transpos matriks
print(f"ini adalah transpose matrikas", "\n", A.T)

# Menjumlahkan matriks
B = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])
C = A + B
print(C)
'''
Beberapa operasi penting dalam NumPy:

A.shape → Mengetahui ukuran matriks (baris, kolom)
A.T → Transpos matriks
np.dot(A, B) → Perkalian matriks
np.linalg.inv(A) → Invers matriks (jika matriks persegi dan inversible)
np.linalg.det(A) → Determinan matriks

'''