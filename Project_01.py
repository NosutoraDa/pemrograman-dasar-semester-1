jmlMHS = int(input("Masukkan Jumlah Data Mahasiswa: "))

# deklarasi kan variable nama dan nilai
nama = []
nilai = []

# memasukkan data mahasiswa sesuai jumlah mahasiswa
for i in range(jmlMHS):
    nm = input("Nama Mahasiswa: ")
    nama.append(nm)
    nl = int(input("Masukkan Nilai: "))
    nilai.append(nl)

# menu data mahasiswa

while True:
    print("====== MENU ======")
    print(" 1. TAMBAH DATA MAHASISWA")
    print(" 2. LIHAT DATA MAHASISWA")
    print(" 3. CARI DATA MAHASISWA")
    print(" 4. DATA NILAI RATA-RATA MAHASISWA")
    print(" 5. DATA NILAI TERTINGGI & TERENDAH MAHASISWA")
    print(" 6. URUTAN DATA MAHASISWA")
    print(" 7. HAPUS DATA MAHASISWA")
    print(" 8. EXIT")
    print("====== MENU ======")

    menu = int(input("Masukkan Nomor anda: "))

    # menambahkan mahasiswa
    if menu == 1:
        jmlMHS = int(input("Masukkan Jumlah Data Mahasiswa: "))
        for i in range(jmlMHS):
            nm = input("Masukkan Nama Mahasiswa: ")
            nama.append(nm)
            nl = int(input("Masukkan Nilai Mahasiswa: "))
            nilai.append(nl)

    # menampilkan nilai mahasiswa
    elif menu == 2:
        print("==== DATA MAHASISWA ====")
        print("Jumlah data Mahasiswa", len(nama))
        for i in range(len(nama)):
            print(i+1," Nama ", nama[i])
            print("     Nilai ", nilai[i])
        print("==== DATA MAHASISWA ====")

        input("Tekan Enter untuk kembali ke menu...")

    # menambahkan fitur pencarian data mahasiswa
    elif menu == 3:
        cari = input("Masukkan nama Mahasiswa yang dicari: ")
        x=0
        for i in range(jmlMHS):
            x=x+1
            if cari == nama[i]:
                print("Nilai Mahasiswa: ",nilai[i])
                x=0
                input("Tekan Enter untuk kembali ke menu...")
            else:
                x=x+1

    # menghitung rata rata nilai mahasiswa
    elif menu == 4:
        totnil = 0
        for i in range(jmlMHS):
            totnil = totnil + nilai[i]

        rata2 = totnil / jmlMHS
        print("Rata-rata nilai Mahasiswa: ",rata2)
        input("Tekan Enter untuk kembali ke menu...")

    # mencari nilai tertinggi dan nilai terendah mahasiswa
    elif menu == 5:
        nmax = 0
        nmmax = ""
        nmin = 100 # harus nilai tertinggi jika tidak maka 0 akan menjadi terendah
        nmmin = ""

        for i in range(jmlMHS):
            if nmax <= nilai[i]:
                nmax = nilai[i]
                nmmax = nama[i]
        if nmin >= nilai[i]:
                nmin = nilai[i]
                nmmin = nama[i]

        print("Nama dengan nilai tertinggi adalah = ", nmmax , "dengan nilai", nmax)
        print("Nama dengan nilai terendah adalah = ", nmmin , "dengan nilai", nmin)
        input("Tekan Enter untuk kembali ke menu...")

    # mengurutkan data mahasiswa ascend descend

    elif menu == 6:
        print("===== ASCEND/DESCEND =====")
        print(" 1. ASCENDING")
        print(" 2. DESCENDING")
        print("===== ASCEND/DESCEND =====")

        menu2 = int(input("Pilih Nomor anda: "))

        if menu2 == 1:
            print("=== ASCEND ===")
            namnil = list(zip(nama, nilai))
            namnil.sort()
            for i in range(len(nama)):
                print(i+1,"Nama: ",nama[i])
                print("    Nilai: ",nilai[i])
            print("=== ASCEND ===")
        if menu2 == 2:
            print("=== DESCEND ===")
            namnil = list(zip(nama, nilai))
            namnil.sort(reverse=True)
            for i in range(len(nama)):
                print(i+1,"Nama: ",namnil[i][0])
                print("    Nilai: ",namnil[i][1])
            print("=== DESCEND ===")
        else:
            print("Menu Tidak di temukan")

        input("Tekan Enter untuk kembali ke menu...")

    # menghapus data mahasiswa

    elif menu == 7:
        hapus = input("Hapus Data Mahasiswa (Enter Nama Mahasiswa): ")

        if hapus in nama:
            i = nama.index(hapus)
            nama.pop(i)
            nilai.pop(i)
            jmlMHS = jmlMHS - 1
            print("Data Mahasiswa telah berhasi di hapus")
        else:
            print("Data Mahasiswa tidak ditemukan")

        input("Tekan Enter untuk kembali ke menu...")

    # keluar dari database/program
    elif menu == 8:
        print("Program Selesai!")
        break;

    # jika input selain 1 sampai 8
    else:
        print("menu tidak di temukan")
        input("Tekan Enter untuk kembali ke menu...")
        