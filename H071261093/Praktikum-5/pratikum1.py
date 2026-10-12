def bersihkan_teks(teks):
    hasil = ""
    alfabet = "abcdefghijklmnopqrstuvwxyz"

    for huruf in teks:
        if huruf.lower() in alfabet:
            hasil += huruf.lower()

    return hasil


def cek_palindrome(teks):
    for i in range(len(teks)):
        if teks[i] != teks[len(teks) - 1 - i]:
            return False, i

    return True, -1


def inti_palindrome(teks):
    palindrome_terbaik = ""
    indeks_terbaik = 0

    for panjang in range(len(teks), 0, -1):
        for indeks in range(len(teks) - panjang + 1):
            substring = teks[indeks:indeks + panjang]

            hasil, posisi = cek_palindrome(substring)

            if hasil:
                palindrome_terbaik = substring
                indeks_terbaik = indeks
                return {
                    "teks": palindrome_terbaik,
                    "panjang": len(palindrome_terbaik),
                    "indeks_awal": indeks_terbaik
                }

    return {
        "teks": palindrome_terbaik,
        "panjang": len(palindrome_terbaik),
        "indeks_awal": indeks_terbaik
    }


teks = input("Masukkan teks prasasti: ")

teks_bersih = bersihkan_teks(teks)

print("\nTeks Bersih:", teks_bersih)
print("Output Terharap:", inti_palindrome(teks_bersih))