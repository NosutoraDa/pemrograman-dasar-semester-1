# Menginisialisasi dictionary stok buah
stok_buah = {
    "Apel" : 10,
    "Jeruk" : 5,
    "Mangga" : 12
}

# mengintegrasikan loop dan items() untuk menampilkan semua key dan value
for x in stok_buah.items():
    stok_buah["Jeruk"] = 15

# Menampilkan hasil
    print(x)