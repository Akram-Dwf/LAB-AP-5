DOMAIN_RESMI = (".com", ".id", ".ac.id")


def deteksi_anomali_email(email):
    """Cek aturan 1-5 dan 7. Return list deskripsi aturan yang dilanggar
    (list kosong jika valid). Aturan duplikat (6) dicek di program utama
    karena butuh daftar email yang sudah tersimpan."""
    masalah = []

    # Aturan 1: tepat satu '@'. Jika gagal, bagian local/domain tidak bisa
    # ditentukan, jadi pengecekan dihentikan di sini.
    if email.count("@") != 1:
        masalah.append("Harus memiliki tepat satu karakter @.")
        return masalah

    local, domain = email.split("@")

    # Aturan 2: local & domain tidak boleh kosong
    if local == "" or domain == "":
        masalah.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    # Aturan 3: tidak boleh ada spasi
    if " " in email:
        masalah.append("Tidak boleh mengandung spasi.")

    # Aturan 4: aturan titik pada local
    if local.startswith(".") or local.endswith(".") or ".." in local:
        masalah.append("Bagian local tidak boleh diawali atau diakhiri titik, "
                       "serta tidak boleh mengandung titik berurutan.")

    # Aturan 5: aturan titik pada domain
    if "." not in domain:
        masalah.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        masalah.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    # Aturan 7: akhiran domain resmi
    resmi = False
    for akhiran in DOMAIN_RESMI:
        if email.lower().endswith(akhiran):
            resmi = True
    if not resmi:
        masalah.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return masalah


def cetak_daftar(daftar_email_valid, karakter_border):
    """Bentuk string multi-baris berbingkai; lebar mengikuti email terpanjang."""
    if len(daftar_email_valid) == 0:
        return "(Tidak ada email valid)"

    terpanjang = 0
    for email in daftar_email_valid:
        if len(email) > terpanjang:
            terpanjang = len(email)

    garis = "+" + karakter_border * (terpanjang + 2) + "+"
    hasil = garis
    for email in daftar_email_valid:
        spasi = " " * (terpanjang - len(email))
        hasil += "\n| " + email + spasi + " |"
    hasil += "\n" + garis
    return hasil


def main():
    print("--- Sistem Pencatatan email valid ---")
    border = input("Masukkan border dengan karakter bebas: ")
    if border == "":
        border = "="
    border = border[0]

    print()
    print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

    daftar_valid = []
    while True:
        email = input("Masukkan email: ")
        if email.strip().lower() == "tutup":
            break

        masalah = deteksi_anomali_email(email)

        # Aturan 6: duplikat (tidak peka huruf besar/kecil)
        for tersimpan in daftar_valid:
            if tersimpan.lower() == email.lower():
                masalah.append("Email sudah terdaftar (Duplikat).")
                break

        if len(masalah) == 0:
            daftar_valid.append(email)
            print(">> Email VALID!")
        else:
            print(">> Email DITOLAK karena:")
            for pesan in masalah:
                print("   - " + pesan)

    print()
    print("--- HASIL EMAIL VALID ---")
    print(cetak_daftar(daftar_valid, border))


if __name__ == "__main__":
    main()