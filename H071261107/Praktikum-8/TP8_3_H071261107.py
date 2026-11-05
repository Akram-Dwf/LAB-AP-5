
import re

def ceknotelf(notelf):
    pattern = '^[0-9]{10,13}$'
    result = re.match(pattern, notelf)
    if result:
        return True
    else:
        return False

datasebelum = []
datasesudah = []

jumlahdata = int(input("Masukkan jumlah data nomor telepon: "))

for i in range(jumlahdata):
    notelf = input("Masukkan nomor telepon: ")
    datasebelum.append(notelf)

    notelfbersih = re.sub(r'[ -]', '', notelf)

    if ceknotelf(notelfbersih):
        datasesudah.append(notelfbersih)
    else:
        print("Nomor telepon tidak valid!")

print("\n--- Data Sebelum Dibersihkan ---")
for notelf in datasebelum:
    print(notelf)

print("\n--- Data Setelah Dibersihkan (Valid) ---")
for notelf in datasesudah:
    print(notelf)

print("\nJumlah nomor valid:", len(datasesudah))
