import re

def cek_username(username):
    pola = "^[a-zA-Z][a-zA-Z0-9_]{4,11}$"
    if re.match(pola, username):
        return True
    else:
        return False

username_valid = []

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.\n")

username = ""
while username != "SELESAI":
    username = input("Masukkan username: ").upper()

    if username == "SELESAI":
        break

    if cek_username(username):
        print("Username tersedia.")
        username_valid.append(username)
    else:
        print("Username tidak valid!")



print()
print("=== Rekapitulasi ===")
print("Username valid:")

nomor = 1
for nama in username_valid:
    print(f'{str(nomor) + '. ' + nama.lower()}')
    nomor = nomor + 1

print()
print("Jumlah username valid:", len(username_valid))