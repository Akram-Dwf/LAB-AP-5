nilai = int(input("masukkan nilai tes :"))

if nilai >= 80 :
    print("lolos ke tahap wawancar")


elif nilai >= 65 :
    pengalaman = int(input("masukkan pengelaman kerja(tahun) :"))
    if pengalaman >= 2:
        print("lolos bersyarat")
else:
    print("tidak lolos")