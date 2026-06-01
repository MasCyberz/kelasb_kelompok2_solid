class KebunBinatang:

    def __init__(self, kandang, pemberian_makan, perawatan):
        self.kandang = kandang
        self.pemberian_makan = pemberian_makan
        self.perawatan = perawatan

    def operasional_harian(self):
        self.pemberian_makan.beri_makan(
            self.kandang.hewan_list
        )

        self.perawatan.rawat(
            self.kandang.hewan_list
        )