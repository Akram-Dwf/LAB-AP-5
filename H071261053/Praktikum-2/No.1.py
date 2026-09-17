#klasifikasi tingkat kepedasan

persentase_cabai = float(input("Masukkan persentase cabai : "))

if persentase_cabai < 0:
    print("input tidak valid")
elif persentase_cabai <= 10 :
    print("level aman")
elif persentase_cabai <=40 :
    print("level sedang")
elif persentase_cabai <= 70 :
    print("level pedas")
else:
    print("level ekstrem")

