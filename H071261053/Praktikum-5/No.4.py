
def deteksi_anomali_email(email, daftar_email):
    error = []

    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return error

    local, domain = email.split("@")
    if local == "" or domain == "":
        error.append("Bagian sebelah (Local) atau setelah @ (domain) " "tidak boleh kosong.")

    if " " in email:
        error.append("Email tidak boleh mengandung spasi.")

    if local.startswith(".") or local.endswith("."):
        error.append("Bagian local tidak boleh diawali atau diakhiri titik.")

    if ".." in local:
        error.append("Bagian local tidak boleh mengandung titik berurutan.")

    if "." not in domain:
        error.append("Bagian domain wajib memiliki minimal satu titik.")

    if ".." in domain:
        error.append("Bagian domain tidak boleh mengandung titik berurutan.")

    if domain.endswith("."):
        error.append("Bagian domain tidak boleh diakhiri titik.")

    if email in daftar_email:
        error.append("Email sudah terdaftar (Duplikat).")

    domain_resmi = (".com", ".id", ".ac.id")

    if not domain.endswith(domain_resmi):
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id.")

    return error

def cetak_daftar(daftar_email_valid, karakter_border):
    if len(daftar_email_valid) == 0:
        return

    email_terpanjang = max(daftar_email_valid,key=len)

    padding = 2
    lebar = len(email_terpanjang) + padding * 2

    border = karakter_border * (lebar + 2)

    print()
    print("=== HASIL EMAIL VALID ===")
    print(border)

    for email in daftar_email_valid:
        print(karakter_border + " " + email.center(lebar) + " " + karakter_border)

    print(border)


daftar_email_valid = []

print("--- Sistem Pencatatan email Valid ---")

karakter_border = input("Masukkan border dengan karakter bebas: ")

print()
print('Ketik "tutup" untuk mengakhiri masukan '"dan mencetak email.")

while True:

    email = input("Masukkan email: ")

    if email.lower() == "tutup":
        break

    error = deteksi_anomali_email(email, daftar_email_valid)

    if len(error) == 0:
        daftar_email_valid.append(email)

        print()
        print("Masukkan email VALID!")

    else:

        print()
        print(">> Email DITOLAK karena:")

        for pesan in error:
            print("- " + pesan)

cetak_daftar(daftar_email_valid,karakter_border)