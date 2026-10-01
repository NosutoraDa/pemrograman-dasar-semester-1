from datetime import datetime, timedelta

# Menampilkan banner tampilan awal
def tampilkan_banner():
    print("================= MENU =================")
    print("SELAMAT DATANG DI PERPUSTAKAAN CENDEKIA")
    print("================= MENU =================")

def tampilkan_menu():
    print("====== MENU ======")
    print(" 1. TAMBAH BUKU")
    print(" 2. PINJAM BUKU")
    print(" 3. KEMBALIKAN BUKU")
    print(" 4. LIHAT DAFTAR BUKU")
    print(" 5. EXIT")
    print("====== MENU ======")

# ubah angka status jadi teks: 1 = Tersedia, 0 = Kosong
def status_teks(status):
    return "Tersedia" if status == 1 else "Kosong"

# format angka jadi rupiah, contoh: 3000 -> Rp 3.000
def format_rupiah(angka):
    return "Rp " + f"{angka:,}".replace(",", ".")

# tambah buku
def tambah_buku(x):
    global jmlbuku, dtbuku, id_buku
    if x == '1':
        judul = input("Masukkan judul buku yg ingin di tambahkan: ")
        penulis = input("Masukkan Penulis/Penerbit buku: ")
        tahun = input("Masukkan Tahun buku ini diterbitkan: ")

        # validasi: hanya boleh 1 atau 0
        while True:
            status = input("Status buku (1 = Tersedia, 0 = Kosong): ")
            if status in ('0', '1'):
                status = int(status)
                break
            print("Input tidak valid, masukkan 1 atau 0.")

        id_buku = jmlbuku

        dtbuku[id_buku] = {
            "judul": judul,
            "penulis": penulis,
            "tahun": tahun,
            "status": status,
            "peminjam": []
        }

        print(f"Buku dengan id: '{id_buku}', berhasil ditambahkan tuan")

        jmlbuku += 1
        return id_buku

# pinjam buku
def pinjam_buku(y):
    global dtbuku, peminjaman_db, id_buku

    if y == '2':
        id_buku = int(input("Masukkan ID Buku yang ingin dipinjam: "))
        nama_peminjam = input("Masukkan Nama Anda: ")

        if id_buku not in dtbuku:
            return f"Buku dengan id '{id_buku}' tidak di temukan tuan"

        buku = dtbuku[id_buku]

        # kalau status Kosong (0), buku tidak bisa dipinjam
        if buku["status"] == 0:
            peminjam_str = ", ".join(p["nama"] for p in buku["peminjam"]) or "-"
            return (f"\nJudul    : {buku['judul']}\nStatus   : {status_teks(buku['status'])}"
                    f"\n\n Buku \"{buku['judul']}\" sedang dipinjam oleh {peminjam_str}.")

        # pinjam: status berubah jadi Kosong (0), simpan nama + tanggal pinjam
        tanggal_pinjam = datetime.now()
        buku["status"] = 0
        buku["peminjam"].append({"nama": nama_peminjam, "tanggal_pinjam": tanggal_pinjam})

        peminjaman_db.append(
            {"nama": nama_peminjam, "id_buku": id_buku, "judul": buku["judul"],
             "tanggal_pinjam": tanggal_pinjam}
        )

        return (f"\nJudul          : {buku['judul']}\nPeminjam       : {nama_peminjam}"
                f"\nTanggal pinjam : {tanggal_pinjam.strftime('%d-%m-%Y')}"
                f"\n\n Buku \"{buku['judul']}\" berhasil dipinjam oleh {nama_peminjam}."
                f"\n Batas pengembalian 7 hari, denda {format_rupiah(1000)}/hari jika terlambat.")

