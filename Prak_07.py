DataNim = ["266151001","266151002","266151003","266151004","266151002"]

laki = []
perempuan = []
# list bisa data duplikat seperti diatas

DataNim[4] = "266151005" # bisa mengubah datalist secara langsung

DataNim.append("266151006") # bisa menambah data dengan list.append

DataNim.remove("266151004") # bisa menghapus data dengan list.remove

for i in range(len(DataNim)): # len perintah untuk menjumlahkan data contoh nya data list ini ada 5 sedangkan i adalah variable counter dari 0
    print(DataNim[i])

for i in range(len(DataNim)): # ini adalah index yaitu memindahkan data dari list 1 ke list 2
    if i <= 2:
        laki.append(DataNim[i])
    elif i > 2:
        perempuan.append(DataNim[i])

print(laki)
print(perempuan)
#print(DataNim) # bisa memilih data yg mau di tampilkan menggunakan [nomor] atau memilih dalam range [0:nomor]