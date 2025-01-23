#nested bisa juga dibilang sebagai matriks
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
print(A.T)

# Menjumlahkan matriks
B = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])
C = A + B
print(C)
