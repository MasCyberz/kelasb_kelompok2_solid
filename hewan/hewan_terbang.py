# Analisis oleh:
# Nama : Ken Gayuh Nusa Islami
# NIM  : K3525031

# Analisis:

# Untuk memperbaikinya disini menggunakan Prinsip SOLID dari:
# Single Responsibility: Setiap kelas hanya mewakili satu jenis hewan terbang.
# Open Closed: Bisa menambah jenis hewan terbang baru tanpa mengubah kelas induk.
# Liskov Substitution: Burung, Kelelawar, dll bisa menggantikan HewanTerbang.
# Interface Segregation: Mengimplementasikan BisaTerbang yang terpisah.
# Dependency Inversion: Bergantung pada abstraksi Hewan dan BisaTerbang.

from hewan.hewan import Hewan
from interfaces.bisa_terbang import BisaTerbang


class Burung(Hewan, BisaTerbang):
    def makan(self):
        print(f"{self.nama} sedang makan biji-bijian")

    def terbang(self):
        print(f"{self.nama} sedang terbang tinggi.")


class Kelelawar(Hewan, BisaTerbang):
    def makan(self):
        print(f"{self.nama} sedang makan buah-buahan")

    def terbang(self):
        print(f"{self.nama} sedang terbang")
