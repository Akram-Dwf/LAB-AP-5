ALFABET = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    hasil = ""
    for ch in teks.lower():
        if ch in ALFABET:
            hasil += ch
    return hasil
def cek_palinrome(teks):
    terbalik = "".join(reversed(teks))
    if teks == terbalik:
        return (True, -1)
    for i in range(len(teks)):
        return (False, i)
def inti_palinrome(teks):
    terpanjang = ""
    awal = 0
    for i in range (len(teks)):
        for j in range(i + 1, len(teks) + 1):
            potongan = teks[i:j]
            if len(potongan) > len(terpanjang):
                if cek_palinrome(potongan)[0]:
                    terpanjang = potongan
                    awal = i
    return{"teks": terpanjang, "panjang": len(terpanjang), "indeks_awal": awal}


teks = input("masukkan teks prasasti: ")
bersih = bersihkan_teks(teks)
print()
print("teks bersih:", bersih)
print("output terharap:", inti_palinrome(bersih))



