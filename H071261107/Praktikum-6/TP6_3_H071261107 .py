
playlist = []
genre_set = set()


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    try:
        durasi = int(durasi)

        if durasi <= 0:
            raise ValueError

        lagu = (judul, artis, genre, durasi)
        playlist.append(lagu)
        genre_set.append(genre.capitalize())

        print("Lagu berhasil ditambahkan!")

    except ValueError:
        print("ERROR: Durasi harus berupa angka positif!")


def tampilkan_playlist(playlist):
    total = 0

    if len(playlist) == 0:
        print("Playlist masih kosong!")
        return

    print("===== PLAYLIST =====")
    print("No | Judul | Artis | Genre | Durasi")

    for i in range(len(playlist)):
        lagu = playlist[i]
        menit = lagu[3] // 60
        detik = lagu[3] % 60

        print(i + 1, "|", lagu[0], "|", lagu[1], "|",
              lagu[2], "|", f"{menit}:{detik:02d}")

        total += lagu[3]

    print("Total durasi:", total // 60, "menit", total % 60, "detik")


def filter_genre(playlist, genre_target):
    hasil = [lagu for lagu in playlist
             if lagu[2].lower() == genre_target.lower()]

    return hasil


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("ERROR: Nomor lagu tidak ditemukan!")
    else:
        lagu = playlist.pop(nomor - 1)
        print("Lagu", lagu[0], "berhasil dihapus!")


def statistik_playlist(playlist, genre_set):
    if len(playlist) == 0:
        print("Playlist masih kosong!")
        return

    distribusi = {}

    for genre in genre_set:
        distribusi[genre] = 0

    for lagu in playlist:
        distribusi[lagu[2]] += 1

    terpanjang = playlist[0]
    terpendek = playlist[0]

    for lagu in playlist:
        if lagu[3] > terpanjang[3]:
            terpanjang = lagu

        if lagu[3] < terpendek[3]:
            terpendek = lagu

    print("\n===== STATISTIK PLAYLIST =====")
    print("Total lagu:", len(playlist))
    print("Jumlah genre unik:", len(genre_set))
    print("Distribusi lagu per genre:")

    for genre in distribusi:
        print(genre, ":", distribusi[genre], "lagu")

    print("Lagu terpanjang:", terpanjang[0])
    print("Lagu terpendek:", terpendek[0])


while True:
    print("\n===== PLAYTUNE =====")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

    menu = input("Pilih menu (1-6): ")

    if menu == "1":
        judul = input("Judul lagu: ")
        artis = input("Nama artis: ")
        genre = input("Genre: ").capitalize()
        durasi = input("Durasi (detik): ")

        tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)

    elif menu == "2":
        tampilkan_playlist(playlist)

    elif menu == "3":
        print("Genre tersedia:", genre_set)
        genre_target = input("Masukkan genre: ")

        hasil = filter_genre(playlist, genre_target)

        if len(hasil) == 0:
            print("Tidak ada lagu dengan genre tersebut!")
        else:
            tampilkan_playlist(hasil)

    elif menu == "4":
        tampilkan_playlist(playlist)

        if len(playlist) > 0:
            try:
                nomor = int(input("Nomor lagu yang ingin dihapus: "))
                hapus_lagu(playlist, nomor)
            except ValueError:
                print("ERROR: Nomor harus berupa angka!")

    elif menu == "5":
        statistik_playlist(playlist, genre_set)

    elif menu == "6":
        break

    else:
        print("Menu tidak valid!")

print("Terima kasih telah menggunakan PlayTune!")
