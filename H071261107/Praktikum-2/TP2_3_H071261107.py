nilai = int(input("masukkan nilai tes : "))
pengalaman = int(input("masukkan pengalaman kerja (tahun) : "))

if nilai <= 79:
    if pengalaman >=2 and nilai >= 65:
        print("Lolos bersyarat")
    else:
        print("tidak lolos")
else:
    print(" lolos")
