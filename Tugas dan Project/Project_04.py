# Menginialisasi Sets untuk User A dan B
User_A = {"Membaca", "Coding", "Berenang", "Catur"}
User_B = {"Futsal", "Coding", "Catur", "Melukis"}

# Hobi yang ditekuni oleh kedua pengguna (Intersection)
hobi_sama = User_A.intersection(User_B)

# Hobi dari Kedua Pengguna (Union)
hobi_beda = User_A.union(User_B)

# Menampilkan Hasil dari Intersection dan Union
print("Hobi dari kedua Users yang sama adalah : ", hobi_sama)
print("Hobi keseluruhan dari kedua users adalah : ", hobi_beda)
