import re

def cek_nim(nim):
    pattern = "^H071[0-9]{6}"
    if re.match(pattern, nim):
        return True
    else:
        return False
def cek_email(email):
    pattern = r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]"
    if re.match(pattern, email):
        return True
    else:
        return False
def cek_telp(telp):
    pattern = "^[08|+62]+\d{10,13}"
    if re.match(pattern, telp):
        return True
    else:
        return False

print('=== Validasi Data Mahasiswa ===')
nim =    input('Masukkan NIM      : ')
email =  input('Masukkan Email    : ')
telp =   input('Masukkan No. Telp : ')

nim_ril = cek_nim(nim)
email_ril = cek_email(email)
telp_ril = cek_telp(telp)

print('--- Hasil Validasi ---')
if nim_ril:
    print('NIM      : Valid')
else:
    print('NIM      : Tidak Valid')

if email_ril:
    print('Email    : Valid')
else:
    print('Email    : Tidak valid')

if telp_ril:
    print('No. Telp : Valid')
else:
    print('No. Telp : Tidak valid')    

if nim_ril and email_ril and telp_ril:
    print('Data mahasiswa berhasil diverifikasi!')