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
    global jmlbuku, dtbuku,id_buku
    if x == '1':
        judul = input("Masukkan judul buku yg ingin di tambahkan: ")
        penulis = input("Masukkan Penulis/Penerbit buku: ")
        tahun = input("Masukkan Tahun buku ini diterbitkan: ")
        stok = int(input("Masukkan Stok dari buku ini: "))

        id_buku = jmlbuku


        dtbuku[id_buku] = {}

        dtbuku[id_buku]["judul"] = judul
        dtbuku[id_buku]["penulis"] = penulis
        dtbuku[id_buku]["tahun"] = tahun
        dtbuku[id_buku]["stok"] = stok

        print(f"Buku dengan id: '{jmlbuku}', berhasil ditambahkan tuan")

        jmlbuku += 1

        return id_buku
        

def pinjam_buku(y):
    global dtbuku,peminjaman_db,id_buku

    if y == '2':
        id_buku = int(input("Masukkan ID Buku yang ingin dipinjam: "))
        nama_peminjam = input("Masukkan Nama Anda: ")

        if id_buku not in dtbuku:
            return f"Buku dengan id '{id_buku}' tidak di temukan tuan"

        if dtbuku["stok"] <= 0:
            return f"Buku dengan id '{id_buku}' sudah ada yang meminjam"

        dtbuku["stok"] -= 1
        
        peminjaman_db.append(
            {"nama": nama_peminjam, "id_buku": id_buku, "judul": dtbuku["judul"]}
        )

        return f"Buku '{dtbuku['judul']}' berhasil di pinjam oleh {nama_peminjam}."




# keseluruhan input dalam menu
def input_menu():
    n = True
    while n == True:
        tampilkan_banner()
        tampilkan_menu()
        print("Masukkan Pilihan Anda Tuan = ")
        item = input().lower()

        if item == '1':
            for key, value in dtbuku.items():
                print(f"{key}. {value['judul']} | {value['penulis']} | {value['tahun']} | {value['stok']}")
            tambah_buku(item)

# menampilkan databuku
        if item == '4':
            print("\n--- Daftar Buku ---")
            for key, value in dtbuku.items():
                print(f"{key}. {value['judul']} | {value['penulis']} | {value['tahun']} | {value['stok']}")
            input("Tekan Enter untuk kembali ke menu...")
            
if _name_ == "_main_":
    global jmlbuku, dtbuku


    dtbuku = {
        1 : {"judul" : "Jews the darkness",
            "penulis" : "Gunanda Fuhrer",
            "tahun" : "1000",
            "stok" : 1}
    }

    jmlbuku = len(dtbuku) + 1
    peminjaman_db = []
    input_menu()