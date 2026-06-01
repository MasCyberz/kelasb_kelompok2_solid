# Analisis oleh:
# Nama : Ken Gayuh Nusa Islami
# NIM  : K3525031

# Analisis:

# Untuk memperbaikinya disini menggunakan Prinsip SOLID dari:
# Single Responsibility: Kelas ini hanya sebagai abstraksi dasar hewan, tidak berisi logika makan atau terbang.
# Open Closed: Dengan kelas abstrak, kita bisa membuat subclass baru tanpa mengubah kode ini.
# Liskov Substitution: Subclass harus bisa menggantikan Hewan, jadi tidak ada metode memaksa (seperti terbang).


from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama, jenis, umur):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur

    @abstractmethod
    def makan(self):
        pass
    