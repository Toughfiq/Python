#membahas dasar OOP
mobil = "bergerak maju"
#mobil dapat di analogi kan sebagai class
#Sementara bergerak maju adalah method 

class Mobil:
    def __init__(self, warna, bergerak):
        # class mobil akan memiliki constructor init menerima 2 parameter
        self.warna = warna
        self.bergerak = bergerak #warna dan bergerak ini adalah instance    
suzuki = Mobil("Navy", "maju")

print(suzuki.warna)