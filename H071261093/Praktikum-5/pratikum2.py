def cek_kata(teks, kata):
    indeks_list = []
    teks_lower = teks.lower()
    kata_lower = kata.lower()
    start = 0
    panjang = len(kata)

    while start < len(teks_lower):
        pos = teks_lower.find(kata_lower, start)
        if pos == -1:
            break
        if cek_batas_kata(teks, pos, panjang):
            indeks_list.append(pos)
        start = pos + 1

    return indeks_list

def bukan_huruf(huruf):
    return not huruf.isalpha()


def cek_batas_kata(teks, i, panjang):
    
    if i > 0 and not bukan_huruf(teks[i - 1]):
        return False
    akhir = i + panjang
    if akhir < len(teks) and not bukan_huruf(teks[akhir]):
            return False
    akhir = i + panjang
    if akhir < len(teks) and not bukan_huruf(teks[akhir]):
        return False
    return True

def sensor_kata(teks, kata, simbol):
    indeks_awal = cek_kata(teks, kata)
    panjang_kata = len(kata)
    teks_tersensor = ""
    posisi_sekarang = 0

    for idx in indeks_awal:
        teks_tersensor += teks[posisi_sekarang:idx]
        teks_tersensor += simbol * panjang_kata
        posisi_sekarang = idx + panjang_kata

    teks_tersensor += teks[posisi_sekarang:]
    jumlah_tersensor = len(indeks_awal)

    return teks_tersensor, jumlah_tersensor, indeks_awal


teks_input = input("Masukkan Teks: ")
kata_input = input("Masukkan kata target: ")
simbol_input = input("Masukkan simbol: ")

hasil_teks, jumlah, list_indeks = sensor_kata(teks_input, kata_input, simbol_input)

print(f"Hasil Teks: {hasil_teks}")
print(f"Jumlah: {jumlah} | Indeks: {list_indeks}")