#=========for loop========
buah = ["jambu", "buni", "tamarin", "menteng", "matoa"]
for b in buah:
    print(b)
    if buah.index(b) == len(buah) - 1:  # Cek apakah elemen terakhir sudah diproses
        print("List selesai")

"""
Penjelasan:
- 'buah.index(b) == len(buah) - 1' memastikan bahwa pesan "List selesai" hanya dicetak setelah elemen terakhir.
- Loop karakter ('for item in b') dihapus karena tidak diperlukan.
"""

#====== for loop dengan range ======
for i in range(5):
    print(i)
"""
Penjelasan:
- range(5) mengembalikan iterable sebanyak 5, yaitu [0, 1, 2, 3, 4].
- 'print(i)' mencetak nilai index secara berurutan.
"""

#while loop
i = 7
while i <=10:
  print(i)
  i += 7

#while loop dengan break
Num = 30
while Num < 30:
  print(Num)
  if Num % 2 = 0:
    break