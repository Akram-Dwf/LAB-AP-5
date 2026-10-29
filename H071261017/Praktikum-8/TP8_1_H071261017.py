import re

def validasi_nim(nim):
    pattern = r"H071\d{6}"
    return re.fullmatch(pattern, nim) is not None

def validasi_email(email):
    pattern = r"[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]+"
    return re.fullmatch(pattern, email) is not None

def validasi_telepon(telepon):
    pattern = r"\d{10,13}"
    return re.fullmatch(pattern, telepon) is not None

print("=== Validasi Data Mahasiswa ===\n")

nim = input("Masukkan NIM       : ")
email = input("Masukkan Email     : ")
telepon = input("Masukkan No. Telp : ")

nim_ok = validasi_nim(nim)
email_ok = validasi_email(email)
telepon_ok = validasi_telepon(telepon)

print("\n--- Hasil Validasi ---")
print("NIM         :", "Valid" if nim_ok else "Tidak valid")
print("Email       :", "Valid" if email_ok else "Tidak valid")
print("No. Telepon :", "Valid" if telepon_ok else "Tidak valid")

if nim_ok and email_ok and telepon_ok:
    print("\nData mahasiswa berhasil diverifikasi!")
else:
    if not nim_ok:
        print("Format NIM tidak valid!")
    if not email_ok:
        print("Format email tidak valid!")
    if not telepon_ok:
        print("Nomor telepon tidak valid!")