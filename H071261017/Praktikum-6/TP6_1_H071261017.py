daftar_buku = {}
daftar_penulis = {}
daftar_harga = {}
daftar_stok = {}

def tambah_buku(judul, penulis, harga, stok):
    daftar_buku[judul] = judul
    daftar_penulis[judul] = penulis
    daftar_harga[judul] = harga
    daftar_stok[judul] = stok

def total_ditemukan_buku(cari):
    total = 0
    for i in daftar_buku.keys():
        if cari in i:
            total += 1
    return total

def mencari_buku(cari):
    total = total_ditemukan_buku(cari)
    if total == 0:
        print("Tidak ada buku yang ditemukan")
        return
    urutan = 0
    print(f"Ditemukan {total} buku: ")
    for i in daftar_buku.keys():
        if cari in i:
            urutan += 1
            penulis = daftar_penulis[i]
            harga = daftar_harga[i]
            stok = daftar_stok[i]
            print(f"  {urutan}. {i} - {penulis} | Rp{harga} | Stok: {stok}")

def update_stok(buku, simbol, angka):
    if buku not in daftar_stok:
        print("Buku tidak ditemukan")
        return
    if simbol == "-":
        if daftar_stok[buku] - int(angka) < 0:
            print("Gagal membuat perubahan, stok tidak cukup")
        else:
            daftar_stok[buku] -= int(angka)
            print(f"Stok '{buku}' berkurang {angka}. Stok sekarang: {daftar_stok[buku]}")
    elif simbol == "+":
        daftar_stok[buku] += int(angka)
        print(f"Stok '{buku}' bertambah {angka}. Stok sekarang: {daftar_stok[buku]}")
    else:
        print("Awali angka dengan + atau -, contoh: +5 atau -2")

def termahal():
    buku_tertinggi = None
    harga_tertinggi = -1
    for buku, harga in daftar_harga.items():
        if harga > harga_tertinggi:
            harga_tertinggi = harga
            buku_tertinggi = buku
    print(f"Buku termahal     : {buku_tertinggi} (Rp{harga_tertinggi})")

print()
print("=======================================")
print("  SISTEM IVENTARIS TOKO BUKU BOOKNEST")
print("=======================================")
while True:
    try:
        print()
        print("Menu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")
        menu = int(input("Pilih menu (1-5): "))
        print("DEBUG: menu yang diterima =", menu)   # hapus nanti
        if menu == 1:
            judul_buku = input("Judul buku: ").title()
            penulis = input("Penulis: ").title()
            harga = int(input("Harga: "))
            stok = int(input("Stok awal: "))
            tambah_buku(judul_buku, penulis, harga, stok)
            print()
            print(f"Buku '{judul_buku}' berhasil ditambahkan!")
        elif menu == 2:
            cari_buku = input("Masukkan kata kunci judul: ").title()
            mencari_buku(cari_buku)
        elif menu == 3:
            judul_buku = input("Judul buku yang ingin diupdate: ").title()
            jumlah_perubahan = input("Jumlah perubahan (positif=tambah, negatif=kurang): ")
            simbol = jumlah_perubahan[0]
            angka = jumlah_perubahan[1:]
            update_stok(judul_buku, simbol, angka)
        elif menu == 4:
            total_buku = len(daftar_stok)
            total_seluruh_stok = sum(daftar_stok.values())
            total_nilai_aset = 0
            for judul in daftar_harga:
                total_nilai_aset += daftar_harga[judul] * daftar_stok[judul]

            print("===================================")
            print("  RINGKASAN INVENTARIS BOOKNEST")
            print("===================================")
            print(f"Jumlah jenis buku : {total_buku}")
            print(f"Total seluruh stok: {total_seluruh_stok}")
            print(f"Total nilai aset  : Rp{total_nilai_aset}")
            if total_buku > 0:
                termahal()
            input("\nTekan Enter untuk kembali ke menu...")
        elif menu == 5:
            print("Terima kasih telah menggunakan BookNest!")
            break
        else:
            print("Input yang anda masukkan tidak valid")
    except (ValueError, IndexError):
        print("Input yang anda masukkan tidak valid")