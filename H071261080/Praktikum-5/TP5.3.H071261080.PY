ALFABET = "abcdefghijklmnopqrstuvwxyz"
def cek_sandi(ch, k):
    posisi = ALFABET.find(ch.lower())
    if posisi == -1:
        return ch
    baru = ALFABET[(posisi + k) % 26]
    if ch == ch.upper():
        return baru.upper()
    return baru

def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:
        hasil += cek_sandi(ch, k)
    return hasil

def mesin_deskripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil = []
    for k in range(26):
        pesan = mesin_deskripsi(sandi, k)
        if pesan.lower(). find(kata_kunci.lower()) != -1:
            hasil.append((k, pesan))
    return hasil
sandi = input("masukkan pesan tersita (enkripsi caesar): ")
kata_kunci = input("masukkan kata kunci target: ")
print()
print("output deskripsi:", retas_sandi(sandi, kata_kunci))