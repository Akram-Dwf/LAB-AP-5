def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()

    if nama in kandidat_set:
        print("Kandidat sudah terdaftar!")
        return False

    kandidat_set.add(nama)
    print("'" + nama + "' berhasil didaftarkan sebagai kandidat!")
    return True


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih = nama_pemilih.lower()
    pilihan = pilihan.capitalize()

    if pilihan not in kandidat_set:
        print("Error: Kandidat tidak ditemukan!")
        return False

    if nama_pemilih in rekap_suara:
        print("'" + nama_pemilih + "' sudah memberikan suara sebelumnya!")
        return False

    rekap_suara[nama_pemilih] = pilihan
    print("Suara '" + nama_pemilih + "' untuk '" + pilihan + "' berhasil dicatat!")
    return True


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for kandidat in kandidat_set:
        perolehan[kandidat] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] = perolehan[pilihan] + 1

    return perolehan


def tampilkan_hasil(perolehan):
    print("========================================")
    print("     HASIL PEMILIHAN KETUA KELAS        ")
    print("========================================")

    total_suara = 0
    suara_tertinggi = 0
    pemenang = ""

    for kandidat in perolehan:
        jumlah = perolehan[kandidat]
        print(kandidat + ": " + str(jumlah) + " suara")
        total_suara = total_suara + jumlah

        if jumlah > suara_tertinggi:
            suara_tertinggi = jumlah
            pemenang = kandidat

    print("Total suara masuk:", total_suara)

    jumlah_pemenang = 0

    for kandidat in perolehan:
        if perolehan[kandidat] == suara_tertinggi:
            jumlah_pemenang = jumlah_pemenang + 1

    if jumlah_pemenang > 1:
        print("Hasil seri! Perlu pemilihan ulang.")
    elif total_suara == 0:
        print("Belum ada suara yang masuk.")
    else:
        print("PEMENANG:", pemenang, "dengan", suara_tertinggi, "suara!")

    print("========================================")


print("========================================")
print("     SISTEM PEMILIHAN KETUA KELAS")
print("========================================")

kandidat_set = set()

print("--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")

    if nama == "":
        if len(kandidat_set) >= 2:
            break
        else:
            print("Minimal harus ada 2 kandidat!")
            continue

    daftar_kandidat(kandidat_set, nama)

print("Kandidat terdaftar:", kandidat_set)

rekap_suara = {}

print("--- FASE PEMUNGUTAN SUARA ---")

while True:
    nama_pemilih = input("\nNama pemilih (kosongkan untuk selesai): ")

    if nama_pemilih == "":
        break

    print("Kandidat yang tersedia:", kandidat_set)
    pilihan = input("Pilih kandidat: ")

    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

perolehan = hitung_suara(rekap_suara, kandidat_set)

tampilkan_hasil(perolehan)