import tkinter as tk
from tkinter import messagebox

# fitur menambahkan tugas
def tambah_tugas():
    try:
        tugas = entry_tmbhtugas.get()

        if tugas == "":
            messagebox.showwarning("Peringatan", "Tugas tidak boleh kosong!")
            return
        
        listtugas.listbox.insert(tk.END, tugas)
        listtugas_entry.delete(0, tk.END)

    except ValueError:
            messagebox.showerror("Input error", "Masukkan input yg benar")

def hapus_tugas():
    # 1. cari tahu item mana yang sedang dipilih (hint: cari "curselection")
    # 2. bagaimana kalau tidak ada yang dipilih? pikirkan apa yang terjadi
    # 3. hapus item itu dari listbox
    pass

def bersihkan_semua():
    # kosongkan seluruh isi listbox (hint: delete dari index 0 sampai tk.END)
    pass


# ---------- JENDELA UTAMA ----------
root = tk.Tk()
root.title("Aplikasi Produktivitas")
root.geometry("500x350")
root.eval('tk::PlaceWindow . center')

# ---------- WIDGET ----------
# Area input:
#   - Label judul
label_judul = tk.Label(root, text="Aplikasi Produktivitas", font=("Times New Roman", 12, "bold"))
label_judul.pack(pady=10)
#   - Entry
label_tambahtgs = tk.Label(root, text="Masukkan Tugas: ")
label_tambahtgs.pack(pady=5)

entry_tmbhtugas = tk.Entry(root, width=30)
entry_tmbhtugas.pack(ipady=5)
#   - Button "Tambah Tugas"  (command=...)

# Area tampilan:
#   - Listbox (atur height & width supaya cukup besar)
#   - opsional: Scrollbar

# Area tombol aksi (pertimbangkan pakai Frame biar rapi):
#   - Button "Hapus Tugas"
#   - Button "Bersihkan Semua"

root.mainloop()