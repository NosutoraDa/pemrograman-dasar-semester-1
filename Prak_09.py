print ("Data Nilai Matakuliah")
print ("=====================")

mk = ()
nilaimk = ()

lsmk = []
lsnilaimk = []

jmlmk = int(input("Masukkan Jumlah Data Matakuliah? = "))
i = 1
while i <= jmlmk:
    a = input("Matakuliah = ")
    b = int(input("Nilai Matakuliah = "))

    lsmk.append(a)
    lsnilaimk.append(b)

    i = i + 1

mk = tuple(lsmk)
nilaimk = tuple(lsnilaimk)

print(mk)
print(nilaimk)

print("Mencari Nilai Matakuliah")
cari = input("Matakuliah Apa yang mau di cari? = ")

i = 0
while i < jmlmk:
    if cari == mk[i]:
        hasilcari = nilaimk[i]

    i = i + 1

print("Nilai Matakuliah = ", hasilcari)