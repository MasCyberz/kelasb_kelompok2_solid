# interfaces/interfaces.py
# Dibuat oleh: Keisha

from abc import ABC, abstractmethod

# ============================================
# INTERFACE - BISA BERENANG
# ============================================
# Interface ini digunakan sebagai "kontrak" untuk
# hewan-hewan yang memiliki kemampuan berenang.
# Contoh: Ikan, Pinguin
# Hewan yang tidak bisa berenang (Singa, Burung)
# TIDAK boleh mengimplementasikan interface ini.

class BisaBerenang(ABC):
    @abstractmethod
    def berenang(self):
        pass
