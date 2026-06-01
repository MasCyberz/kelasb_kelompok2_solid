class KebunBinatang:
    def __init__(self, kandang):
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()

            if isinstance(hewan, BisaTerbang):
                hewan.terbang()
            if isinstance(hewan, BisaBerlari):
                hewan.berlari()
            if isinstance(hewan, BisaBerenang):
                hewan.berenang()