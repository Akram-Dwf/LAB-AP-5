import re

def cek_nim(nim):
    pola = "^H071[0-9]{6}$"
    if re.match(pola, nim):
        return True
    else:
        return False

def cek_email(email):
    pola = r"^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
    if re.match(pola, email):
        return True
    else:
        return False

def cek_telepon(telepon):
    pola = "^[0-9]{10,13}$"
    if re.match(pola, telepon):
        return True
    else:
        return False


print("=== Validasi Data Mahasiswa ===\n")

nim = input("Masukkan NIM      : ")
email = input("Masukkan Email    : ")
telepon = input("Masukkan No. Telp : ")

print("--- Hasil Validasi ---\n")

nim_valid = cek_nim(nim)
email_valid = cek_email(email)
telepon_valid = cek_telepon(telepon)

if nim_valid:
    print("NIM         : Valid")
else:
    print("NIM         : Format NIM tidak valid!")

if email_valid:
    print("Email       : Valid")
else:
    print("Email       : Format email tidak valid!")

if telepon_valid:
    print("No. Telepon : Valid\n")
else:
    print("No. Telepon : Nomor telepon tidak valid!")

if nim_valid and email_valid and telepon_valid:
    print("Data mahasiswa berhasil diverifikasi!")