def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()
    if nama in kandidat_set:
        print("'" + nama + "' sudah terdaftar sebelumnya!")
    else:
        kandidat_set.add(nama)
        print("'" + nama + "' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pilihan = pilihan.capitalize()
    kunci = nama_pemilih.lower()  

    if pilihan not in kandidat_set:
        print("Kandidat '" + pilihan + "' tidak ada dalam daftar! Suara tidak dicatat.")
    elif kunci in rekap_suara:
        print("'" + nama_pemilih + "' sudah memberikan suara sebelumnya!")
    else:
        rekap_suara[kunci] = pilihan
        print("Suara '" + nama_pemilih + "' untuk '" + pilihan + "' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    for kandidat in kandidat_set:
        perolehan[kandidat] = 0  
    for pemilih in rekap_suara:
        pilihan = rekap_suara[pemilih]
        perolehan[pilihan] += 1
    return perolehan


def tampilkan_hasil(perolehan):
    print("=" * 40)
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)

    total = 0
    tertinggi = 0
    for kandidat in sorted(perolehan):
        suara = perolehan[kandidat]
        print(" " + kandidat + ": " + str(suara) + " suara")
        total += suara
        if suara > tertinggi:
            tertinggi = suara
    print("Total suara masuk: " + str(total))

    if total == 0:
        print("Belum ada suara yang masuk.")
    else:
        pemenang = []
        for kandidat in sorted(perolehan):
            if perolehan[kandidat] == tertinggi:
                pemenang.append(kandidat)

        if len(pemenang) == 1:
            print("PEMENANG: " + pemenang[0] + " dengan " + str(tertinggi) + " suara!")
        else:
            print("Hasil SERI antara: " + ", ".join(pemenang))
            print("Perlu dilakukan pemilihan ulang!")
    print("=" * 40)


print("=" * 40)
print(" SISTEM PEMILIHAN KETUA KELAS")
print("=" * 40)

print("--- FASE PENDAFTARAN KANDIDAT ---")
kandidat_set = set()
while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
    if nama == "":
        if len(kandidat_set) < 2:
            print("Minimal harus ada 2 kandidat! Saat ini baru ada " + str(len(kandidat_set)) + ".")
        else:
            break
    else:
        daftar_kandidat(kandidat_set, nama)
print("Kandidat terdaftar:", kandidat_set)

print("--- FASE PEMUNGUTAN SUARA ---")
rekap_suara = {}
while True:
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()
    if nama_pemilih == "":
        break
    print("Kandidat yang tersedia:", kandidat_set)
    pilihan = input("Pilih kandidat: ").strip()
    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)
