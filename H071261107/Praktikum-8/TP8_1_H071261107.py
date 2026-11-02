import re

def ceknim(nim):
    pattern = '^H071[0-9]{6}$'
    result = re.match(pattern, nim)
    if result:
        print(f"{'NIM':15} : Valid")
        return True
    else:
        print(f"{'NIM':15} : Tidak Valid")
        return False

def cekemail(email):
    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    result = re.match(pattern, email)
    if result:
        print(f"{'EMAIL':15} : Valid")
        return True
    else:
        print(f"{'EMAIL':15} : Tidak Valid")
        return False

def ceknotelf(notelf):
    pattern = '^[0-9]{10,13}$'
    result = re.match(pattern, notelf)
    if result:
        print(f"{'NOMOR TELEFON':15} : Valid")
        return True
    else:
        print(f"{'NOMOR TELEFON':15} : Tidak Valid")
        return False
    
print ("=== Validasi Data Mahasiswa ===")
print("")
nim = input(f"{'MASUKKAN NIM':20}: ")
email = input(f"{'MASUKKAN EMAIL MHS':20}: ")
notelf = input(f"{'MASUKKAN NO. Telp':20}: ")
print("")
print("--- Hasil Validasi ---")
hasilnim = ceknim(nim)
hasilemail = cekemail(email)
hasilnotelf = ceknotelf(notelf)

if hasilnim and hasilemail and hasilnotelf:
    print("\nData Mahasiswa berhasil diverifikasi!")
else:
    print("\nData Mahasiswa Belum Valid")


