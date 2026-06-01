from interfaces.bisa_berjalan import BisaBerjalan
from interfaces.bisa_berenang import BisaBerenang
from interfaces.bisa_terbang import BisaTerbang

class Perawatan:
    def rawat(self, daftar_hewan):

        print("\n=== PERAWATAN HEWAN ===")

        for hewan in daftar_hewan:

            if isinstance(hewan, BisaBerjalan):
                hewan.berjalan()

            if isinstance(hewan, BisaTerbang):
                hewan.terbang()

            if isinstance(hewan, BisaBerenang):
                hewan.berenang()