# kembalikan buku
def kembalikan_buku(y):
    global dtbuku, id_buku

    if y == '3':
        id_buku = int(input("Masukkan ID Buku yang ingin dikembalikan: "))
        nama_peminjam = input("Masukkan Nama Anda: ")

        if id_buku not in dtbuku:
            return f"Buku dengan id '{id_buku}' tidak di temukan tuan"

        buku = dtbuku[id_buku]

        # cari data peminjaman berdasarkan nama
        data_pinjam = None
        for p in buku["peminjam"]:
            if p["nama"] == nama_peminjam:
                data_pinjam = p
                break

        if data_pinjam is None:
            return f"Nama '{nama_peminjam}' tidak tercatat meminjam buku ini tuan"

        # hitung lama pinjam dan denda (Rp 1.000/hari jika lewat 7 hari)
        hari_pinjam = (datetime.now() - data_pinjam["tanggal_pinjam"]).days
        hari_telat = max(0, hari_pinjam - 7)
        denda = hari_telat * 1000

        buku["peminjam"].remove(data_pinjam)
        buku["status"] = 1  # kembali Tersedia

        return (f"\nJudul          : {buku['judul']}\nPeminjam       : {nama_peminjam}"
                f"\nTanggal pinjam : {data_pinjam['tanggal_pinjam'].strftime('%d-%m-%Y')}"
                f"\nLama pinjam    : {hari_pinjam} hari"
                f"\nTelat          : {hari_telat} hari"
                f"\nTotal denda    : {format_rupiah(denda)}"
                f"\n\n Buku \"{buku['judul']}\" berhasil dikembalikan oleh {nama_peminjam}.")

# keseluruhan input dalam menu
def input_menu():
    n = True
    while n == True:
        tampilkan_banner()
        tampilkan_menu()
        print("Masukkan Pilihan Anda Tuan = ")
        item = input().lower()
        print(f"Pilih: {item}\n")

        if item == '1':
            for key, value in dtbuku.items():
                print(f"{key}. {value['judul']} | {value['penulis']} | {value['tahun']} | {status_teks(value['status'])}")
            tambah_buku(item)
            input("Tekan Enter untuk kembali ke menu...")

        if item == '2':
            print(pinjam_buku(item))
            input("Tekan Enter untuk kembali ke menu...")

        if item == '3':
            print(kembalikan_buku(item))
            input("Tekan Enter untuk kembali ke menu...")

        # menampilkan data buku
        if item == '4':
            print("\n--- Daftar Buku ---")
            print(" a. Keseluruhan Data Buku")
            print(" b. Filter Yang Tersedia saja")
            print("Masukkan Pilihan Anda Tuan = ")
            pilihan = input().lower()
            print(f"Pilih: {pilihan}\n")

            if pilihan == 'a':
                for key, value in dtbuku.items():
                    print(f"{key}. {value['judul']} | {value['penulis']} | {value['tahun']} | Status: {status_teks(value['status'])}")
            elif pilihan == 'b':
                for key, value in dtbuku.items():
                    if value['status'] == 1:
                        print(f"{key}. {value['judul']} | {value['penulis']} | {value['tahun']} | Status: {status_teks(value['status'])}")
            else:
                print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali ke menu...")

        # exit
        if item == '5':
            print("gudbai")
            break

if __name__ == "__main__":
    dtbuku = {
        1: {"judul": "Jews the darkness",
            "penulis": "Gunanda Fuhrer",
            "tahun": "1000",
            "status": 1,
            "peminjam": []},
        2: {"judul": "Arif Unlimited Rizz",
            "penulis": "Arifu Darkness",
            "tahun": "2026",
            "status": 1,
            "peminjam": []},
        3: {"judul": "Dimas Romances Story",
            "penulis": "Vergil",
            "tahun": "1500",
            "status": 0,
            # dipinjam 10 hari lalu, untuk testing denda (3 hari telat = Rp 3.000)
            "peminjam": [{"nama": "Rehan Paleojavanicus",
                          "tanggal_pinjam": datetime.now() - timedelta(days=10)}]}
    }

    jmlbuku = len(dtbuku) + 1
    peminjaman_db = []
    input_menu()