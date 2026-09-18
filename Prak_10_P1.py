nilai = (78, 92, 65, 88, 78, 70, 92, 85, 78, 90)

# Proses Menghitung Jumlah Nilai 78 dan 92 Menggunakan metode count.

x = nilai.count(78)
y = nilai.count(92)

print("Jumlah Kemunculan 78 sebanyak = ", x)
print("Jumlah Kemunculan 92 sebanyak = ", y)

# Proses mencari indeks pertama dari nilai 88 menggunakan method index.

p = nilai.index(88)
print("Indeks dari 88 adalah", p)

# Nilai rata rata dari seluruh elemen tuple (gunakan loop atau sum)

n = sum(nilai) / len(nilai)
print("Nilai Rata-rata = ", n)

# Mencari Nilai tertinggi dan terendah

print("Nilai tertinggi adalah = ", max(nilai))
print("Nilai terendah adalah = ", min(nilai))

# Unpacking mengambil 3 nilai pertama dan di simpan ke variable a b c

# (a, b, c, *_) = nilai
(a, b, c) = nilai[:3]

print(a)
print(b)
print(c)
