# Analisis oleh:
# Nama : Ken Gayuh Nusa Islami
# NIM  : K3525031

# Analisis:

# Single Responsibility: Kelas ini khusus untuk hewan yang bisa berenang.
# Open Closed: Bisa menambah berbagai jenis hewan air tanpa mengubah kelas Hewan atau HewanDarat.
# Liskov Substitution: HewanBerenang dapat menggantikan Hewan tanpa merusak program.
# Interface Segregation: Implementasi interface BisaBerenang (dipisah dari terbang dan makan).
# Dependency Inversion: Bergantung pada abstraksi Hewan dan BisaBerenang.

from hewan.hewan import Hewan
from interfaces.bisa_berenang import BisaBerenang

class Ikan(Hewan, BisaBerenang):
    def makan(self):
        print(f"{self.nama} sedang makan")

    def berenang(self):
        print(f"{self.nama} sedang berenang dengan sirip.")


class UburUbur(Hewan, BisaBerenang):
    def makan(self):
        print(f"{self.nama} sedang makan")

    def berenang(self):
        print(f"{self.nama} sedang berenang.")
