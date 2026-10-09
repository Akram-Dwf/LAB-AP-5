
daftar_email_valid = []
daftar_email_tercatat = []


def deteksi_anomali_email(email):
    error = []

    # Aturan 1: Harus memiliki tepat satu @
    if email.count("@") != 1:
        error.append("Email harus memiliki tepat satu karakter @")

    # Aturan 3: Tidak boleh ada spasi
    if " " in email:
        error.append("Email tidak boleh mengandung spasi")

    # Aturan 6: Tidak boleh duplikat
    for email_lama in daftar_email_tercatat:
        if email.lower() == email_lama.lower():
            error.append("Email tidak boleh duplikat")
            break

    # Pemeriksaan local dan domain jika hanya ada satu @
    if email.count("@") == 1:
        local, domain = email.split("@")

        # Aturan 2: Local dan domain tidak boleh kosong
        if local == "":
            error.append("Bagian local tidak boleh kosong")

        if domain == "":
            error.append("Bagian domain tidak boleh kosong")

        # Aturan 4: Pemeriksaan bagian local
        if local.startswith(".") or local.endswith("."):
            error.append("Bagian local tidak boleh diawali atau diakhiri titik")

        if ".." in local:
            error.append("Bagian local tidak boleh memiliki titik berurutan")

        # Aturan 5: Pemeriksaan bagian domain
        if "." not in domain:
            error.append("Domain harus memiliki minimal satu titik")

        if ".." in domain:
            error.append("Domain tidak boleh memiliki titik berurutan")

        if domain.endswith("."):
            error.append("Domain tidak boleh diakhiri titik")

        # Aturan 7: Akhiran domain resmi
        if not domain.endswith((".com", ".id", ".ac.id")):
            error.append("Email harus berakhiran .com, .id, atau .ac.id")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    if len(daftar_email_valid) == 0:
        return "Belum ada email valid."

    email_terpanjang = max(
        len(email) for email in daftar_email_valid
    )

    lebar = email_terpanjang + 4
    border = karakter_border * (lebar + 2)

    hasil = border + "\n"

    for email in daftar_email_valid:
        isi = "  " + email + "  "
        hasil += "|" + isi.ljust(lebar) + "|\n"

    hasil += border

    return hasil


while True:
    email = input("\nMasukkan email (ketik 'tutup' untuk selesai): ")

    if email.lower() == "tutup":
        break

    error = deteksi_anomali_email(email)

    # Catat email agar masukan berikutnya bisa diperiksa duplikatnya
    daftar_email_tercatat.append(email)

    if len(error) == 0:
        daftar_email_valid.append(email)
        print("\nEmail valid!")
        print(cetak_daftar([email], "="))
    else:
        print("\nEmail tidak valid. Kesalahan:")

        for nomor, pesan in enumerate(error, start=1):
            print(str(nomor) + ". " + pesan)


print("\n=== DAFTAR SELURUH EMAIL VALID ===")
print(cetak_daftar(daftar_email_valid, "="))