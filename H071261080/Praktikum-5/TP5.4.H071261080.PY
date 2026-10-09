def deteksi_anomali_email(email):
    masalah = []
    jumlah_at = email.count("@")

    if jumlah_at != 1:
        masalah.append("Harus memiliki tepat satu karakter @.")
    if " " in email:
        masalah.append("Tidak boleh mengandung spasi.")
    if jumlah_at != 1:
        return masalah

    bagian = email.split("@")
    local = bagian[0]
    domain = bagian[1]

    if local == "" or domain == "":
        masalah.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")
    if local.startswith(".") or local.endswith(".") or ".." in local:
        masalah.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")
    if "." not in domain:
        masalah.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        masalah.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")
    if not (email.endswith(".com") or email.endswith(".id") or email.endswith(".ac.id")):
        masalah.append("Wajib berakhiran dengan .com, .id, atau .ac.id")
    return masalah


def cetak_daftar(daftar_email_valid, karakter_border):
    terpanjang = 0
    for email in daftar_email_valid:
        if len(email) > terpanjang:
            terpanjang = len(email)

    garis = "+" + karakter_border * (terpanjang + 2) + "+"
    hasil = garis + "\n"
    for email in daftar_email_valid:
        spasi = " " * (terpanjang - len(email))
        hasil = hasil + "| " + email + spasi + " |\n"
    hasil = hasil + garis
    return hasil


print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")
print()
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_valid = []

while True:
    email = input("Masukkan email: ")
    if email == "tutup":
        break

    masalah = deteksi_anomali_email(email)
    if email in daftar_valid:
        masalah.append("Email sudah terdaftar (Duplikat).")

    if len(masalah) == 0:
        print(">> Email VALID!")
        daftar_valid.append(email)
    else:
        print(">> Email DITOLAK karena:")
        for m in masalah:
            print("   - " + m)

print()
print("--- HASIL EMAIL VALID ---")
print(cetak_daftar(daftar_valid, border))