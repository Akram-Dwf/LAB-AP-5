def format_durasi(detik):
    menit = detik // 60
    sisa = detik % 60
    return f"{menit}:{sisa:02d}"


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return

    garis = "=" * 55
    print(garis)
    print(f"{'No':<4}{'Judul':<22}{'Artis':<14}{'Genre':<8}{'Durasi':<6}")
    print(garis)

    total_detik = 0
    for i, (judul, artis, genre, durasi) in enumerate(playlist, start=1):
        print(f"{i:<4}{judul:<22}{artis:<14}{genre:<8}{format_durasi(durasi):<6}")
        total_detik += durasi

    print(garis)
    print(f"Total durasi playlist: {total_detik // 60} menit {total_detik % 60} detik")


def filter_genre(playlist, genre_target):
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Error: Nomor lagu tidak valid!")
        return False
    lagu = playlist.pop(nomor - 1)
    print(f"Lagu '{lagu[0]}' berhasil dihapus!")
    return True


def statistik_playlist(playlist, genre_set):
    print("=" * 40)
    print(" STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)

    if len(playlist) == 0:
        print(" Playlist masih kosong.")
        print("=" * 40)
        return

    # Dictionary untuk menghitung jumlah lagu per genre
    distribusi = {}
    for lagu in playlist:
        genre = lagu[2]
        distribusi[genre] = distribusi.get(genre, 0) + 1

    terpanjang = max(playlist, key=lambda lagu: lagu[3])
    terpendek = min(playlist, key=lambda lagu: lagu[3])

    print(f" Total lagu : {len(playlist)}")
    print(f" Jumlah genre : {len(genre_set)}")
    print(f" Daftar genre : {genre_set}")
    print(" Distribusi genre:")
    for genre, jumlah in distribusi.items():
        print(f" {genre} : {'#' * jumlah} ({jumlah})")
    print(f" Lagu terpanjang : {terpanjang[0]} ({format_durasi(terpanjang[3])})")
    print(f" Lagu terpendek : {terpendek[0]} ({format_durasi(terpendek[3])})")
    print("=" * 40)


def tampilkan_menu():
    print("Menu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")


def main():
    playlist = []
    genre_set = set()

    print("=" * 40)
    print(" PLAYLIST MUSIK - PLAYTUNE")
    print("=" * 40)

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == "1":
            judul = input("Judul lagu: ").strip()
            artis = input("Artis: ").strip()
            genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip()
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi <= 0:
                    print("Error: Durasi harus berupa angka positif!")
                else:
                    tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            except ValueError:
                print("Error: Durasi harus berupa angka!")

        elif pilihan == "2":
            tampilkan_playlist(playlist)

        elif pilihan == "3":
            if len(playlist) == 0:
                print("Playlist masih kosong.")
            else:
                print(f"Genre tersedia: {genre_set}")
                genre_target = input("Masukkan genre yang ingin difilter: ").strip()
                hasil = filter_genre(playlist, genre_target)
                if len(hasil) == 0:
                    print(f"Tidak ada lagu bergenre '{genre_target}'.")
                else:
                    print(f"Lagu bergenre '{genre_target}':")
                    for i, (judul, artis, genre, durasi) in enumerate(hasil, start=1):
                        print(f" {i}. {judul} - {artis} ({format_durasi(durasi)})")

        elif pilihan == "4":
            if len(playlist) == 0:
                print("Playlist masih kosong.")
            else:
                tampilkan_playlist(playlist)
                try:
                    nomor = int(input("Nomor lagu yang ingin dihapus: "))
                    if hapus_lagu(playlist, nomor):
                        # Sinkronkan set genre dengan lagu yang tersisa
                        genre_set.clear()
                        genre_set.update(lagu[2] for lagu in playlist)
                except ValueError:
                    print("Error: Nomor lagu harus berupa angka!")

        elif pilihan == "5":
            statistik_playlist(playlist, genre_set)

        elif pilihan == "6":
            print("Terima kasih telah menggunakan PlayTune!")
            break

        else:
            print("Pilihan tidak valid! Silakan pilih 1-6.")


main()