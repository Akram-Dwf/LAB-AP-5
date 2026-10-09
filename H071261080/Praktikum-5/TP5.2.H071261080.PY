ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_kata(teks, kata):
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    hasil = []
    start = 0
    posisi = teks_kecil.find(kata_kecil, start)
    while posisi != -1:
        hasil.append(posisi)
        start = posisi + 1
        posisi = teks_kecil. find(kata_kecil, start)
    return hasil

def cek_batas_kata(teks, i, panjang):
    if i > 0 and teks[i - 1].lower() in ALFABET:
        return False
    if i + panjang < len(teks) and teks[i + panjang].lower() in ALFABET:
        return False
    return True

def sensor_kata(teks, kata, simbol):
    semua = cek_kata(teks, kata)
    Panjang = len(kata)
    hasil = ""
    indeks_sensor = []
    posisi_sekarang = 0
    for i in semua:
        if cek_batas_kata(teks, i, Panjang):
            hasil = hasil + teks[posisi_sekarang:i] + simbol * Panjang
            posisi_sekarang = i + Panjang
            indeks_sensor.append(i)
    hasil = hasil + teks[posisi_sekarang:]
    return (hasil, len(indeks_sensor), indeks_sensor)
teks = input("masukkan teks ta: ")
kata = input("masukkan kata target: ")
simbol = input("masukkan simbol: ")
hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
print("hasil teks:", hasil)
print("jumlah:", jumlah, "| indeks:", indeks)