a = "Selamat datang  di program ini"
b = "Silahkan mmenginput nilai kalian"
c = input("Nilai teori: ")
teori = float(c)
d = input("Nilai Praktek: ")
praktek = float(d)
e = "Selamat, anda lulus!"
f = "Anda harus mengulang ujian praktek"
g = "Anda harus mengulang ujian teori"
h = "Anda harus mengulangi ujian teori dan praktek"

if teori >= 70.0 and praktek >= 70.0 :
    print (e)
if teori >= 70.0 and praktek <= 70.0 :
    print (f)
elif teori <= 70.0 and praktek >= 70.0 :
    print (g)
else:
    print (h)

