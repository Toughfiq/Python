name = input ("sebutkan nama :")
print(name)
try:
    nilai = int(input(f"{name}, masukkan nilai: "))
    print(nilai)
except ValueError:
    print("Input harus berupa angka!")
nilai = 75
if nilai >= 85:
    print("Nilai A,Hebat")
elif nilai >= 70:
    print("Nilai B,Tingkatkan lagi")
elif nilai>=60
  print("Nilai C,Belajar lagi ya!")
elif nilai>=50
  print("Nilai D,Jangan menyerah")
else:
    print("Nilai E,Goblok!")