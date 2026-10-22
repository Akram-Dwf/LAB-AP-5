
kandidat_set = set()
rekap_suara = {}

def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()

    if nama in kandidat_set:
        print("Kandidat sudah terdaftar!")
    else:
        kandidat_set.add(nama)
        print("Kandidat", nama, "berhasil didaftarkan!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih = nama_pemilih.lower()
    pilihan = pilihan.capitalize()

    if nama_pemilih in rekap_suara:
        print("Anda sudah memberikan suara!")
    elif pilihan not in kandidat_set:
        print("ERROR: Kandidat tidak ditemukan!")
    else:
        rekap_suara[nama_pemilih] = pilihan
        print("Suara berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for nama in kandidat_set:
        perolehan[nama] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1

    return perolehan


def tampilkan_hasil(perolehan):
    print("\n===== HASIL VOTING =====")

    for nama in perolehan:
        print(nama, ":", perolehan[nama], "suara")

    if len(perolehan) == 0:
        print("Tidak ada kandidat!")
        return

    tertinggi = max(perolehan.values())
    pemenang = []

    for nama in perolehan:
        if perolehan[nama] == tertinggi:
            pemenang.append(nama)

    print("Total suara masuk:", sum(perolehan.values()))

    if tertinggi == 0:
        print("Belum ada suara yang masuk.")
    elif len(pemenang) > 1:
        print("Hasil seri! Perlu pemilihan ulang.")
    else:
        print("Pemenang:", pemenang[0])


print("===== VOTECLASS =====")
print("FASE PENDAFTARAN KANDIDAT")

while True:
    nama = input("Nama kandidat (kosong untuk selesai): ")

    if nama == "":
        break

    daftar_kandidat(kandidat_set, nama)

if len(kandidat_set) < 2:
    print("Kandidat minimal harus 2 orang!")
else:
    print("\nFASE PEMUNGUTAN SUARA")

    while True:
        nama_pemilih = input("Nama pemilih (kosong untuk selesai): ")

        if nama_pemilih == "":
            break

        pilihan = input("Pilih kandidat: ")
        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)
