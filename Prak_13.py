# menu makanan
import os

def menu_warteg():
    os.system('cls')
    print("=======MENU WARTEG=======")
    print("====== MENU Makanan======")
    print(" 1. Nasi Goreng Rp. 15.000")
    print(" 2. Mie Goreng Rp. 12.000")
    print(" 3. Ayam Goreng Rp. 20.000")
    print("====== MENU Minuman======")
    print(" a. Es Teh Rp. 5.000")
    print(" b. Es Jeruk Rp. 6.000")
    print(" c. Air Mineral Rp. 3.000")
    print("----------------------------")

def datamakanan(x):
    global jmlmak,nmk

    if x=="1":
        nmk = "Nasi Goreng"
        hmk = 15000

    if x=="2":
        nmk = "Mie Goreng"
        hmk = 12000

    if x=="3":
        nmk = "Ayam Goreng"
        hmk = 20000

    jmlmak = jmlmak + 1

    dtmak[jmlmak] = {}

    dtmak[jmlmak]["nama"] = nmk 
    dtmak[jmlmak]["harga"] = hmk

    for key, value in dtmak.items():
        print(f"{key}. {value}")

def dataminuman(y):
    global jmlmin,nmk

    if y=="a":
        nmn = "Es Teh"
        hmn = 5000

    if y=="b":
        nmn = "Es Jeruk"
        hmn = 6000

    if y=="c":
        nmn = "Air Mineral"
        hmn = 3000

    jmlmin = jmlmin + 1

    dtmin[jmlmin] = {}

    dtmin[jmlmin]["nama"] = nmn
    dtmin[jmlmin]["harga"] = hmn

    for key, value in dtmin.items():
        print(f"{key}. {value}")


def main():
    n = True
    while n==True:
        menu_warteg()
        print("Silahkan pilih menu makanan yang diinginkan: ")
        item = input().lower()
        if item == '1' or item == '2' or item == '3':
            print("Pesanan Makanan")
            datamakanan(item)

        if item == 'a' or item == 'b' or item == 'c':
            print("Pesanan Minuman")
            dataminuman(item)

        print("Apakah masih ada pilihan menu yang ingin dipesan? (y/n): ")
        pilihan = input().lower()
            
        if pilihan == 'n':
            n = False

            totalmak = sum(item["harga"] for item in dtmak.values())
            totalmin = sum(item["harga"] for item in dtmin.values())
            totalmakmin = totalmak + totalmin

            print(" Total Harga dari Makanan adalah : Rp. ", totalmak)
            print(" Total Harga dari Minuman adalah : Rp. ", totalmin)
            print(" Total Harga dari Kedua Makanan dan Minuman adalah : Rp.", totalmakmin)

            print("Terima kasih telah memesan warteg kami!")

if __name__ == "__main__":
    global dtmin, jmlmin

    dtmak = {}
    jmlmak = 0

    dtmin = {}
    jmlmin = 0
    
    main()

