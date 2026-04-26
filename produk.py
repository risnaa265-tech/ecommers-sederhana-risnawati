class Sepatu:
    def _init_(self, merk, model, harga, stok):
        self.merk = merk
        self.model = model
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        print(f"[{self.merk}] {self.model}")
        print(f"Harga: Rp{self.harga:,}")
        print(f"Sisa Stok: {self.stok} pasang")
        print("-" * 20)

class TokoSepatu:
    def _init_(self):
        self.katalog = []

    def tambah_produk(self, sepatu):
        self.katalog.append(sepatu)

    def lihat_semua_produk(self):
        print("=== KATALOG TOKO SEPATU ===")
        for item in self.katalog:
            item.tampilkan_info()

# --- Implementasi ---

# 1. Membuat objek sepatu
sepatu1 = Sepatu("Adidas", "Ultraboost 5.0", 3200000, 10)
sepatu2 = Sepatu("Nike", "Air Jordan 1 Low", 2500000, 5)
sepatu3 = Sepatu("Brodo", "Vantage V2 Hi", 400000, 15)

# 2. Memasukkan ke sistem toko
toko_saya = TokoSepatu()
toko_saya.tambah_produk(sepatu1)
toko_saya.tambah_produk(sepatu2)
toko_saya.tambah_produk(sepatu3)

# 3. Menampilkan katalog
toko_saya.lihat_semua_produk()