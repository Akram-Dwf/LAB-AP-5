def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()

    if nama not in kandidat_set:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")
    else:
        print(f"'{nama}' telah berada di dalam kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih = nama_pemilih.lower()
    pilihan = pilihan.capitalize()

    if nama_pemilih in rekap_suara:
        print(f"'{nama_pemilih.capitalize()}' sudah memberikan suara sebelumnya!")
    elif pilihan not in kandidat_set:
        print(f"Kandidat '{pilihan}' tidak ditemukan! Suara tidak dicatat.")
    else:
        rekap_suara[nama_pemilih] = pilihan
        print(f"Suara '{nama_pemilih.capitalize()}' untuk '{pilihan}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for kandidat in kandidat_set:
        perolehan[kandidat] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1

    return perolehan


def tampilkan_hasil(perolehan):
    print("\n======================================")
    print("  HASIL PEMILIHAN KETUA KELAS")
    print("======================================")

    for kandidat in (perolehan):
        print(f"  {kandidat}: {perolehan[kandidat]} suara")

    total = sum(perolehan.values())
    print(f"\nTotal suara masuk: {total}")

    if perolehan:
        tertinggi = max(perolehan.values())
        pemenang = [nama for nama, suara in perolehan.items() if suara == tertinggi]

        if len(pemenang) > 1:
            print(f"Hasil SERI antara: {', '.join(pemenang)}")
            print("Perlu dilakukan pemilihan ulang!")
        else:
            print(f"PEMENANG: {pemenang[0]} dengan {tertinggi} suara!")

    print("======================================")


kandidat_set = set()
rekap_suara = {}

print("======================================")
print("  SISTEM PEMILIHAN KETUA KELAS")
print("======================================")

print("\n--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")

    if nama == "":
        break

    daftar_kandidat(kandidat_set, nama)

print(f"\nKandidat terdaftar: {kandidat_set}")

if len(kandidat_set) < 2:
    print("Minimal harus ada 2 kandidat untuk melanjutkan!")
else:
    print("\n--- FASE PEMUNGUTAN SUARA ---")

    while True:
        nama_pemilih = input("\nNama pemilih (kosongkan untuk selesai): ")

        if nama_pemilih == "":
            break

        print(f"Kandidat yang tersedia: {kandidat_set}")
        pilihan = input("Pilih kandidat: ")

        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)