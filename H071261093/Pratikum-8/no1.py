import re

def validasi_nim(nim):
    pola = r"^H071\d{6}$"
    hasil = re.match(pola, nim)
    if hasil:
        return True
    else:
        return False

def validasi_email(email):
    pola = r"^\w+@\w+\.\w+"
    hasil = re.match(pola, email)
    if hasil:
        return True
    else:
        return False

def validasi_telepon(telp):
    pola = r"^\d{10,13}$"
    hasil = re.match(pola, telp)
    if hasil:
        return True
    else:
        return False

print("\n=== Validasi Data Mahasiswa ===")

nim = input("Masukkan NIM".ljust(18) + ": ").strip()
email = input("Masukkan Email".ljust(18) + ": ").strip()
telp = input("Masukkan No. Telp".ljust(18) + ": ").strip()

nim_valid = validasi_nim(nim)
email_valid = validasi_email(email)
telp_valid = validasi_telepon(telp)

print("\n--- Hasil Validasi ---")

if nim_valid:
    print("NIM".ljust(15) + ": Valid")
else:
    print("NIM".ljust(15) + ": Tidak valid")
    print("Format NIM tidak valid!")

if email_valid:
    print("Email".ljust(15) + ": Valid")
else:
    print("Email".ljust(15) + ": Tidak valid")
    print("Format email tidak valid!")

if telp_valid:
    print("No. Telepon".ljust(15) + ": Valid")
else:
    print("No. Telepon".ljust(15) + ": Tidak valid")
    print("Nomor telepon tidak valid!")

if nim_valid and email_valid and telp_valid:
    print("\nData mahasiswa berhasil diverifikasi!")