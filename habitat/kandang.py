# ==========================================
# TUGAS PRAKTIKUM PRINSIP SOLID
# Nama Kelompok : Kelompok 2 - Kelas B
# Nama Anggota  : Amelia Pinasti Nugraheni 
# NIM           : K3525049
# Bagian Kelas  : Habitat (kandang.py)
# ==========================================

class Kandang:
    def __init__(self, nama_kandang: str = "Kandang Utama"):
        self.nama_kandang = nama_kandang
        self.kapasitas = kapasitas
        self.kapasitas = 30 #diberi batas kapasitas agar bisa dikontrol jumlah hewannya
        self.hewan_list = [] 

    def tambah_hewan(self, hewan) -> bool:
        # [Memenuhi DIP & OCP] 
        # Dimana nanti program enerima objek 'hewan' secara umum lewat abstraksi.
        if len(self.hewan_list) < self.kapasitas:
            self.hewan_list.append(hewan)
            print(f"-> [INFO] {hewan.nama} berhasil dimasukkan ke {self.nama_kandang}.")
            return True 
        print(f"-> [PERINGATAN] {self.nama_kandang} sudah penuh! Gagal memasukkan {hewan.nama}.")
        return False

    def tampilkan_penghuni(self):
        # [Memenuhi SRP]
        # Tugasnya khusus hanya untuk mencetak/menampilkan daftar penghuni kandang.
        print(f"\n===== DAFTAR PENGHUNI {self.nama_kandang.upper()} =====")
        if not self.hewan_list:
            print("Kandang ini masih kosong.")
            return
        
        for index, hewan in enumerate(self.hewan_list, start=1):
            jenis_hewan = hewan.__class__.__name__
            print(f"{index}. {hewan.nama} ({jenis_hewan})")