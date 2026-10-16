ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    if ch.lower() in ALFABET:
        huruf = ALFABET.find(ch.lower())
        baru = ALFABET[(huruf + k) % 26]
        return baru.upper() if ch.isupper() else baru
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
    for k in range(26):
        pesan = mesin_dekripsi(sandi, k)
        if pesan.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, pesan))
    return hasil

sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci = input("Masukkan kata kunci target: ")
print("Output Deskripsi:", retas_sandi(sandi, kata_kunci))