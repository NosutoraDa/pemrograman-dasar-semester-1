import tkinter as tk
from tkinter import messagebox

def pil_minuman():
    return var_minuman.get()

def minuman_pilih():
    try:
        minuman = pil_minuman()
        # mengambil nilai dari kolom input/entry dan mengubahnya jadi float

        # harga per 100 ml untuk tiap minuman
        if minuman == "Espresso":
            total = 15000
        elif minuman == "Americano":
            total = 20000
        elif minuman == "Cappucino":
            total = 25000
        else:
            messagebox.showwarning("Pilih minuman", "Silakan pilih jenis minuman terlebih dahulu.")
            return

        # tambahan topping (bisa lebih dari satu), .get() mengambil 1 atau 0
        topping = ""
        if var_xshot.get() == 1:
            total += 5000
            topping += "- Extra Shot (Rp5.000)\n"
        if var_oatmilk.get() == 1:
            total += 10000
            topping += "- Susu Oat (Rp10.000)\n"
        if var_vanilla.get() == 1:
            total += 4000
            topping += "- Sirup Vanilla (Rp4.000)\n"

        if topping == "":
            topping = "- Tanpa topping\n"


        # menampilkan hasil pada label dengan mengedit config
        messagebox.showinfo(
            "Struk Pembayaran",
            f"Jenis Kopi: {minuman}\n\n"
            f"Topping:\n{topping}\n"
            f"Total Harga: Rp{total:,.0f}"
            "Terima Kasih atas pembeliannya Tuan!!".replace(",", ".")
        )

    except ValueError:
        messagebox.showerror("Input error")

# jendela utama
root = tk.Tk()

var_minuman = tk.StringVar()
var_xshot = tk.BooleanVar()
var_oatmilk = tk.BooleanVar()
var_vanilla = tk.BooleanVar()

root.title ("Dapa Warrior Cafe")
root.geometry("500x350") # mengatur ukuran jendela
root.eval('tk::PlaceWindow . center') # memposiskan jendela di tengah layar

# label judul
label_judul = tk.Label(root, text="Hitlers Drinks", font=("Arial", 12, "bold"))
label_judul.pack(pady=10)

# pilihan minum
label_minum = tk.Label(root, text="Silahkan pilih kopinya", font=("Arial", 15))
label_minum.pack()

frame_minum = tk.Frame(root)
frame_minum.pack(pady=5)

minum_pil1 = tk.Radiobutton(frame_minum, text="Espresso - Rp15.000", variable=var_minuman, value="Espresso")
minum_pil1.grid(row=0, column=0, padx=5)
minum_pil2 = tk.Radiobutton(frame_minum, text="Americano - Rp20.000", variable=var_minuman, value="Americano")
minum_pil2.grid(row=0, column=1, padx=5)
minum_pil3 = tk.Radiobutton(frame_minum, text="Cappuccino - Rp25.000", variable=var_minuman, value="Cappuccino")
minum_pil3.grid(row=0, column=2, padx=5)

# pilihan topping
label_topping = tk.Label(root, text="Pilih topping")
label_topping.pack(pady=(10, 0))

frame_topping = tk.Frame(root)
frame_topping.pack(pady=5)

topping_pil1 = tk.Checkbutton(frame_topping, text="Extra Shot (+5.000)", variable=var_xshot)
topping_pil1.grid(row=0, column=0, padx=5)
topping_pil2 = tk.Checkbutton(frame_topping, text="Susu Oat (+10.000)", variable=var_oatmilk)
topping_pil2.grid(row=0, column=1, padx=5)
topping_pil3 = tk.Checkbutton(frame_topping, text="Sirup Vanilla (+4.000)", variable=var_vanilla)
topping_pil3.grid(row=0, column=2, padx=5)

# tombol pesan
tombol_pesan = tk.Button(root, text="Pesan Sekarang", command=minuman_pilih)
tombol_pesan.pack(pady=10)

root.mainloop()