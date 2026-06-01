class PemberianMakan:
    def beri_makan(self, daftar_hewan):
        print("\n=== PEMBERIAN MAKAN ===")

        for hewan in daftar_hewan:
            hewan.makan()