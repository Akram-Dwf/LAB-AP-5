import re

def validasi_username(username):
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]{4,11}$'
    if re.match(pattern, username):
        return True
    else:
        return False

print("\n=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")

username_valid = []
while True:
    username = input("Masukkan username: ")

    if username == 'SELESAI'.lower():
        break

    if validasi_username(username):
        username_valid.append(username)
        hasil = "Username tersedia"
    else:
        hasil = "Username tidak valid!"

    print (hasil)

print("=== Rekapitulasi ===")
print("username valid: ")

for i in range (len(username_valid)):
    print(str(i + 1) + "." + username_valid[i])

print("Jumlah username valid: ", len(username_valid))
 




