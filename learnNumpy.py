#kita akan mencoba menggunakan numpy disini 
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
# line 23 bisa disebut juga dengan operasi otomatis/broadcasting
'''
Beberapa operasi penting dalam NumPy:

A.shape → Mengetahui ukuran matriks (baris, kolom)
A.T → Transpos matriks
np.dot(A, B) → Perkalian matriks
np.linalg.inv(A) → Invers matriks (jika matriks persegi dan inversible)
np.linalg.det(A) → Determinan matriks

'''
#mengetahui ukuran dari matriks
print(f"ini adalah ukuran dari matriks \n", "A = ", A.shape, "\n B = ", B.shape) 
#melakukan perkalian matriks
matriksDot = np.dot(A, B)
print(f"ini adalah hasil perkalian matriks 3D = \n", matriksDot)

# Perkalian elemen-per-elemen
print(f"ini adalah hasil perkailan matriks A dan B = \n", A * B)

# Pembagian elemen-per-elemen
print(f"ini adalah hasil pembagian matriks A dan B = \n", B / A)

#menggabungkan matriks
# Gabungan horizontal
print(f"Ini adalah gabungan horizontal dari matriks A dan B = \n", np.hstack((A, B)))

# Gabungan vertikal
print(f"Ini adalah hasil gabungan vertikal dari matriks A dan B = \n", np.vstack((A, B)))

#invers matriks
#inv_A = np.linalg.inv(A)
#print(f"ini adalah hasil invers matriks A = \n", inv_A)
#eigenvalues dan eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
#eigenvectors akan digunakan untuk mereduksi dimensi, dan juga analisis matriks bobot untuk memahami bagaimana informasi diolah/diproses
#normalisasi data di normalisasi
data = np.array([[50, 60], [80, 90], [100, 110]])
normalized_data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)
print(normalized_data)