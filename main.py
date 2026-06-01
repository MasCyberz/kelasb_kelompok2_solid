from hewan.hewan_darat import Kucing, Pinguin
from habitat.kandang import Kandang

from services.pemberian_makan import PemberianMakan
from services.perawatan import Perawatan

from zoo.kebun_binatang import KebunBinatang


def main():

    kucing = Kucing("Kucing Himalaya", "Albino", 3)
    pinguin = Pinguin("Pinguin Antartika", "Hitam", 5)

    kandang = Kandang("Kandang Kutub")

    kandang.tambah_hewan(kucing)
    kandang.tambah_hewan(pinguin)

    kandang.tampilkan_penghuni()

    pemberian_makan = PemberianMakan()
    perawatan = Perawatan()

    kebun_binatang = KebunBinatang(
        kandang,
        pemberian_makan,
        perawatan
    )

    kebun_binatang.operasional_harian()


if __name__ == "__main__":
    main()