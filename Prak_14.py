import tkinter as tk
from tkinter import messagebox

# menghitung bmi
def hitung_bmi():
    try:
        # mengambil nilai dari kolom input/entry dan mengubahnya jadi float
        berat = float(entry_panjang.get())
        tinggi = float(entry_lebar.get()) / 100

        # proses perhitung
        luas = berat / (tinggi * tinggi)

        # menampilkan hasil pada label dengan mengedit config
        bmi = luas

        # mengkategorikan bmi

        if bmi < 18.5:
            label_hasil.config(text=f"BMI anda: {luas:.2f}, anda adalah kurus")
        elif bmi > 18.5:
            label_hasil.config(text=f"BMI anda: {luas:.2f}, anda adalah normal")
        elif bmi > 24.9:
            label_hasil.config(text=f"BMI anda: {luas:.2f}, anda adalah gemuk")
        elif bmi > 30:
            label_hasil.config(text=f"BMI anda: {luas:.2f}, anda adalah obesitas")
    

    except ValueError:
        messagebox.showerror("Input error", "Masukkan angka yang valid untuk panjang dan lebar.")


# 1. membuat jendela utama
root = tk.Tk()

root.title ("Kalkulator BMI")
root.geometry("350x250") # mengatur ukuran jendela
root.eval('tk::PlaceWindow . center') # memposiskan jendela di tengah layar

# 2. Membuat Label Judul
label_judul = tk.Label(root, text = "Hitung BMI orang", font=("Arial", 12, "bold"))
label_judul.pack(pady=10) # jarak antara judul dan label

# 3. Membuat Input untuk Berat
label_panjang = tk.Label(root, text="Masukkan berat: ")
label_panjang.pack()

entry_panjang = tk.Entry(root, width=20)
entry_panjang.pack(pady=5)

# 4. Membuat Input Untuk Tinggi
label_lebar = tk.Label(root, text="Masukkan tinggi: ")
label_lebar.pack()

entry_lebar = tk.Entry(root, width=20)
entry_lebar.pack(pady=5)

# 5. Membuat tombol Hitung
tombol_hitung = tk.Button(root, text="Hitung Luas", command= hitung_bmi, bg="lightblue")
tombol_hitung.pack(pady=5)

# 6. Membuat Label untuk menampilkan Hasil
label_hasil = tk.Label(root, text="Luas : -", font=("Arial", 12, "bold"), fg="green")
label_hasil.pack(pady=5)

# Menjalankan Aplikasi
root.mainloop()

