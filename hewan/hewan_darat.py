# Analisis oleh:
# Nama : Ken Gayuh Nusa Islami
# NIM  : K3525031

# Analisis:

# Untuk memperbaikinya disini menggunakan Prinsip SOLID dari:
# Single Responsibility: Kelas ini khusus untuk hewan darat, tidak mencampur perilaku terbang.
# Liskov Substitution: HewanDarat bisa menggantikan Hewan tanpa merusak program.
# Open Closed: Jika butuh hewan darat dengan perilaku tambahan, buat subclass lagi.


from hewan.hewan import Hewan

class HewanDarat(Hewan):
    def __init__(self, nama, jenis):
        super().__init__(nama, jenis)

    def makan(self):
        print(f"{self.nama} (hewan darat) sedang makan di darat.")
