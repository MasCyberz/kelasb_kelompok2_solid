# habitat/kandang.py

class Kandang:
    def __init__(self, nama_kandang: str, kapasitas: int):
        self.nama_kandang = nama_kandang
        self.kapasitas = kapasitas
        self.daftar_hewan = []  # Menampung list objek hewan

    def tambah_hewan(self, hewan) -> bool:

        #[Memenuhi DIP & OCP] 
        #Menerima objek 'hewan' secara umum lewat abstraksi.Kandang 
        #tidak peduli jenis hewannya apa, selama ia adalah objek hewan.
        if len(self.daftar_hewan) < self.kapasitas:
            self.daftar_hewan.append(hewan)
            print(f"-> [INFO] {hewan.nama} berhasil dimasukkan ke {self.nama_kandang}.")
            return True
        print(f"-> [PERINGATAN] {self.nama_kandang} sudah penuh! Gagal memasukkan {hewan.nama}.")
        return False

    def tampilkan_penghuni(self):
    
        #[Memenuhi SRP]
        #Tugasnya khusus hanya untuk mencetak/menampilkan daftar penghuni kandang.
        print(f"\n===== DAFTAR PENGHUNI {self.nama_kandang.upper()} =====")
        if not self.daftar_hewan:
            print("Kandang ini masih kosong.")
            return
        
        for index, hewan in enumerate(self.daftar_hewan, start=1):
            # Mengambil nama class asli hewan (misal: Elang, Singa) secara dinamis
            jenis_hewan = hewan.__class__.__name__
            print(f"{index}. {hewan.nama} ({jenis_hewan})")