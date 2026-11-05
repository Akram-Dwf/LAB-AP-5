import re


print("=== Pembersihan Data Nomor Telepon ===\n")
jumlah = input("Masukkan jumlah data: ")
while not re.fullmatch(r"[1-9][0-9]*", jumlah):
    print("Jumlah harus berupa angka lebih dari 0!")
    jumlah = input("Masukkan jumlah data: ")
jumlah = int(jumlah)
print()

data = []
valid = []
for i in range(1, jumlah + 1):
    sebelum = input("Nomor ke-" + str(i) + ": ")
    print()
    sesudah = re.sub(r"[ -]", "", sebelum)
    status = re.fullmatch(r"[08|+62]\d{10,13}", sesudah) is not None
    data.append((sebelum, sesudah, status))
    if status:
        valid.append(sesudah)

print("--- Hasil Pembersihan ---")
for i, (sebelum, sesudah, status) in enumerate(data, 1):
    print("\nData " + str(i) + ":")
    print("Sebelum : " + sebelum)
    print("Sesudah : " + sesudah)
    print("Status  : " + ("Valid" if status else "Tidak valid"))

print("\nJumlah nomor valid: " + str(len(valid)))