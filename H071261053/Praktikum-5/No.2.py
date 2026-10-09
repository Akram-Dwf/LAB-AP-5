
def cek_kata(teks, kata):
    teks_lower = teks.lower()
    kata_lower = kata.lower()

    daftar_indeks = []
    posisi_pencarian = 0

    while True:
        indeks_kata = teks_lower.find(kata_lower, posisi_pencarian)
        
        if indeks_kata == -1:
            break

        daftar_indeks.append(indeks_kata)
        posisi_pencarian = indeks_kata + 1

    return daftar_indeks

def cek_batas_kata(teks, indeks_kata, panjang_kata):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    teks_lower = teks.lower()

    if indeks_kata > 0:
        karakter_sebelum = teks_lower[indeks_kata - 1] 

        if karakter_sebelum in alfabet:
            return False

    indeks_sesudah = indeks_kata + panjang_kata

    if indeks_sesudah < len(teks):
        karakter_sesudah = teks_lower[indeks_sesudah]

        if karakter_sesudah in alfabet:
            return False

    return True

def sensor_kata(teks, kata, simbol):
    panjang_kata = len(kata)
    semua_indeks = cek_kata(teks, kata)
    
    indeks_sensor = []

    for indeks_kata in semua_indeks:
        if cek_batas_kata(teks, indeks_kata, panjang_kata):
            indeks_sensor.append(indeks_kata)
        
    teks_hasil = ""
    posisi_terakhir = 0
    simbol_sensor = simbol * panjang_kata
    
    for indeks_kata in indeks_sensor:
        teks_hasil += teks[posisi_terakhir:indeks_kata]
        teks_hasil += simbol_sensor

        posisi_terakhir = indeks_kata + panjang_kata
        
    teks_hasil += teks[posisi_terakhir:]
    
    return teks_hasil, len(indeks_sensor), indeks_sensor


teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")
hasil_teks, jumlah_sensor, daftar_indeks = sensor_kata(teks, kata, simbol)

print("Hasil Teks:", hasil_teks)
print("Jumlah:", jumlah_sensor, "| Indeks:", daftar_indeks)