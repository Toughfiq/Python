name = input ("sebutkan nama :")
print(name)
try:
    nilai = int(input(f"{name}, masukkan nilai: "))
    print(nilai)
except ValueError:
    print("Input harus berupa angka!")
if nilai >= 85:
    print("Nilai A,Hebat")
elif nilai >= 70:
    print("Nilai B,Tingkatkan lagi")
elif nilai>=60:
  print("Nilai C,Belajar lagi ya!")
elif nilai>=50:
  print("Nilai D,Jangan menyerah")
else:
    print("Nilai E,Goblok!")

    """
Anda diharTODO:
uskan membuat program diskon untuk sebuah toko belanja dengan ketentuan berikut.
- Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
- Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
- Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon, 
  dan simpan dalam variabel bernama "total_harga".

Tips:
- Ingat yang dicari adalah total harga belanja setelah diskon, bukan besaran potongan harga.
"""
# Jangan ubah kode ini
dico = 750000

# TODO: Silakan buat kode Anda di bawah ini
if dico >= 500000 :