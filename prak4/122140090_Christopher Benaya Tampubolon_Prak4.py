class Hewan:
    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
    
    def bersuara(self):
        pass
    
    def makan(self):
        print(f"{self.nama} sedang makan: tulang")
    
    def minum(self):
        print(f"{self.nama} sedang minum: air")

class Kucing(Hewan):
    def bersuara(self):
        print(f"Kucing {self.nama} bersuara: meong")

class Anjing(Hewan):
    def bersuara(self):
        print(f"Anjing {self.nama} bersuara: guk-guk")

hewan1 = Kucing("Iccha", "Betina")
hewan2 = Anjing("Pher", "Jantan")

print(hewan1.nama)
print(hewan2.nama)

hewan1.bersuara()
hewan1.makan()
hewan2.bersuara()
hewan2.makan()
