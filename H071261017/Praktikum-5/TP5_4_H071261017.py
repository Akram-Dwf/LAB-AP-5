def deteksi_anomali_email(email):
    error = []

    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return error

    local, domain = email.split("@")

    if local == "" or domain == "":
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if " " in email:
        error.append("Tidak boleh mengandung spasi.")

    if local.startswith(".") or local.endswith(".") or ".." in local:
        error.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

    if "." not in domain:
        error.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    akhir = email.lower()
    if not (akhir.endswith(".com") or akhir.endswith(".id") or akhir.endswith(".ac.id")):
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return error

def cetak_daftar(daftar_email_valid, karakter_border):
    terpanjang = 0
    for email in daftar_email_valid:
        if len(email) > terpanjang:
            terpanjang = len(email)

    lebar = terpanjang + 2             
    garis = "+" + karakter_border * lebar + "+"

    hasil = garis + "\n"
    for email in daftar_email_valid:
        hasil = hasil + "| " + email.ljust(terpanjang) + " |\n"
    hasil = hasil + garis
    return hasil

print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")
if border == "":
    border = "="

print("\nKetik 'tutup' untuk mengakhiri masukan dan mencetak email.")
daftar_valid = []

while True:
    email = input("Masukkan email: ").strip()
    if email.lower() == "tutup":
        break

    error = deteksi_anomali_email(email)

    if len(error) == 0 and email in daftar_valid:
        error.append("Email sudah terdaftar (Duplikat).")

    if len(error) == 0:
        print(">> Email VALID!")
        daftar_valid.append(email)
    else:
        print(">> Email DITOLAK karena:")
        for pesan in error:
            print("   -", pesan)

print("\n--- HASIL EMAIL VALID ---")
if len(daftar_valid) > 0:
    print(cetak_daftar(daftar_valid, border))
else:
    print("(Tidak ada email valid)")