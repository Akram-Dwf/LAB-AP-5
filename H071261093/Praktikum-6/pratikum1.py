inventaris_toko = []

def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok,
    }
    inventaris.append(buku)
    print()
    print(f"Buku '{judul}' udah di tambahin ya!")
    print()

def cari_buku(inventaris, kata_kunci):
    hasil = []
    for buku in inventaris:
        if kata_kunci in buku["judul"]:
            hasil.append(buku)
    urutan = 0
    panjang = len(hasil)
    print(f"Ditemukan {panjang} buku:")
    for hasil_nya in hasil:
        urutan += 1
        print(f"{urutan} {hasil_nya["judul"]} {hasil_nya["penulis"]} | RP{hasil_nya["harga"]} | Stik: {hasil_nya["stok"]}")

def update_stok(inventaris, judul, jumlah):
    simbol = jumlah[0]
    angka = jumlah[1:]
    for buku in inventaris:
        if buku["judul"] == judul:
            if simbol == "-":
                buku["stok"] -= int(angka)
                if buku["stok"] < 0:
                    print("Tidak dapat membuat perubahan")
                    buku["stok"] += int(angka)
                else:
                    print(f"Stok '{"stok"}' berkurang {angka}. Stok sekarang: {buku["stok"]}")
            elif simbol == "+":
                buku["stok"] += int(angka)
                print(f"Stok '{"stok"}' bertambah {angka}. Stok sekarang: {buku["stok"]}")
        elif judul not in buku["judul"]:
            print("Buku yang anda masukkan tidak ada")

def ringkasan_inventaris(inventaris):
    total_buku = len(inventaris)
    total_seluruh_stok = 0
    total_nilai_aset = 0
    buku_tertinggi = None
    harga_tertinggi = -1
    for i in inventaris:
        total_seluruh_stok += i["stok"]
        total_nilai_aset += i["harga"] * i["stok"]
        if i["harga"] > harga_tertinggi:
            buku_tertinggi = i["judul"]
            harga_tertinggi = i["harga"]
    print()
    print("=" * 33)
    print("  RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 33)
    print(f"Jumlah jenis buku : {total_buku}")
    print(f"Total seluruh stok: {total_seluruh_stok}")
    print(f"Total nilai aset  : {total_nilai_aset}")
    print(f"Buku termahal     : {buku_tertinggi} (Rp{harga_tertinggi})")
    print("=" * 33)

print()
print("=" * 40)
print("  SISTEM IVENTARIS TOKO BUKU BOOKNEST")
print("=" * 40)
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
        if menu == 1:
            judul_buku = input("Judul buku: ").title ()
            penulis = input("Penulis: ").title ()
            harga = int(input("Harga: "))
            stok = int(input("Stok awal: "))
            if harga < 0 or stok < 0:
                print("Harga atau stok tidak boleh mines ya")
                continue
            tambah_buku(inventaris_toko, judul_buku, penulis, harga, stok)
        elif menu == 2:
            mencari_buku = input("Masukkan kata kunci dari judulnya ya: ").title ()
            cari_buku(inventaris_toko, mencari_buku)
        elif menu == 3:
            judul_buku = input("Apa judul yang ingin kamu update: ").title ()
            jumlah_perubahan = input("Jumlah perubahan (positif=tambah, negatif=kurang): ")
            update_stok(inventaris_toko, judul_buku, jumlah_perubahan)
        elif menu == 4:
            ringkasan_inventaris(inventaris_toko)
        elif menu == 5:
            print("Terima kasih telah menggunakan BookNest!")
            break
        else:
            print("Maaf banget tapi input yang anda masukkan itu salah")
    except:
        print("Maaf banget tapi input yang anda masukkan itu salah")
        continue