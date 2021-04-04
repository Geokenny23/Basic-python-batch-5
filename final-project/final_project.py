#import smtplib supaya guna mengconnect python ke gmail
import smtplib as smp
import getpass

def menu():
    print("----menu---")
    print("1. Kirim E-mail")
    print("2. Keluar")

def menu2() :
    print("apakah anda ingin mengirim lagi?(y/t)")

print("Selamat datang!!!")
while True:
    menu()
    pilihan = int(input("Pilih menu: "))
    if pilihan == 1:
        #menulis/log in ke gmail anda(gmail pengirim)
        gmailaddress = input("silahkan input gmail anda? \n ")
        gmailpassword = getpass.getpass(prompt= "password:  ")
       

        mailServer = smp.SMTP('smtp.gmail.com' , 587)          #untuk mengirim email, dibutuhkan server
        mailServer.starttls()

        #code ini berfungsi untuk meng log in akun gmail anda 
        mailServer.login(gmailaddress , gmailpassword)

        #menulis email penerima
        mailto = input("alamat email yang ingin dikirim? \n ")

        #menulis subject dan body yang akan menjadi pesan 
        sub = input("subject?\n")
        body = input("message? \n ")
        msg = f'subject: {sub}\n\n{body}'                     #menggunakan f string agar penulisannya  berformat

        #mengirimkan email
        mailServer.sendmail(gmailaddress, mailto , msg)
        print("Pesan sedang dikirim...\n")
        print(" \n pesan berhasil dikirim!\n")

        #untuk membuka file dan melihat alamat email yang telah terkirim
        f = open("receiver_list.txt", "a")
        f.write(mailto)
        f.write("\n")
        f.close()

        mailServer.quit()


    elif pilihan == 2:
        break
    else:
        print("Silahkan input no yang benar")
        print("++++++++++++++++++++++++++++")
        continue
  

#sumber
#https://youtu.be/JRCJ6RtE3xU
#https://youtu.be/u2O9bPyHNOE
#https://youtu.be/sXjpkcF7rPQ