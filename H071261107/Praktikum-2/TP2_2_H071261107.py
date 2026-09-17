jarak = int(input("masukkan jarak : "))
LayananExpress = input("Layanan Express (ya/tidak) : ")
totaltarifpengiriman = 0

if jarak >= 20:
    totaltarifpengiriman = 35000
elif jarak >= 5:
    totaltarifpengiriman = 20000
elif jarak >= 0: 
    totaltarifpengiriman = 10000
else:
    print("jarak tidak valid")

totaltarifpengiriman += 15000 if LayananExpress == "ya" else 0

print(totaltarifpengiriman)
    

