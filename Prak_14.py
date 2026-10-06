import tkinter as tk
from tkinter import messagebox

# menghitung luas
def hitung_luas():
    try:
        # mengambil nilai dari kolom input/entry dan mengubahnya jadi float
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())

        # proses perhitung
        luas = panjang * lebar

        # menampilkan hasil pada label dengan mengedit config
        label_hasil.config(text=f"Luas: {luas}")

    except ValueError:
        messagebox.showerror("Input error", "Masukkan angka yang valid untuk panjang dan lebar.")


# 1. membuat jendela utama
root = tk.Tk()

root.title ("Kalkulator Luas Persegi Panjang")
root.geometry("350x250") # mengatur ukuran jendela
root.eval('tk::PlaceWindow . center') # memposiskan jendela di tengah layar

# 2. Membuat Label Judul
label_judul = tk.Label(root, text = "Hitung Luas Persegi Panjang", font=("Arial", 12, "bold"))
label_judul.pack(pady=10) # jarak antara judul dan label

# 3. Membuat Input untuk Panjang
label_panjang = tk.Label(root, text="Masukkan Panjang: ")
label_panjang.pack()

entry_panjang = tk.Entry(root, width=20)
entry_panjang.pack(pady=5)

# 4. Membuat Input Untuk Lebar
label_lebar = tk.Label(root, text="Masukkan Lebar: ")
label_lebar.pack()

entry_lebar = tk.Entry(root, width=20)
entry_lebar.pack(pady=5)

# 5. Membuat tombol Hitung
tombol_hitung = tk.Button(root, text="Hitung Luas", command= hitung_luas, bg="lightblue")
tombol_hitung.pack(pady=5)

# 6. Membuat Label untuk menampilkan Hasil
label_hasil = tk.Label(root, text="Luas : -", font=("Arial", 12, "bold"), fg="green")
label_hasil.pack(pady=5)

# Menjalankan Aplikasi
root.mainloop()

