#import smtplib supaya guna mengconnect python ke gmail
import smtplib as smp

#menulis/log in ke gmail anda(gmail pengirim)
gmailaddress = input("silahkan input gmail anda? \n ")
gmailpassword = input("passwordnya apa? \n  ")

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
print(" \n pesan berhasil dikirim!")

#untuk membuka file dan melihat alamat email yang telah terkirim
f = open("receiver_list.txt", "a")
f.write(mailto)
f.write("\n")
f.close()

mailServer.quit()

#sumber
#https://youtu.be/JRCJ6RtE3xU
#https://youtu.be/u2O9bPyHNOE
#https://youtu.be/sXjpkcF7rPQ