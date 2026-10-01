        if item == '4':
            print("\n--- Daftar Buku ---")
            for key, value in dtbuku.items():
                
                list_peminjaman = [p["nama"] for p in peminjaman_db if p["id_buku"] == key]

                if list_peminjaman:
                    status_peminjam = ", ".join(list_peminjaman)

                else:
                    status_peminjam = "Belum ada yang pinjam"
                print(f"{key}. {value['judul']} | {value['penulis']} | {value['tahun']} | Stok buku: {value['stok']}")
                print(f"Status Buku Peminjaman: {status_peminjam}")
            input("Tekan Enter untuk kembali ke menu...")