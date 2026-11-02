import re

def bersihkan(nomor):
    hasil = re.sub("[ -]", "", nomor)
    return hasil

def cek_nomor(nomor):
    pola = "^[0-9]{10,13}$"
    if re.match(pola, nomor):
        return True
    else:
        return False

print("=== Pembersihan Data Nomor Telepon ===\n")

jumlah = int(input("Masukkan jumlah data: "))

data_sebelum = []
data_sesudah = []
nomor_valid = []

for i in range(jumlah):
    nomor = input("Nomor ke-" + str(i + 1) + ": ")
    print()

    nomor_bersih = bersihkan(nomor)
    data_sebelum.append(nomor)
    data_sesudah.append(nomor_bersih)

    if cek_nomor(nomor_bersih):
        nomor_valid.append(nomor_bersih)

print("--- Hasil Pembersihan ---\n")

for i in range(jumlah):
    print("Data " + str(i + 1) + ":")
    print("Sebelum :", data_sebelum[i])
    print("Sesudah :", data_sesudah[i])

    if cek_nomor(data_sesudah[i]):
        print("Status  : Valid\n")
    else:
        print("Status  : Tidak valid\n")

print("Jumlah nomor valid:", len(nomor_valid))