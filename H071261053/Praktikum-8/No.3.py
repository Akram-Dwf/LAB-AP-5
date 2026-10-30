import re

def bersihkan_no_telp(no_telp):
    pattern = r'[\s-]'
    return re.sub(pattern, "", no_telp)

def validasi_no_telp(no_telp):
    pattern = r'^08\d{8,11}$'

    if re.match(pattern, no_telp):
        return True
    else:
        return False

data_telepon = []
telepon_valid = []

print("\n=== Pembersihan Nomor Telepon ===")

jumlah_data = int(input("Masukkan jumlah data: "))
for i in range(jumlah_data):
    no_telp = input(f"Nomor ke-{i + 1}: ")
    no_bersih = bersihkan_no_telp(no_telp)

    if validasi_no_telp(no_bersih):
        status = "Valid"
        telepon_valid.append(no_bersih)
    else:
        status = "Tidak valid"

    data_telepon.append([no_telp, no_bersih, status])

print("\n--- Hasil Pembersihan ---")

for i in range (len(data_telepon)):
    print(f"\nData {i + 1}: ")
    print("Sesudah: ", data_telepon[i][0])
    print("Setelah: ", data_telepon[i][1])
    print("Status : ", data_telepon[i][2])

print("Jumlah nomor valid: ", len(telepon_valid))


    
