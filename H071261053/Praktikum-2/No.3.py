#rekrutmen karyawan baru

nilai_tes = float(input("masukkan nilai tes: "))
pengalaman_kerja = float(input("masukkan pengalaman kerja (tahun): "))

if nilai_tes >= 80:
    print("lolos ke tahap wawancara")
elif nilai_tes >= 65 and pengalaman_kerja >= 2:
    print("lolos bersyarat")
else:
    print("tidak lolos")