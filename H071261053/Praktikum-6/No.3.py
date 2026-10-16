def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)

    return True

def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return

    total_durasi = 0
    nomor = 1

    print("=" * 56)
    print(f"{'No':<4}{'Judul':<23}{'Artis':<17}{'Genre':<12}{'Durasi'}")
    print("=" * 56)

    for lagu in playlist:
        judul = lagu[0]
        artis = lagu[1]
        genre = lagu[2]
        durasi = lagu[3]

        menit = durasi // 60
        detik = durasi % 60

        if detik < 10:
            detik = "0" + str(detik)

        print(f"{nomor:<4}{judul:<23}{artis:<17}{genre:<12}{menit}:{detik}")

        total_durasi += durasi
        nomor += 1

    print("Total durasi playlist:",
        total_durasi // 60,
        "menit",
        total_durasi % 60,
        "detik")

def filter_genre(playlist, genre_target):
    hasil = [lagu for lagu in playlist
        if lagu[2] == genre_target]

    return hasil

def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        return False

    lagu_dihapus = playlist.pop(nomor - 1)

    return lagu_dihapus

def statistik_playlist(playlist, genre_set):
    print("========================================")
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("========================================")
    print("Total lagu    :", len(playlist))
    print("Jumlah genre  :", len(genre_set))
    print("Daftar genre  :", genre_set)

    if len(playlist) == 0:
        print("Playlist masih kosong.")
        print("========================================")
        return

    jumlah_genre = {}

    for lagu in playlist:
        genre = lagu[2]

        if genre in jumlah_genre:
            jumlah_genre[genre] += 1
        else:
            jumlah_genre[genre] = 1

    print("Distribusi genre:")

    for genre in jumlah_genre:
        print(" ", genre, ":", "#" * jumlah_genre[genre],
              f"({jumlah_genre[genre]})")

    lagu_terpanjang = playlist[0]
    lagu_terpendek = playlist[0]

    for lagu in playlist:
        if lagu[3] > lagu_terpanjang[3]:
            lagu_terpanjang = lagu

        if lagu[3] < lagu_terpendek[3]:
            lagu_terpendek = lagu

    durasi_panjang = lagu_terpanjang[3]
    durasi_pendek = lagu_terpendek[3]

    detik_panjang = durasi_panjang % 60
    detik_pendek = durasi_pendek % 60

    if detik_panjang < 10:
        detik_panjang = "0" + str(detik_panjang)

    if detik_pendek < 10:
        detik_pendek = "0" + str(detik_pendek)

    print("Lagu terpanjang :", lagu_terpanjang[0],
        f"({durasi_panjang // 60}:{detik_panjang})")

    print("Lagu terpendek  :",lagu_terpendek[0],
        f"({durasi_pendek // 60}:{detik_pendek})")

    print("========================================")

playlist = []
genre_set = set()

while True:
    print("========================================")
    print("    PLAYLIST MUSIK - PLAYTUNE")
    print("========================================")
    print("Menu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        judul = input("Judul lagu: ")
        artis = input("Artis: ")
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")

        while True:
            try:
                durasi = int(input("Durasi (dalam detik): "))

                if durasi > 0:
                    break

                print("Durasi harus berupa angka positif.")

            except ValueError:
                print("Input tidak valid. Masukkan angka bulat.")

        tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)

        print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")

    elif pilihan == "2":
        tampilkan_playlist(playlist)

    elif pilihan == "3":
        print("Genre tersedia:", genre_set)
        genre_target = input("Masukkan genre yang ingin difilter: ")

        hasil = filter_genre(playlist, genre_target)

        if len(hasil) == 0:
            print("Tidak ada lagu dengan genre tersebut.")
        else:
            print(f"Lagu bergenre '{genre_target}':")

            nomor = 1

            for lagu in hasil:
                menit = lagu[3] // 60
                detik = lagu[3] % 60

                if detik < 10:
                    detik = "0" + str(detik)

                print(f"  {nomor}. {lagu[0]} - {lagu[1]} "
                    f"({menit}:{detik})")

                nomor += 1

    elif pilihan == "4":
        tampilkan_playlist(playlist)

        if len(playlist) > 0:
            try:
                nomor = int(input("Nomor lagu yang ingin dihapus: "))
                hasil_hapus = hapus_lagu(playlist, nomor)

                if hasil_hapus is False:
                    print("Nomor lagu tidak valid.")
                else:
                    genre_set = set()

                    for lagu in playlist:
                        genre_set.add(lagu[2])

                    print(f"Lagu '{hasil_hapus[0]}' berhasil dihapus!")

            except ValueError:
                print("Input harus berupa angka.")

    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak valid. Masukkan angka 1-6.")