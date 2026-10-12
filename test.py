import tkinter as tk
from tkinter import messagebox

# jendela utama (HARUS dibuat paling awal)
root = tk.Tk()
root.title("Kafe Kopi")
root.geometry("350x350")  # mengatur ukuran jendela
root.eval('tk::PlaceWindow . center')  # memposisikan jendela di tengah layar

# variabel tkinter (setelah root dibuat)
var_minuman = tk.StringVar()
var_xshot = tk.IntVar()
var_oatmilk = tk.IntVar()
var_vanilla = tk.IntVar()

def pil_minuman():
    return var_minuman.get()

def minuman_pilih():
    minuman = pil_minuman()

    # harga dasar minuman
    if minuman == "Espresso":
        total = 15000
    elif minuman == "Americano":
        total = 20000
    elif minuman == "Cappuccino":
        total = 25000
    else:
        messagebox.showerror("Input error", "Silakan pilih jenis kopi terlebih dahulu.")
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

    # menampilkan struk pembayaran
    messagebox.showinfo(
        "Struk Pembayaran",
        f"Jenis Kopi: {minuman}\n\n"
        f"Topping:\n{topping}\n"
        f"Total Harga: Rp{total:,.0f}".replace(",", ".")
    )

# label judul
label_judul = tk.Label(root, text="Kafe Kopi", font=("Arial", 12, "bold"))
label_judul.pack(pady=10)  # jarak antara judul dan label

# pilihan minum
label_minum = tk.Label(root, text="Silahkan pilih kopinya")
label_minum.pack(anchor="w")
minum_pil1 = tk.Radiobutton(root, text="Espresso - Rp15.000", variable=var_minuman, value="Espresso")
minum_pil1.pack(anchor="w")
minum_pil2 = tk.Radiobutton(root, text="Americano - Rp20.000", variable=var_minuman, value="Americano")
minum_pil2.pack(anchor="w")
minum_pil3 = tk.Radiobutton(root, text="Cappuccino - Rp25.000", variable=var_minuman, value="Cappuccino")
minum_pil3.pack(anchor="w")

# pilihan topping
label_topping = tk.Label(root, text="Pilih topping")
label_topping.pack(anchor="w")
topping_pil1 = tk.Checkbutton(root, text="Extra Shot (+5.000)", variable=var_xshot)
topping_pil1.pack(anchor="w")
topping_pil2 = tk.Checkbutton(root, text="Susu Oat (+10.000)", variable=var_oatmilk)
topping_pil2.pack(anchor="w")
topping_pil3 = tk.Checkbutton(root, text="Sirup Vanilla (+4.000)", variable=var_vanilla)
topping_pil3.pack(anchor="w")

# tombol pesan
tombol_pesan = tk.Button(root, text="Pesan Sekarang", command=minuman_pilih)
tombol_pesan.pack(pady=10)

root.mainloop()