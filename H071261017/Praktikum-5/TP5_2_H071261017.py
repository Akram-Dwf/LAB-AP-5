ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_kata(teks, kata):
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    hasil = []
    start = 0
    while True:
        i = teks_kecil.find(kata_kecil, start)
        if i == -1:
            break
        hasil.append(i)
        start = i + 1
    return hasil


def bukan_huruf(ch):
    return ch.lower() not in ALFABET   


def cek_batas_kata(teks, i, panjang):
    if i > 0 and not bukan_huruf(teks[i - 1]):
        return False
    akhir = i + panjang
    if akhir < len(teks) and not bukan_huruf(teks[akhir]):
        return False
    return True


def sensor_kata(teks, kata, simbol):
    semua_indeks = cek_kata(teks, kata)
    panjang = len(kata)

    indeks_sensor = []
    for i in semua_indeks:
        if cek_batas_kata(teks, i, panjang):
            indeks_sensor.append(i)

    hasil = ""
    posisi = 0
    for i in indeks_sensor:
        hasil = hasil + teks[posisi:i] + simbol * panjang
        posisi = i + panjang
    hasil = hasil + teks[posisi:]

    return (hasil, len(indeks_sensor), indeks_sensor)


teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")
hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
print("Hasil Teks:", hasil)
print("Jumlah:", jumlah, "| Indeks:", indeks)