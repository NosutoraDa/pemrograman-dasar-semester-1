# Menampilkan Tuple di Tuples
mahasiswa = (
    ("Andi", "TK", 3.75),
    ("Budi", "TI", 3.20),
    ("Citra", "TRK", 3.90),
    ("Dedi", "TK", 3.40),
    ("Eka", "TI", 3.65)
)

for i in range (len(mahasiswa)):
    (nama, prodi, ipk) = mahasiswa[i]
    print(f"Nama = {nama}, Prodi = {prodi}, IPK =  {ipk:.2f}")

# Mencari IPK tertinggi dan terendah

ipk_tertinggi = 0
nama_tertinggi = ""
for nama, prodi, ipk in mahasiswa:
    if ipk > ipk_tertinggi:
        ipk_tertinggi = ipk
        nama_tertinggi = nama

print("Mahasiswa tertinggi = ", nama_tertinggi, "dengan nilai = ", ipk_tertinggi)
# Mencari IPK tertinggi dan terendah

#ipk_tertinggi = max(mahasiswa, key=lambda item: item[2])
#ipk_terendah = min(mahasiswa, key=lambda item: item[2])

#print(f"IPK tertinggi adalah = {ipk_tertinggi}")
#print(f"IPK terendah adalah = {ipk_terendah}")

# Mengurutkan Mahasiswa berdasarkan IPK dalam bentuk tuple baru

urutdata = tuple(sorted(mahasiswa, key=lambda item: item[2], reverse=True))

print("Data Mahasiswa yang di urutkan secara descending: ")
for x in range(len(urutdata)):
    print("Nama: ", urutdata[x][0], "Prodi: ", urutdata[x][1], "IPK: ", urutdata[x][2])
print("Data Mahasiswa yang di urutkan secara descending")

# Menghitung rata rata IPK

totalipk = sum(i[2] for i in mahasiswa)
rata2ipk = totalipk / len(mahasiswa)

print(f"Rata rata ipk mahasiswa: {rata2ipk:.2f}")