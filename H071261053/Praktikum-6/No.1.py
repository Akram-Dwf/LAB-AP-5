def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {"judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok}
    inventaris.append(buku)
    return True

def cari_buku(inventaris, kata_kunci):
    hasil = []

    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)

    return hasil

def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah

            if stok_baru < 0:
                return False, "Gagal: stok tidak mencukupi."

            buku["stok"] = stok_baru
            if jumlah < 0:
                return True, (f"Stok '{buku['judul']}' berkurang {abs(jumlah)}. "
                    f"Stok sekarang: {stok_baru}")

            return True, (f"Stok '{buku['judul']}' bertambah {jumlah}. "
                f"Stok sekarang: {stok_baru}")

    return False, "Error: buku tidak ditemukan."

def ringkasan_inventaris(inventaris):
    jumlah_jenis = len(inventaris)
    total_stok = 0
    total_aset = 0
    buku_termahal = None

    for buku in inventaris:
        total_stok += buku["stok"]
        total_aset += buku["harga"] * buku["stok"]

        if buku_termahal is None or buku["harga"] > buku_termahal["harga"]:
            buku_termahal = buku

    return jumlah_jenis, total_stok, total_aset, buku_termahal

inventaris = []

print("=" * 40)
print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("=" * 40)

while True:
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")

        try:
            harga = float(input("Harga: "))
            stok = int(input("Stok awal: "))

            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif.")
            else:
                tambah_buku(inventaris, judul, penulis, harga, stok)
                print(f"Buku '{judul}' berhasil ditambahkan!")

        except ValueError:
            print("Error: harga harus angka dan stok harus bilangan bulat.")

    elif pilihan == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        hasil = cari_buku(inventaris, kata_kunci)

        if hasil:
            print(f"Ditemukan {len(hasil)} buku:")

            nomor = 1

            for buku in hasil:
                print(f"{nomor}. {buku['judul']} - {buku['penulis']}"
                    f"| Rp{buku['harga']:g} | Stok: {buku['stok']}")
                nomor += 1

        else:
            print("Buku tidak ditemukan.")

    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ")

        try:
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))

            berhasil, pesan = update_stok(inventaris, judul, jumlah)
            print(pesan)

        except ValueError:
            print("Error: perubahan stok harus berupa bilangan bulat.")

    elif pilihan == "4":
        jumlah_jenis, total_stok, total_aset, buku_termahal = (ringkasan_inventaris(inventaris))

        print("=" * 40)
        print("RINGKASAN INVENTARIS BOOKNEST")
        print("=" * 40)
        print(f"Jumlah jenis buku : {jumlah_jenis}")
        print(f"Total seluruh stok: {total_stok}")
        print(f"Total nilai aset  : Rp{total_aset:.0f}")

        if buku_termahal is not None:
            print(f"Buku termahal: {buku_termahal['judul']} "
                f"(Rp{buku_termahal['harga']:.0f})")
        else:
            print("Buku termahal: Belum ada buku")

        print("=" * 40)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break

    else:
        print("Pilihan tidak valid.")