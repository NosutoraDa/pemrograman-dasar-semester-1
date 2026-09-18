# Soal
# Menghitung Luas Bangun Ruang Kotak Limas

# Inisialisasi
t_pg = int(input("Masukkan Tinggi Persegi: "))#25
p_pg = int(input("Masukkan Panjang Persegi: "))#14
l_pg = int(input("Masukkan Lebar Persegi: "))#12

st_sg = int(input("Masukkan selisih Tinggi Segitiga: "))#14
sp_sg =  int(input("Masukkan selisih Panjang Segitiga: "))#20
t_sg = int(input("Masukkan selisih Tinggi Segitiga: "))#11
gm_sg = float(input("Masukkan selisih Garis Miring Segitiga: "))#13.60
a_sg = int(input("Masukkan selisih Alas Segitiga: "))#6

garis_miring = (a_sg**2 + t_sg**2)**0.5
alas_segitiga = (sp_sg - p_pg)
tinggi_segitiga = (t_pg - st_sg)

# Menghitung Luas Permukaan Kotak
pg1 = p_pg * l_pg
pg2 = t_pg * l_pg
pg3 = p_pg * t_pg
pg4 = p_pg * t_pg
pg5 = p_pg * l_pg
pg6 = l_pg * st_sg

# Menghitung Luas Permukaan Segitiga
sg1 = 0.5 * a_sg * t_sg
sg2 = 0.5 * a_sg * t_sg
sg3 = gm_sg * l_pg
sg4 = (sp_sg - p_pg) * (l_pg)

# Menghitung Luas Keseluruhan
Luas_Seluruh = pg1 + pg2 + pg3 + pg4 + pg5 + pg6 + sg1 + sg2 + sg3 + sg4

# Menampilkan Hasil Perhitungan Luas
print("Luas Keseluruhan gabungan bangun ruang = ",Luas_Seluruh, "cm2")
