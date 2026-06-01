# interfaces/interfaces.py
# Dibuat oleh: Keisha

from abc import ABC, abstractmethod

# ============================================
# INTERFACE - BISA BERJALAN
# ============================================
# Interface ini digunakan sebagai "kontrak"
# untuk hewan yang dapat berjalan.
#
# Contoh:
# - Singa
# - Burung
# - Pinguin
#
# Hewan yang tidak memiliki kemampuan berjalan
# tidak perlu mengimplementasikan interface ini.

class BisaBerjalan(ABC):
    @abstractmethod
    def berjalan(self):
        pass