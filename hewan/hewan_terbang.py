# Analisis oleh:
# Nama : Ken Gayuh Nusa Islami
# NIM  : K3525031

# Analisis:

# Untuk memperbaikinya disini menggunakan Prinsip SOLID dari:
# Single Responsibility: Setiap kelas hanya mewakili satu jenis hewan terbang.
# Open Closed: Bisa menambah jenis hewan terbang baru tanpa mengubah kelas induk.
# Liskov Substitution: Elang, Kelelawar, dll bisa menggantikan HewanTerbang.
# Interface Segregation: Mengimplementasikan BisaTerbang yang terpisah.
# Dependency Inversion: Bergantung pada abstraksi Hewan dan BisaTerbang.


from abc import ABC, abstractmethod
from hewan.hewan import Hewan
from interfaces.interface1 import BisaTerbang

class HewanTerbang(Hewan, BisaTerbang, ABC):
    def __init__(self, nama, jenis):
        super().__init__(nama, jenis)

    @abstractmethod
    def terbang(self):
        pass


class Elang(HewanTerbang):
    def __init__(self, nama, jenis):
        super().__init__(nama, jenis)

    def terbang(self):
        print(f"{self.nama} sedang terbang tinggi.")


class Kelelawar(HewanTerbang):
    def __init__(self, nama, jenis):
        super().__init__(nama, jenis)

    def terbang(self):
        print(f"{self.nama} sedang terbang.")
