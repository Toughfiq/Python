'''
Sebuah peternakan ayam memiliki sistem conveyor belt yang mengangkut telur untuk diperiksa. 
Sistem ini perlu memeriksa telur satu per satu sampai menemukan telur yang retak atau 
sampai semua telur sudah diperiksa.
Buatlah program yang:

Menerima list berisi kondisi telur (0 untuk telur bagus, 1 untuk telur retak)
Memeriksa telur satu per satu menggunakan for loop
Jika menemukan telur retak (1), program harus berhenti dan memberitahu posisi telur yang retak jika semua telur sudah diperiksa dan tidak ada yang retak, program memberitahu bahwa semua telur dalam kondisi baik
'''
telur = ["retak", "bagus", "bagus", "bagus", "retak", "bagus", "retak"]
statusTelur = []
posisiRetak = []
for b in telur:
    if b == "retak":
        statusTelur.append(1)
    else: 
        statusTelur.append(0)
    print(statusTelur)
if statusTelur == 1:
    print(f"Telur yang retak ditemukan pada posisi {posisiRetak}")
#==================================================================

#cara jika menggunakan enumerate
telur = ["retak", "bagus", "bagus", "bagus", "retak", "bagus", "retak"]
statusTelur = []

for index, b in enumerate(telur):
    if b == "retak":
        statusTelur.append(1)
    else:
        statusTelur.append(0)
        print(statusTelur)
        print(f"Telur yang retak ditemukan pada posisi {index + 1}")
