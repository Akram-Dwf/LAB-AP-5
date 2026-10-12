def deteksi_anomali_email(email):
    error = []

    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return error

    lokal, domain = email.split("@")

    if lokal == "" or domain == "":
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if " " in email:
        error.append("Email tidak boleh mengandung spasi.")

    if lokal.startswith(".") or lokal.endswith(".") or ".." in lokal:
        error.append("Bagian lokal tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

    if "." not in domain or ".." in domain or domain.endswith("."):
        error.append("Bagian domain wajib memiliki minimal satu titik dan tidak boleh mengandung titik berurutan atau diakhiri titik.")

    if not email.endswith((".com", ".id", ".ac.id")):
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    if not email_valid:
        return ""
    email_terpanjang = max(len(email) for email in email_valid)
    lebar_garis = email_terpanjang + 2
    garis_horizontal = karakter_border * lebar_garis

    hasil_bingkai = [f"+{garis_horizontal}+"]
    for email in daftar_email_valid:
        baris = f"| {email.ljust(email_terpanjang)} |"
        hasil_bingkai.append(baris)
    hasil_bingkai.append(f"+{garis_horizontal}+")

    return "\n".join(hasil_bingkai)


email_valid = []
border = input("Masukkan border dengan karakter bebas: ")
print("\nKetik 'tutup' untuk mengakhiri masukan dan mencetak email.")

while True:
    email = input("Masukkan email: ")

    if email.lower() == "tutup":
        break

    error = deteksi_anomali_email(email)

    if email in email_valid:
        error.append("Email sudah terdaftar (Duplikat).")

    if error:
        print(">> Email DITOLAK karena:")
        for e in error:
            print("-", e)
    else:
        email_valid.append(email)
        print(">> Email VALID!")

print("\n--- HASIL EMAIL VALID ---")
if email_valid:
        bingkai_teks = cetak_daftar(email_valid, border)
        print(bingkai_teks)
        print()
else:
    print("(Tidak ada email valid yang terdaftar)")
