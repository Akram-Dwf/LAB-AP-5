jarak = int(input("Masukkan jarak pengiriman (km): "))
express = input("Layanan express (ya/tidak): ").lower()

if jarak < 0:
    print("Input tidak valid")
else:
    if jarak < 5:
        tarif = 10000
    elif jarak <= 20:
        tarif = 20000
    else:
        tarif = 35000

total = (tarif + 15000) if express == "ya" else tarif

print("Total tarif pengiriman: Rp", total)