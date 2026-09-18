# Inisialisasi  List of Tuples yang berisi (tanggal, kode_produk, jumlah, harga)

transaksi = [
    ("2024-01-05", "P001", 3, 15000),
    ("2024-01-05", "P002", 2, 25000),
    ("2024-01-06", "P001", 5, 15000),
    ("2024-01-06", "P003", 1, 50000),
    ("2024-02-01", "P002", 4, 25000),
    ("2024-02-02", "P001", 2, 15000),
    ("2024-02-02", "P003", 3, 50000),
    ("2024-02-03", "P001", 1, 15000)
]
    
# Menampilkan pendapatan perproduk untuk setiap kode produk, diurutkan dari terbesar ke terkecil
satudata = []

print("==========LIST OF TUPLES==========")
for kode in ["P001","P002","P003"]:
    total = 0
    harga_barang = 0
    for tnggl,kodebrg,jmlh,harga in transaksi:
        if kodebrg == kode:
            total += jmlh
            harga_barang = harga
    satudata.append(("", kode,total,harga_barang))

urutdata = tuple(sorted(satudata, key=lambda item: item[2] * item[3], reverse=True))

for x in range(len(urutdata)):
    kodebrg = urutdata[x][1]
    total = urutdata[x][2] * urutdata[x][3]
    print(x + 1, "Kode Barang:", kodebrg, "Dan Pendapatan sebesar: Rp.", total)
print("==========LIST OF TUPLES==========")

# total pendapatan perbulan
total_bln1 = 0
total_bln2 = 0

for x in range(len(transaksi)):
    for tnggl,kodebrg,jmlh,harga in transaksi:

        if "2024-01" in tnggl:
            total_bln1 += jmlh * harga
        elif "2024-02" in tnggl:
            total_bln2 += jmlh * harga

# Urutkan menggunakan if else

if total_bln2 >= total_bln1:
    print("=====DESCEND=====")
    print(1, "Bulan 02 dengan Pendapatan sebesar", total_bln2)
    print(2, "Bulan 01 dengan Pendapatan sebesar", total_bln1)
    print("=====DESCEND=====")
else: 
    print("=====ASCEND=====")
    print(1, "Bulan 01 dengan Pendapatan sebesar", total_bln1)
    print(2, "Bulan 02 dengan Pendapatan sebesar", total_bln2)
    print("=====ASCEND=====")

# produk dengan total unit terbanyak
jmlh_tertinggi = 0
kodebrg_tertinggi = ""

for x in range(len(transaksi)):
    for tnggl,kodebrg,jmlh,harga in transaksi:
        if jmlh > jmlh_tertinggi:
            jmlh_tertinggi = jmlh
            kodebrg_tertinggi = kodebrg
print("=====UNIT TERBANYAK=====")
print("Kode barang", kodebrg_tertinggi, "adalah produk dengan penjualan terbanyak dengan total", jmlh_tertinggi)
print("=====UNIT TERBANYAK=====")

# menghitung Rata-rata jumlah barang per transaksi

print("=====RATA-RATA_BARANG=====")
for kode in ["P001","P002","P003"]:
    total_jmlh = 0
    count = 0
    for tnggl,kodebrg,jmlh,harga in transaksi:
        if kodebrg == kode:
            total_jmlh += jmlh
            count += 1

    rata2jmlh = total_jmlh / count
    print(f"Rata-rata unit barang {kode} pertransaksi: {rata2jmlh:.2f} ")
print("=====RATA-RATA_BARANG=====")

# daftar transaksi pada tanggal tertentu yang di input

cari_tnggl = input("Silahkan Masukkan Tanggal Transaksi: ")
hasil = []

for tnggl,kodebrg,jmlh,harga in transaksi:
    if cari_tnggl in tnggl:
        hasil.append((tnggl,kodebrg,jmlh,harga))

if not hasil:
    print("Tidak ada transaksi ditemukan untuk", cari_tnggl,". . .")

else:
    print("=====PERCARIAN=====")
    print(f"Hasil pencarian {cari_tnggl} telah ditemukan")
    for tnggl,kodebrg,jmlh,harga in hasil:
        print(tnggl,kodebrg,jmlh,harga)
    print("=====PENCARIAN====")
