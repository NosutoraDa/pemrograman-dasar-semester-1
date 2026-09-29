def tampilkan_menu():
    print("\n=== MENU PERPUSTAKAAN ===")
    print("1. Tambah Buku")
    print("2. Pinjam Buku")
    print("3. Kembalikan Buku")
    print("4. Lihat Daftar Buku")
    print("5. Keluar")

def tambah_buku(kumpulan_buku):
    judul = input("Masukkan judul buku yang ingin ditambahkan: ")
    kumpulan_buku.append(judul)
    print(f"Buku '{judul}' berhasil ditambahkan!")

def main():
    # Variabel list untuk menyimpan data buku
    data_buku = []
    
    n = True
    while n == True:
        tampilkan_menu()
        print("Silahkan pilih menu yang diinginkan (1-5): ")
        item = input().lower()
        
        # Pilihan untuk Menambah Buku
        if item == '1':
            tambah_buku(data_buku)

        # Pilihan untuk Pinjam Buku (Contoh placeholder)
        elif item == '2':
            print("\n[Fitur Pinjam Buku]")
            # Masukkan fungsi pinjam buku di sini
            
        # Pilihan untuk Lihat Buku
        elif item == '4':
            print("\n--- Daftar Buku Saat Ini ---")
            if len(data_buku) == 0:
                print("Belum ada buku.")
            else:
                for i, buku in enumerate(data_buku, 1):
                    print(f"{i}. {buku}")
                    
        # Pilihan untuk Keluar Program
        elif item == '5' or item == 'keluar':
            print("Terima kasih telah menggunakan perpustakaan!")
            n = False # Mengubah nilai loop agar berhenti
            
        else:
            print("Pilihan tidak valid, silakan masukkan nomor 1 sampai 5.")

# Menjalankan program utama
if __name__ == "__main__":
    main()