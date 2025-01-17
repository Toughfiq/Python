name = input ("sebutkan nama :")
print(name)
try:
    nilai = int(input(f"{name}, masukkan nilai: "))
    print(nilai)
except ValueError:
    print("Input harus berupa angka!")