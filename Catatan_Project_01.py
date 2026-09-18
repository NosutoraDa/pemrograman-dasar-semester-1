# inisialisasi jumlah data mahasiswa
jmlMHS = int(input("Masukkan Jumlah Data Mahasiswa: "))

# deklarasi kan variable nama dan nilai
nama = []
nilai = []

# memasukkan data mahasiswa sesuai jumlah mahasiswa
for i in range(jmlMHS):
    nm = input("Nama Mahasiswa: ")
    nama.append(nm)
    nl = int(input("Masukkan Nilai: "))
    nilai.append(nl)

# menampilkan data dan jumlah mahasiswa
print("Jumlah data Mahasiswa", jmlMHS)

for i in range(jmlMHS):
    print(i+1," Nama ", nama[i])
    print("     Nilai ", nilai[i])

# menambahkan fitur pencarian data mahasiswa
cari = input("Masukkan nama Mahasiswa yang dicari: ")

x=0 # fungsi x adalah untuk menjebak data yang mana ada dan yang mana tidak ada, namanya algoritma
for i in range(jmlMHS):
    x=x+1
    if cari == nama[i]:
        print("Nilai Mahasiswa = ",nilai[i])
        x=0
        break;
    else:
        x=x+1

if x > 0:
    print("Data Mahasiswa tidak ketemu")

# menghitung rata rata nilai mahasiswa
totnil = 0
for i in range(jmlMHS):
    totnil = totnil + nilai[i]

rata2 = totnil / jmlMHS

print("Rata-rata nilai Mahasiswa = ",rata2)

# mencari nilai tertinggi dan nilai terendah mahasiswa
nmax = 0
nmmax = ""
nmin = 100 # harus nilai tertinggi jika tidak maka 0 akan menjadi terendah
nmmin = ""

for i in range(jmlMHS):
    if nmax <= nilai[i]:
        nmax = nilai[i]
        nmmax = nama[i]
    if nmin >= nilai[i]:
        nmin = nilai[i]
        nmmin = nama[i]

print("Nama dengan nilai tertinggi adalah = ", nmmax , "dengan nilai", nmax)
print("Nama dengan nilai terendah adalah = ", nmmin , "dengan nilai", nmin)

# mengurutkan data mahasiswa
print(nama.sort())
print(nilai.sort())

