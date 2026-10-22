daftar_list_kandidat = set()
daftar_suara_kandidat = {}
daftar_suara_pemilihan = {}
rekapan_suara_yang_memilih = set()

def daftar_kandidat(kandidat_set, nama):
    daftar_suara_kandidat[kandidat_set] = 0
    daftar_list_kandidat.add(nama)

def berikan_suara(rekap_suara, kandidat_set):
    if rekap_suara in rekapan_suara_yang_memilih:
        print(f"'{rekap_suara}' sudah memberikan suara sebelumnya!")      
    elif not hitung_suara(rekap_suara, kandidat_set):                     
        print(f"Kandidat '{kandidat_set}' tidak terdaftar!")
    else:
        rekapan_suara_yang_memilih.add(rekap_suara)
        daftar_suara_pemilihan[rekap_suara] = kandidat_set
        print(f"Suara '{rekap_suara}' untuk '{kandidat_set}' berhasil dicatat!")   # UBAH: pakai parameter
    print()

def hitung_suara(rekap_suara, kandidat_set):
    if kandidat_set in daftar_suara_kandidat:
        daftar_suara_kandidat[kandidat_set] += 1
        return True
    return False

def tampilkan_hasil():
    if not daftar_suara_kandidat:                                         # BARU: cegah error jika kosong
        print("Belum ada kandidat.")
        return
    tertinggi = max(daftar_suara_kandidat.values())
    pemenang = [k for k, v in daftar_suara_kandidat.items() if v == tertinggi]
    ada_berapa_pemilih = len(daftar_suara_pemilihan)
    for key, value in daftar_suara_kandidat.items():
        print(f"   {key}: {value} suara")
    print()
    print(f"Total suara masuk: {ada_berapa_pemilih}")
    if len(pemenang) > 1:                                                 
        print("Hasil seri dan perlu pemilihan ulang")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {tertinggi} suara!")

print("==================================")
print("   SISTEM PEMILIHAN KETUA KELAS")
print("==================================")
while True:
    nama_kandidat = input("Masukkan nama kandidat (kosongkan untuk selesai): ").title()
    if nama_kandidat == "":
        print()
        print(f" Kandidat terdaftar: {daftar_list_kandidat}")
        break
    daftar_kandidat(nama_kandidat, nama_kandidat)                         
    print(f"'{nama_kandidat}' berhasil didaftarkan sebagai kandidat!")
print()
print("--- FASE PEMUNGUTAN SUARA ---")
while True:
    print()
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").title()
    if nama_pemilih == "":
        break
    print(f"Kandidat yang tersedia: {daftar_list_kandidat}")
    pilih_kandidat = input("Pilih kandidat: ").title()
    if pilih_kandidat == "":
        print("Nama kandidat tidak boleh kosong")
        continue
    berikan_suara(nama_pemilih, pilih_kandidat)
print()
print("=================================")
print("   HASIL PEMILIHAN KETUA KELAS")
print("=================================")
tampilkan_hasil()