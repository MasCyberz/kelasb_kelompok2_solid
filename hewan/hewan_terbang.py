# Analisis oleh:
# Nama : Ken Gayuh Nusa Islami
# NIM  : K3525031

# Analisis:

# Untuk memperbaikinya disini menggunakan Prinsip SOLID dari:
# Single Responsibility: Hanya untuk hewan terbang.
# Interface Segregation: Mengimplementasikan interface BisaTerbang, bukan menggabungkan di kelas induk.
# Liskov Substitution: HewanTerbang bisa menggantikan Hewan.
# Open Closed: Jika ada hewan terbang dengan perilaku khusus, buat subclass lagi.

from hewan.hewan import Hewan
from interfaces.interface1 import BisaTerbang

class HewanTerbang(Hewan, BisaTerbang):
    def __init__(self, nama, jenis):
        super().__init__(nama, jenis)

    def makan(self):
        print(f"{self.nama} (hewan terbang) sedang makan di udara.")

    def terbang(self):
        print(f"{self.nama} sedang terbang.")
        