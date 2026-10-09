nilai=int(input("Masukkan nilai:"))


if nilai >=80:
    print("Lolos ke Tahap Wawancara")

elif nilai >=65:
    pengalaman=int(input("Masukkan pengalaman kerja(Tahun):"))
    if pengalaman >=2:  
        print("Lolos Bersyarat")
    else:
        print("Pelamar dinyatakaan tidak lolos")

else:
    print("Pelamar dinyatakan tidak lolos")