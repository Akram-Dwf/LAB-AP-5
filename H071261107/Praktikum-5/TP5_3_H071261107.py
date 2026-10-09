
ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_sandi(ch, k):
    kecil = ch.lower()

    if kecil in ALFABET:
        posisi = ALFABET.find(kecil)
        posisi_baru = (posisi + k) % 26
        hasil = ALFABET[posisi_baru]

        if ch.isupper():
            return hasil.upper()

        return hasil

    return ch


def mesin_enkripsi(teks, k):
    hasil = ""

    for ch in teks:
        hasil += cek_sandi(ch, k)

    return hasil


def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)


def retas_sandi(sandi, kata_kunci):
    hasil = []

    for kunci in range(26):
        pesan = mesin_dekripsi(sandi, kunci)

        if pesan.lower().find(kata_kunci.lower()) != -1:
            hasil.append((kunci, pesan))

    return hasil


sandi = input("Masukkan pesan tersita: ")
kata_kunci = input("Masukkan kata kunci target: ")

print("Output Deskripsi:", retas_sandi(sandi, kata_kunci))