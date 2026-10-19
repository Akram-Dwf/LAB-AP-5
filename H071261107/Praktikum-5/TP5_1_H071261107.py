def bersihkan_teks(teks):
    hasil =""
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    
    for huruf in teks:
        huruf = huruf.lower()

        if huruf in alfabet:
            hasil += huruf
        
    return hasil

def cek_palindrome(teks):
    balik = "".join(reversed(teks))

    if teks == balik:
        return True, -1

    for i in range(len(teks)):
        if teks[i] != balik[i]:
            return False, i

def inti_palindrome(teks):
    teks = bersihkan_teks(teks)

    terpanjang = ""
    indeks = 0

    for i in range(len(teks)):
        for j in range(i + 1, len(teks) + 1):
            bagian = teks[i:j]

            if cek_palindrome(bagian)[0]:
                if len(bagian) > len(terpanjang):
                    terpanjang = bagian
                    indeks = i

    return {
        "teks": terpanjang,
        "panjang": len(terpanjang),
        "indeks_awal": indeks
    }


hasil = input("Masukkan teks prasasti :")
teks =  hasil

print(f"Teks Bersih :{bersihkan_teks(teks)}")
print(inti_palindrome(teks))