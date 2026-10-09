jarak = int(input("masukkan jarak pengiriman (km) :"))
express = input("layanan express (ya/tidak) :")

if jarak >= 0 and jarak <= 5:
    jarak = 10000
elif jarak <=20:
    jarak = 20000
else:
    jarak = 35000

layanan = 15000 if express == "ya" else 0
tarif = jarak + layanan
print("tarif pengiriman: Rp", tarif )


