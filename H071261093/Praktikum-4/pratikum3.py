def countdown(waktu):
    if waktu == 0:
        print(waktu)
        print("LUNCURKANNNNNN!")
    else:
        print(waktu)
        countdown(waktu - 1)

while True:
    try:
        hitung_mundur = int(input("Masukkan angka awal hitung mundur: "))
        if hitung_mundur < 0:
            print("Angka tidak boleh negatif")
            continue
        break
    except:
        print("Input yang anda masukkan tidak valid")
        continue

countdown(hitung_mundur)