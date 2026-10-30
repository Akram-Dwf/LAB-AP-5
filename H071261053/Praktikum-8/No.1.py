import re

def validasi_nim(nim):
   pattern = r'^H071\d{6}$'
   if re.match(pattern, nim):
      return True
   else:
      return False

def validasi_email(email):
   pattern = r'^[a-zA-Z0-9]+@+[a-zA-Z]+\.[a-zA-Z]{2,}$'
   if re.match(pattern, email):
      return True
   else:
      return False

def validasi_no_telepon(no_telp):
   pattern = r'^\d{10,13}$'
   if re.match(pattern, no_telp):
      return True
   else:
      return False

print("\n=== Validasi Data Mahasiswa ===")

nim = input("Masukkan NIM        : ")
email = input("Masukkan Email      : ")
no_telp = input("Masukkan No. Telp   : ")

hasil_nim = validasi_nim(nim)
hasil_email = validasi_email(email)
hasil_no_telp = validasi_no_telepon(no_telp)

print("\n=== Hasil Validasi ===")

if hasil_nim:
   print("NIM           : Valid")
else:
   print("NIM           : Format NIM tidak valid!")

if hasil_email:
   print("Email         : Valid")
else:
   print("Email         : Format email tidak valid!")

if hasil_no_telp:
   print("No. Telepon   : Valid")
else:
   print("No. Telepon   : No. Telepon tidak valid!")

if hasil_nim and hasil_email and hasil_no_telp:
   print("\n Data mahasiswa berhasil diverifikasi!")
