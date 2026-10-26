ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_sandi(ch, k):
    """Geser satu karakter ch sejauh k posisi (tanpa ord/chr)."""
    idx = ALFABET.find(ch.lower())
    if idx == -1:
        return ch                       # spasi, angka, tanda baca tidak diubah
    baru = ALFABET[(idx + k) % 26]      # % menangani k negatif maupun > 26
    if ch != ch.lower():                # huruf asli kapital
        return baru.upper()
    return baru.lower()


def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:
        hasil += cek_sandi(ch, k)
    return hasil


def mesin_dekripsi(teks, k):
    # dekripsi = enkripsi dengan pergeseran berlawanan arah
    return mesin_enkripsi(teks, -k)


def retas_sandi(sandi, kata_kunci):
    """Brute force kunci 0..25, simpan hasil yang memuat kata kunci."""
    hasil = []
    for k in range(26):
        pesan = mesin_dekripsi(sandi, k)
        if pesan.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, pesan))
    return hasil


def main():
    sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
    kata_kunci = input("Masukkan kata kunci target: ")
    print()
    print("Output Deskripsi:", retas_sandi(sandi, kata_kunci))


if __name__ == "__main__":
    main()