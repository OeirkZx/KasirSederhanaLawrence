import time

# Tipe Data & Struktur Data: Dictionary untuk menyimpan menu (string dan integer)
menu_kasir = {
    "Kopi": 18000,
    "Teh": 15000,
    "Roti": 12000,
    "Donat": 8000,
}

# Inisialisasi pesanan (Struktur Data: list, sebagai sekuens)
pesanan = ["Kopi", "Roti", "Donat"]

# --- Fungsi-Fungsi ---

# 1. Sorting Manual Bubble Sort untuk harga (dari termahal)
def urutkan_harga_pesanan(items, menu):
    # Mengambil harga dari setiap item pesanan
    harga_items = [menu[item] for item in items]
    n = len(harga_items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if harga_items[j] < harga_items[j + 1]:
                # Tukar harga dan nama item secara bersamaan
                harga_items[j], harga_items[j + 1] = harga_items[j + 1], harga_items[j]
                items[j], items[j+1] = items[j+1], items[j]
    return items, harga_items

# 2. Fungsi Rekursif untuk menghitung total belanja
def hitung_total_rekursif(harga_list):
    if not harga_list:  # Kasus dasar: jika list harga kosong
        return 0
    else:
        # Menjumlahkan elemen pertama dengan sisa list (panggilan rekursif)
        return harga_list[0] + hitung_total_rekursif(harga_list[1:])

# --- Eksekusi Program Kasir ---

print("===== Struk Kasir Sederhana =====")
print(f"Pesanan Awal (Sekuens): {pesanan}")
print("-" * 35)

# Mengukur waktu eksekusi untuk proses sorting
start_sort_time = time.time()
pesanan_terurut, harga_terurut = urutkan_harga_pesanan(pesanan, menu_kasir)
end_sort_time = time.time()
execution_sort_time = end_sort_time - start_sort_time

print("Pesanan diurutkan dari termahal:")
for item in pesanan_terurut:
    print(f"- {item}: Rp{menu_kasir[item]}")
print(f"Waktu eksekusi sorting: {execution_sort_time:.10f} detik")
print("-" * 35)

# Mengukur waktu eksekusi untuk perhitungan total rekursif
start_total_time = time.time()
total_belanja = hitung_total_rekursif(harga_terurut)
end_total_time = time.time()
execution_total_time = end_total_time - start_total_time

print(f"Total Belanja: Rp{total_belanja}")
print(f"Waktu eksekusi perhitungan total: {execution_total_time:.10f} detik")
print("=" * 35)