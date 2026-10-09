jarak=int(input("Masukkan jarak pengiriman (KM):"))
layanan_express=input("layanan express(Ya/tidak):")

if jarak <5:
    tarif=10000 
elif jarak <=20:
    tarif=20000
elif jarak <15:
    tarif = 15000

else:
    tarif=35000

biaya_tambahan=15000 if layanan_express == "Ya" else 0
tarif= tarif + biaya_tambahan

print("Total tarif pengiriman:Rp",tarif)