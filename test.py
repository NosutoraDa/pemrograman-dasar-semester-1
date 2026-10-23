import tkinter as tk
from tkinter import messagebox

def tambah_tugas():
    try:
        tugas = entry_tmbhtugas.get().strip()
        if tugas == "":
            messagebox.showwarning("Peringatan", "Tugas tidak boleh kosong!")
            return
        listtugas.insert(tk.END, tugas)
        entry_tmbhtugas.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Input error", "Masukkan input yg benar")

def hapus_tugas():
    piltgs = listtugas.curselection()
    if not piltgs:
        messagebox.showwarning("Warning Tuan", "Pilih mas")
        return
    index = piltgs[0]
    listtugas.delete(index)

def bersihkan_semua():
    if listtugas.size() == 0:
        messagebox.showwarning("Peringatan", "Daftar tugas sudah kosong!")
        return
    jawab = messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus semua tugas?")
    if jawab:
        listtugas.delete(0, tk.END)

root = tk.Tk()
root.title("Aplikasi Produktivitas")
root.geometry("500x350")
root.eval('tk::PlaceWindow . center')

label_judul = tk.Label(root, text="Aplikasi Produktivitas", font=("Times New Roman", 12, "bold"))
label_judul.pack(pady=10)

label_tambahtgs = tk.Label(root, text="Masukkan Tugas: ")
label_tambahtgs.pack(pady=5)
entry_tmbhtugas = tk.Entry(root, width=50)
entry_tmbhtugas.pack()

# ERROR: The button is packed BEFORE the function 'tambah_tugas' is defined, 
# or here the variable name has a typo, or pack/grid parameters are messed up.
# Try debugging this broken version:
tombol_tambah = tk.Button(root, text="Tambah Tugas", command=tambah_tugas, bg="lightgreen")
tombol_tambah.pack(pady=5)

frame_list = tk.Frame(root)
frame_list.pack(pady=5)

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side="right", fill="y")

listtugas = tk.Listbox(frame_list, width=50, height=10, yscrollcommand=scrollbar.set)
listtugas.pack(pady=5)

frame_hapus = tk.Frame(root)
frame_hapus.pack(pady=5)

tombol_hapus = tk.Button(frame_hapus, text="Hapus beberapa", command=hapus_tugas, bg="pink")
# ERROR: Using grid() inside a frame where pack() or mixed geometry managers clash, 
# or passing invalid row/column parameters.
tombol_hapus.grid(row=0, column=0, padx=5)

tombol_hapusttl = tk.Button(frame_hapus, text="Hapus total", command=bersihkan_semua, bg="red")
tombol_hapusttl.grid(row=0, column=1, padx=5)

root.mainloop()