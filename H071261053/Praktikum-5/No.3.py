ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(karakter, pergeseran):
    karakter_kecil = karakter.lower()

    if karakter_kecil in ALFABET:
        posisi_huruf = ALFABET.find(karakter_kecil)
        posisi_baru = (posisi_huruf + pergeseran) % 26
        huruf_baru = ALFABET[posisi_baru]

        if karakter.isupper():
            return huruf_baru.upper()

        return huruf_baru

    return karakter


def mesin_enkripsi(teks, pergeseran):
    hasil_enkripsi = ""

    for karakter in teks:
        hasil_enkripsi += cek_sandi(karakter, pergeseran)

    return hasil_enkripsi


def mesin_dekripsi(teks, pergeseran):
    return mesin_enkripsi(teks, -pergeseran)

def retas_sandi(sandi, kata_kunci):
    hasil_retas = []

    for kunci in range(26):
        pesan_asli = mesin_dekripsi(sandi, kunci)

        if pesan_asli.lower().find(kata_kunci.lower()) != -1:
            hasil_retas.append((kunci, pesan_asli))

    return hasil_retas


sandi = input("Masukan pesan tersita (enkripsi Caesar): ")
kata_kunci = input("Masukan kata kunci target: ")
hasil = retas_sandi(sandi, kata_kunci)
print("Output Deskripsi:", hasil)