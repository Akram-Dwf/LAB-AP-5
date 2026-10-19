ALFABET = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    hasil = ""
    for ch in teks:
        if ch.lower() in ALFABET:      
            hasil = hasil + ch.lower()
    return hasil


def cek_palindrome(teks):
    terbalik = "".join(reversed(teks))
    if teks == terbalik:
        return (True, -1)
    
    for i in range(len(teks)):
        if teks[i] != terbalik[i]:
            return (False, i)

def inti_palindrome(teks):
    terbaik = {"teks": "", "panjang": 0, "indeks_awal": 0}
    for i in range(len(teks)):
        for j in range(i + 1, len(teks) + 1):
            potongan = teks[i:j]
            sama, _ = cek_palindrome(potongan)
            
            if sama and len(potongan) > terbaik["panjang"]:
                terbaik = {"teks": potongan, "panjang": len(potongan), "indeks_awal": i}
    return terbaik


teks = input("Masukkan teks prasasti: ")
bersih = bersihkan_teks(teks)
print("\nTeks Bersih:", bersih)
print("Output Terharap:", inti_palindrome(bersih))