# dictionary
thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1964
}
# cara memamnggil nilai
#x = thisdict.keys()
#x = thisdict.values()

thisdict["color"] = "white"
# menampilkan data per key
# print(thisdict["brand"])
# print(x)

for x,y in thisdict.items():
    print(x,y)