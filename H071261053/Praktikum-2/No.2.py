# #menghitung tarif pengiriman

jarak = float(input("Masukkan jarak pengiriman (dalam km): "))
layanan_express = input("layanan express (ya/tidak): ")
biaya_express = 15000 if layanan_express == "ya" else 0

if jarak < 5:
    tarif_dasar = 10000
elif jarak <=20:
    tarif_dasar = 20000
else:
    tarif_dasar = 35000

total_tarif = tarif_dasar + biaya_express
print(f"total tarif pengiriman: Rp.{total_tarif}")