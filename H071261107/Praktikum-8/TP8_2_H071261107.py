
import re

def cekusername(username):
    pattern = '^[a-zA-Z][a-zA-Z0-9_]{4,11}$'
    result = re.match(pattern, username)
    if result:
        return True
    else:
        return False

daftarusername = []

while True:
    username = input("Masukkan username (SELESAI untuk berhenti): ")
    if username == "SELESAI":
        break
    if cekusername(username):
        print("Username tersedia.")
        daftarusername.append(username)
    else:
        print("Username tidak valid!")

print("\n--- Daftar Username Valid ---")

for username in daftarusername:
    print(username)

print("Jumlah username valid:", len(daftarusername))
