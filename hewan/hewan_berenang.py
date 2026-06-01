# Analisis oleh:
# Nama : Ken Gayuh Nusa Islami
# NIM  : K3525031

# Analisis:

# Single Responsibility: Kelas ini khusus untuk hewan yang bisa berenang.
# Open Closed: Bisa menambah berbagai jenis hewan air tanpa mengubah kelas Hewan atau HewanDarat.
# Liskov Substitution: HewanBerenang dapat menggantikan Hewan tanpa merusak program.
# Interface Segregation: Implementasi interface BisaBerenang (dipisah dari terbang dan makan).
# Dependency Inversion: Bergantung pada abstraksi Hewan dan BisaBerenang.

from abc import ABC, abstractmethod
from hewan.hewan import Hewan
from interfaces.interface1 import BisaBerenang

class HewanBerenang(Hewan, BisaBerenang, ABC):
    def __init__(self, nama, jenis):
        super().__init__(nama, jenis)

    @abstractmethod
    def berenang(self):
        pass


class Ikan(HewanBerenang):
    def __init__(self, nama, jenis):
        super().__init__(nama, jenis)

    def berenang(self):
        print(f"{self.nama} sedang berenang dengan sirip.")


class UburUbur(HewanBerenang):
    def __init__(self, nama, jenis):
        super().__init__(nama, jenis)

    def berenang(self):
        print(f"{self.nama} sedang berenang.")
