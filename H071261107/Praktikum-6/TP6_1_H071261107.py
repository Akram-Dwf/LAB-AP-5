
listbuku = []

def tambah_buku(inventaris, judul, penulis, harga, stok):
    try:
        harga = int(harga)
        stok = int(stok)

        if harga < 0 or stok < 0:
            raise ValueError

        buku = {
            "judul": judul,
            "penulis": penulis,
            "harga": harga,
            "stok": stok
        }

        inventaris.append(buku)
        print("Buku berhasil ditambahkan!")

    except ValueError:
        print("ERROR: Harga dan stok harus angka positif!")


def cari_buku(inventaris, kata_kunci):
    jumlah = 0

    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            jumlah += 1
            print(buku["judul"], "-", buku["penulis"],
                  "| Rp", buku["harga"], "| Stok:", buku["stok"])

    print("Ditemukan", jumlah, "buku")


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            if buku["stok"] + jumlah < 0:
                print("Gagal! Stok tidak cukup.")
                return

            buku["stok"] += jumlah
            print("Stok berhasil diupdate. Stok sekarang:", buku["stok"])
            return

    print("ERROR: Buku tidak ditemukan!")


def ringkasan_inventaris(inventaris):
    total_stok = 0
    total_aset = 0

    for buku in inventaris:
        total_stok += buku["stok"]
        total_aset += buku["harga"] * buku["stok"]

    print("Jumlah jenis buku:", len(inventaris))
    print("Total seluruh stok:", total_stok)
    print("Total nilai aset: Rp", total_aset)

    if len(inventaris) > 0:
        termahal = inventaris[0]

        for buku in inventaris:
            if buku["harga"] > termahal["harga"]:
                termahal = buku

        print("Buku termahal:", termahal["judul"], "- Rp", termahal["harga"])
    else:
        print("Belum ada buku")


while True:
    print("\n========================================")
    print("SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print("========================================")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    menu = input("Pilih menu (1-5): ")

    if menu == "1":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")
        harga = input("Harga: ")
        stok = input("Stok awal: ")

        tambah_buku(listbuku, judul, penulis, harga, stok)

    elif menu == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        cari_buku(listbuku, kata_kunci)

    elif menu == "3":
        judul = input("Judul buku yang ingin diupdate: ")

        try:
            jumlah = int(input("Jumlah perubahan stok: "))
            update_stok(listbuku, judul, jumlah)
        except ValueError:
            print("ERROR: Masukkan angka!")

    elif menu == "4":
        ringkasan_inventaris(listbuku)

    elif menu == "5":
        break

    else:
        print("Menu tidak valid!")

print("Terimakasih telah menggunakan BookNest")
