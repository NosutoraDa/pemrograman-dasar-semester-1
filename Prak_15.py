import tkinter as tk
from tkinter import messagebox

# menghitung luas
def hitung_luas():
    try:
        bangun = pil_bangunan()
        # mengambil nilai dari kolom input/entry dan mengubahnya jadi float
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())

        # proses perhitung
        if bangun == "persegi_panjang":
            luas = panjang * lebar
        elif bangun == "segitiga":
            luas = 0.5 * panjang * lebar
        elif bangun == "lingkaran":
            luas = 3.14 * (panjang ** 2)
            

        # menampilkan hasil pada label dengan mengedit config
        label_hasil.config(text=f"Luas: {luas}")

    # menampilkan error
    except ValueError:
        messagebox.showerror("Input error", "Masukkan angka yang valid untuk panjang dan lebar.")

def ubah_tampilan():
    bangun = pil_bangunan.get()

    # mengubah tampilan dengan config if elif
    if bangun == "persegi_panjang":
        label_panjang.config(text="Masukkan Panjang: ")
        label_lebar.config(text="Masukkan Lebar: ")
    elif bangun == "segitiga":
        label_panjang.config(text="Masukkan Alas: ")
        label_lebar.config(text="Masukkan Tinggi: ")
    else:
        label_panjang.config(text="Masukkan P / 3.14: ")
        label_lebar.config(text="Masukkan Jari-jari lingkaran: ")

# 1. membuat jendela utama
root = tk.Tk()

root.title ("Kalkulator Perhitungan Luas Bangunan")
root.geometry("450x350") # mengatur ukuran jendela
root.eval('tk::PlaceWindow . center') # memposiskan jendela di tengah layar

# 2. Membuat Label Judul
label_judul = tk.Label(root, text = "Hitung Luas Persegi Panjang", font=("Arial", 12, "bold"))
label_judul.pack(pady=10) # jarak antara judul dan label

# radio button untuk 1 pilihan

pil_bangunan = tk.StringVar(value="persegi_panjang")

# menambah frame radio agar tidak stuck pack
frame_radio = tk.Frame(root)
frame_radio.pack(pady=5)

pill1 = tk.Radiobutton(frame_radio, text="Persegi Panjang", value="persegi_panjang", command=ubah_tampilan, variable=pil_bangunan)
pill1.grid(row=0, column=0, padx=5) #column itu urutan jadi 0,1,2

pill2 = tk.Radiobutton(frame_radio, text="Segitiga", value="segitiga", command=ubah_tampilan, variable=pil_bangunan)
pill2.grid(row=0, column=1, padx=5)

pill3 = tk.Radiobutton(frame_radio, text="Lingkaran", value="lingkaran", command=ubah_tampilan, variable=pil_bangunan)
pill3.grid(row=0, column=2, padx=5)

# 3. Membuat Input untuk Panjang
label_panjang = tk.Label(root, text="- : ")
label_panjang.pack()

entry_panjang = tk.Entry(root, width=20)
entry_panjang.pack(pady=5)

# 4. Membuat Input Untuk Lebar
label_lebar = tk.Label(root, text="- : ")
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

