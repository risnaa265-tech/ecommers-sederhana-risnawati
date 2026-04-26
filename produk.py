# Contoh struktur data sederhana
produk_celana = {
    "CLN001": {"nama": "Jeans Slim Fit", "warna": "Navy", "harga": 195000},
    "CLN002": {"nama": "Chino Pants", "warna": "Khaki", "harga": 180000},
    "CLN003": {"nama": "Cargo Pants", "warna": "Olive", "harga": 200000}
}

def cek_harga(kode):
    barang = produk_celana.get(kode)
    if barang:
        return f"{barang['nama']} ({barang['warna']}) - Rp{barang['harga']}"
    else:
        return "Kode tidak ditemukan"

# Cara panggil
print(cek_harga("CLN001"))