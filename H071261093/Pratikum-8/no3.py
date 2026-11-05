import re

data_nomor = []

def Validasi(nomor):
    validasi_nomor = r"^[08|+62]\d{9,11}$"
    pola = r"\s|-"
    nomorke = 1
    data_valid = 0
    for i in nomor:
        hasil_bersih = re.sub(pola, "", i)
        hasil_validasi = re.match(validasi_nomor, hasil_bersih)

        print(f"\nData {nomorke}:")
        print("Sebelum".ljust(10) + f": {i}")
        print("Sesudah".ljust(10) + f": {hasil_bersih}")

        if hasil_validasi:
            print("Status".ljust(10) + ": Valid")
            data_valid += 1
        else:
            print("Status".ljust(10) + ": Tidak valid")

        nomorke += 1

    print(f"\nJumlah Nomor valid: {data_valid}")

print("=== Pembersihan Data Nomor Telepon ===\n")
while True:
    try:
        jumlah = int(input("Masukkan jumlah data: "))
        if jumlah > 0:
            break
        print("Jumlah harus lebih dari 0!")
    except:
        print("Masukkan angka yang benar!")

for i in range(1, jumlah + 1):
    nomor = input(f"\nNomor ke-{i}: ").strip()
    data_nomor.append(nomor)

Validasi(data_nomor)