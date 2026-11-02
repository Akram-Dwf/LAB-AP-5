import re

POLA = {
    "NIM": r"H071[0-9]{6}",
    "Email": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+",
    "No. Telepon": r"[0-9]{10,13}",
}
PESAN = {
    "NIM": "Format NIM tidak valid!",
    "Email": "Format email tidak valid!",
    "No. Telepon": "Nomor telepon tidak valid!",
}


def validasi(jenis, data):
    return re.fullmatch(POLA[jenis], data) is not None


print("=== Validasi Data Mahasiswa ===\n")
data = {
    "NIM": input("Masukkan NIM      : ").strip(),
    "Email": input("Masukkan Email    : ").strip(),
    "No. Telepon": input("Masukkan No. Telp : ").strip(),
}

print("\n--- Hasil Validasi ---")
semua_valid = True
for jenis, isi in data.items():
    if validasi(jenis, isi):
        print(jenis.ljust(11) + " : Valid")
    else:
        print(jenis.ljust(11) + " : " + PESAN[jenis])
        semua_valid = False

if semua_valid:
    print("\nData mahasiswa berhasil diverifikasi!")