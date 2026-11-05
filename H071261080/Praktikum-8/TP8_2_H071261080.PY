import re


def username_valid(nama):
    return re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{4,11_}", nama) is not None


valid = []
print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.\n")

while True:
    nama = input("Masukkan username: ")
    if nama == "SELESAI":
        break
    if username_valid(nama):
        print("Username tersedia.\n")
        valid.append(nama)
    else:
        print("Username tidak valid!\n")

print("\n=== Rekapitulasi ===")
print("Username valid:")
for nomor, nama in enumerate(valid, 1):
    print(str(nomor) + ". " + nama)
print("\nJumlah username valid: " + str(len(valid)))