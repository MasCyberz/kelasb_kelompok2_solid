# Analisis oleh:
# Nama : Ken Gayuh Nusa Islami
# NIM  : K3525031

# Analisis:

# Untuk memperbaikinya disini menggunakan Prinsip SOLID dari:
# Single Responsibility: Kelas ini khusus untuk hewan darat, tidak mencampur perilaku terbang.
# Liskov Substitution: HewanDarat bisa menggantikan Hewan tanpa merusak program.
# Open Closed: Jika butuh hewan darat dengan perilaku tambahan, buat subclass lagi.


from hewan.hewan import Hewan
from interfaces.bisa_berjalan import BisaBerjalan
from interfaces.bisa_berenang import BisaBerenang

class Kucing(Hewan, BisaBerjalan):
    def makan(self):
        print(f"{self.nama} sedang makan wiskas")
    
    def berjalan(self):
        print(f"{self.nama} sedang berjalan")

class Pinguin(Hewan, BisaBerjalan, BisaBerenang):
    def makan(self):
        print(f"{self.nama} sedang makan ikan")
    
    def berjalan(self):
        print(f"{self.nama} sedang berjalan diatas es")
        
    def berenang(self):
        print(f"{self.nama} juga bisa berenang di air dingin")