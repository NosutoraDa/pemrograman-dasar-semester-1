# 1. Deklarasi & Input Awal
jmlMHS = int(input("Masukkan Jumlah Data Mahasiswa: "))
nama = []
nilai = []

for i in range(jmlMHS):
    nm = input("Nama Mahasiswa: ")
    nama.append(nm)
    nl = int(input("Masukkan Nilai: "))
    nilai.append(nl)

# 2. Loop Utama
while True:
    print("====== MENU ======")
    print("1. TAMBAH DATA MAHASISWA")
    print("2. LIHAT DATA MAHASISWA")
    print("8. EXIT")
    print("====== MENU ======")

    menu = int(input("Masukkan Nomor anda: "))

    # PERBAIKAN: Komentar `#` dan `if` HARUS di-indent 4 spasi (di dalam while)
    if menu == 1:
        tambah = int(input("Masukkan Jumlah Data Mahasiswa: "))
        for i in range(tambah):
            nm = input("Masukkan Nama Mahasiswa: ")
            nama.append(nm)
            nl = int(input("Masukkan Nilai Mahasiswa: "))
            nilai.append(nl)

    # PERBAIKAN: Komentar `#` dan `elif` juga 4 spasi (di dalam while)
    elif menu == 2:
        print("===== DATA MAHASISWA =====")
        print("Jumlah data Mahasiswa:", len(nama))
        
        # Pakai len(nama) supaya pembacaan data tidak terpotong!
        for i in range(len(nama)):
            print(i + 1, "Nama :", nama[i])
            print("   Nilai:", nilai[i])
        print("===== DATA MAHASISWA =====")

        input("\nTekan Enter untuk kembali ke menu...")