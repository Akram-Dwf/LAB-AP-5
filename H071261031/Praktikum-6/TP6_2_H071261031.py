def daftar_kandidat(kandidat_set, nama):
    nama = nama.strip().capitalize()
    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar sebagai kandidat!")
        return False
    kandidat_set.add(nama)
    print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")
    return True


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    kunci = nama_pemilih.strip().lower()
    pilihan = pilihan.strip().capitalize()

    if kunci in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
        return False

    if pilihan not in kandidat_set:
        print(f"Error: Kandidat '{pilihan}' tidak ada dalam daftar! Suara tidak dicatat.")
        return False

    rekap_suara[kunci] = pilihan
    print(f"Suara '{nama_pemilih}' untuk '{pilihan}' berhasil dicatat!")
    return True


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    for kandidat in sorted(kandidat_set):
        perolehan[kandidat] = 0
    for kandidat in rekap_suara.values():
        perolehan[kandidat] += 1
    return perolehan


def tampilkan_hasil(perolehan):
    print("=" * 40)
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)

    for kandidat, jumlah in perolehan.items():
        print(f" {kandidat}: {jumlah} suara")

    total = sum(perolehan.values())
    print(f"Total suara masuk: {total}")

    if total == 0:
        print("Belum ada suara yang masuk. Tidak ada pemenang.")
        print("=" * 40)
        return

    suara_tertinggi = max(perolehan.values())
    pemenang = [k for k, v in perolehan.items() if v == suara_tertinggi]

    if len(pemenang) == 1:
        print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")
    else:
        print(f"Hasil SERI antara: {', '.join(pemenang)}")
        print("Perlu dilakukan pemilihan ulang!")
    print("=" * 40)


def main():
    kandidat_set = set()
    rekap_suara = {}

    print("=" * 40)
    print(" SISTEM PEMILIHAN KETUA KELAS")
    print("=" * 40)

    print("--- FASE PENDAFTARAN KANDIDAT ---")
    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
        if nama == "":
            if len(kandidat_set) < 2:
                print("Minimal harus ada 2 kandidat sebelum melanjutkan!")
                continue
            break
        daftar_kandidat(kandidat_set, nama)

    print(f"Kandidat terdaftar: {kandidat_set}")

    
    print("--- FASE PEMUNGUTAN SUARA ---")
    while True:
        nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()
        if nama_pemilih == "":
            break
        print(f"Kandidat yang tersedia: {kandidat_set}")
        pilihan = input("Pilih kandidat: ")
        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)


    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)


main()