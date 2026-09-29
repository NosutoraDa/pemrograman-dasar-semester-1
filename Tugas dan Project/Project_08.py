# Menampilkan banner tampilan awal
def tampilkan_banner():
    print("============ MENU ============")
    print("SELAMAT DATANG DI PERPUSTAKAAN")
    print("============ MENU ============")

def tampilkan_menu():
    print("====== MENU ======")
    print(" 1. TAMBAH BUKU")
    print(" 2. PINJAM BUKU")
    print(" 3. KEMBALIKAN BUKU")
    print(" 4. LIHAT DAFTAR BUKU")
    print(" 5. CARI BUKU")
    print(" 6. EXIT")
    print("====== MENU ======")

# tambah buku
def tambah_buku(x):
    global jmlbuku, dtbuku
    if x == '1':
        judul = input("Masukkan judul buku yg ingin di tambahkan: ")
        penulis = input("Masukkan Penulis/Penerbit buku: ")
        tahun = input("Masukkan Tahun buku ini diterbitkan: ")

        jmlbuku += 1

        dtbuku[jmlbuku] = {}

        dtbuku[jmlbuku]["judul"] = judul
        dtbuku[jmlbuku]["penulis"] = penulis
        dtbuku[jmlbuku]["tahun"] = tahun

        print(f"Buku dengan id: '{jmlbuku}', berhasil ditambahkan tuan")

# keseluruhan input dalam menu
def input_menu():
    n = True
    while n == True:
        tampilkan_banner()
        tampilkan_menu()
        print("Masukkan Pilihan Anda Tuan = ")
        item = input().lower()

        if item == '1':
            tambah_buku(item)

        if item == '4':
            print("\n--- Daftar Buku Terbaru ---")
            for key, value in dtbuku.items():
                print(f"{key}. {value['judul']} | {value['penulis']} | {value['tahun']} ")
                input("Tekan Enter untuk kembali ke menu...")
if __name__ == "__main__":
    global jmlbuku, dtbuku

    jmlbuku = 1
    dtbuku = {
        1 : {"judul" : "Jews the darkness",
            "penulis" : "Gunanda Fuhrer",
            "tahun" : "1000"}
    }

    input_menu()