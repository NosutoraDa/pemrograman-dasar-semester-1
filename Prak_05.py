# Soal
# Menghitung Volume Bangun Ruang Kotak dan Limas

# Inisialisasi
t_pg = int(input("Masukkan Tinggi Persegi: "))
p_pg = int(input("Masukkan Panjang Persegi: "))
l_pg = int(input("Masukkan Lebar Persegi: "))

st_sg = int(input("Masukkan selisih Tinggi Segitiga: "))
sp_sg = int(input("Masukkan selisih Panjang Segitiga: "))

# Menghitung Volume Bangun Ruang Pertama (Kotak)
Volume1 = p_pg * l_pg * t_pg

# Menghitung Volume Bangun Ruang Kedua (Limas)
t_sg = t_pg - st_sg
p_sg = sp_sg - p_pg
l_sg = l_pg

Volume2 = p_sg * l_sg * t_sg

# Menghitung keseluruhan gabungan Bangun Ruang
Volume = Volume1 + Volume2

# Menampilkan Hasil Perhitungan Volume Bangun Ruang
print("Volume bangun ruang =",Volume, "cm3")


