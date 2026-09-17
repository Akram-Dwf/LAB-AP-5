persen = int(input("Masukkan persentase cabai: "))

if persen < 0:
    print("Input tidak valid")
elif persen <= 10:
    print("Level Aman")
elif persen <= 40:
    print("Level Sedang")
elif persen <= 70:
    print("Level Pedas")
else:
    print("Level Ekstrem")


