
def cek_kata(teks, kata):
    indeks = []
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    mulai = 0

    while True:
        posisi = teks_kecil.find(kata_kecil, mulai)

        if posisi == -1:
            break

        indeks.append(posisi)
        mulai = posisi + 1

    return indeks

def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwxyz"

    if i > 0 and teks[i - 1].lower() in alfabet:
        return False

    akhir = i + panjang

    if akhir < len(teks) and teks[akhir].lower() in alfabet:
        return False

    return True


def sensor_kata(teks, kata, simbol):
    indeks = cek_kata(teks, kata)
    hasil = ""
    jumlah = 0
    indeks_sensor = []
    posisi = 0

    for i in indeks:
        if cek_batas_kata(teks, i, len(kata)):
            hasil += teks[posisi:i]
            hasil += simbol * len(kata)
            posisi = i + len(kata)
            jumlah += 1
            indeks_sensor.append(i)

    if jumlah > 0:
        hasil += teks[posisi:]
    else:
        hasil = teks

    return hasil, jumlah, indeks_sensor


teks = input("Masukkan teks: ")
kata = input("Kata yang disensor: ")
simbol = input("Simbol sensor: ")

print(sensor_kata(teks, kata, simbol))