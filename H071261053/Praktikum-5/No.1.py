
def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    teks_bersih = ""

    for karakter in teks:
        karakter = karakter.lower()

        if karakter in alfabet:
            teks_bersih += karakter

    return teks_bersih

def cek_palindrome(teks):
    teks_balik = ''.join(reversed(teks))

    if teks == teks_balik:
        return True, -1

    indeks_pertama_beda = 0
    for i in range(len(teks)):
        if teks [i] != teks_balik [i]:
            indeks_pertama_beda = i
            break

    return False, indeks_pertama_beda

def inti_palindrome(teks_bersih):

    palindrome_terpanjang = ""
    indeks_awal = 0

    for i in range(len(teks_bersih)):
        for j in range(i + 1, len(teks_bersih) +1):
            substring = teks_bersih[i:j]

            hasil, indeks_pertama_beda = cek_palindrome(substring)

            if hasil:
                if len(substring) > len(palindrome_terpanjang):
                    palindrome_terpanjang = substring
                    indeks_awal = i

    return {
        "teks": palindrome_terpanjang,
        "panjang": len(palindrome_terpanjang),
        "indeks_awal": indeks_awal
    }

teks = input("Masukkan teks prasasti: ")
print()
teks_bersih = bersihkan_teks(teks)
hasil = inti_palindrome(teks_bersih)


print("Teks Bersih:", teks_bersih)
print("Output Terharap", hasil)