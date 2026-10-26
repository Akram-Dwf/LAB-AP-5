ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_kata(teks, kata):
    """Return list semua indeks kemunculan kata (tidak peka huruf besar/kecil)."""
    indeks = []
    if kata == "":
        return indeks
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    start = 0
    while True:
        pos = teks_kecil.find(kata_kecil, start)
        if pos == -1:
            break
        indeks.append(pos)
        start = pos + 1
    return indeks


def cek_batas_kata(teks, i, panjang):
    """True jika karakter sebelum & sesudah kata bukan huruf (atau di batas teks)."""
    if i > 0 and teks[i - 1].lower() in ALFABET:
        return False
    akhir = i + panjang
    if akhir < len(teks) and teks[akhir].lower() in ALFABET:
        return False
    return True


def sensor_kata(teks, kata, simbol):
    """Return (teks_tersensor, jumlah_tersensor, list_indeks_awal)."""
    if simbol == "":
        simbol = "*"
    simbol = simbol[0]
    panjang = len(kata)
    hasil = ""
    posisi = 0          # bagian teks asli yang sudah dirakit
    indeks_sensor = []
    for i in cek_kata(teks, kata):
        if i < posisi:
            continue    # lewati kemunculan yang menumpuk dengan yang sudah disensor
        if cek_batas_kata(teks, i, panjang):
            hasil = hasil + teks[posisi:i] + simbol * panjang
            posisi = i + panjang
            indeks_sensor.append(i)
    hasil = hasil + teks[posisi:]
    return (hasil, len(indeks_sensor), indeks_sensor)


def main():
    teks = input("Masukkan Teks: ")
    kata = input("Masukkan kata target: ")
    simbol = input("Masukkan simbol: ")
    hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
    print("Hasil Teks:", hasil)
    print("Jumlah:", jumlah, "| Indeks:", indeks)


if __name__ == "__main__":
    main()