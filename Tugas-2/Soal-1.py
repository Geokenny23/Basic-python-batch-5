semuakontak = []
kontak = []

def menu():
    print("----menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

def tampilkankontak():
    print("Daftar Kontak: ")
    for  kontak in semuakontak:
        print("Nama : " + kontak["nama"])
        print("No. Telepon : " + kontak["telpon"])

def tambahkontak():
    nama = str(input("\nMasukkan Data\nNama : "))
    telpon = str(input("No Telepon : "))      
    kontak = {
         "nama" : nama,
         "telpon" : telpon,
    }
    semuakontak.append(kontak)

    print("Kontak berhasil ditambahkan")

print("Selamat datang!!!")
while True:
    menu()
    pilihan = int(input("Pilih menu: "))
    if pilihan == 1:
        tampilkankontak()
    elif pilihan ==  2:
        tambahkontak()
    elif pilihan == 3:
        print("program selesai, sampai  jumpa")
        break
    else:
       print("menu tidak tersedia, silahkan menginput No. yang benar")
       print("-------------------------------------------------------")


    





# print("Selamat datang!")
      

# while True:
#     print("---Menu---")
#     print("1.  Daftar Kontak")
#     print("2.  Tambah Kontak")
#     print("3.  Keluar")
#     pilih = int(input("Pilih menu: "))
#     if  pilih == 1:   
#         #print("Amal")
#         #print("0834267588")
#         Nama = {
#         "nama" : "Amal"
#         "No. telepon" : "0834267588"
#         }
#             }
#         daftar_kontak = [Nama].append(x)
#         print(daftar_kontak)
#         #print(Nama)
#         #print(Nomor)
#         #print(x)
#         #print(y)
#     elif pilih == 2: 
#         x = str(input("Nama: "))
#         y = int(input("No. Telepon: "))
#         print("Kontak berhasil ditambahkan")


#     elif pilih == 3:
#         print("program selesai, sampai  jumpa")
#         break
#     else:
#         print("menu tidak tersedia, silahkan menginput No. yang benar")
#         print("------------------------------------------------------")
        
    






