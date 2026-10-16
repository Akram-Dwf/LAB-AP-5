def format_durasi(detik):
    menit = detik // 60
    sisa = detik % 60
    return f"{menit}:{sisa:02d}"  
def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)
    print("Lagu '" + judul + "' oleh " + artis + " berhasil ditambahkan!")
def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return
    print("=" * 55)
    print(f"{'No':<4}{'Judul':<22}{'Artis':<15}{'Genre':<8}{'Durasi'}")
    print("=" * 55)
    nomor = 1
    total = 0
    for lagu in playlist:
        print(f"{nomor:<4}{lagu[0]:<22}{lagu[1]:<15}{lagu[2]:<8}{format_durasi(lagu[3])}")
        total += lagu[3]
        nomor += 1
    print("=" * 55)
    print("Total durasi playlist: " + str(total // 60) + " menit " + str(total % 60) + " detik")
def filter_genre(playlist, genre_target):
    
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]
def hapus_lagu(playlist, nomor):
    if 1 <= nomor <= len(playlist):
        lagu = playlist.pop(nomor - 1)  
        print("Lagu '" + lagu[0] + "' berhasil dihapus!")
    else:
        print("Nomor lagu tidak valid!")
def statistik_playlist(playlist, genre_set):
    print("=" * 40)
    print(" STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)
    if len(playlist) == 0:
        print(" Playlist masih kosong.")
        print("=" * 40)
        return
    hitung = {}
    terpanjang = playlist[0]
    terpendek = playlist[0]
    for lagu in playlist:
        hitung[lagu[2]] = hitung.get(lagu[2], 0) + 1
        if lagu[3] > terpanjang[3]:
            terpanjang = lagu
        if lagu[3] < terpendek[3]:
            terpendek = lagu

    print(" Total lagu       : " + str(len(playlist)))
    print(" Jumlah genre     : " + str(len(genre_set)))
    print(" Daftar genre     :", genre_set)
    print(" Distribusi genre:")
    for genre in hitung:
        print("   " + genre + " : " + "#" * hitung[genre] + " (" + str(hitung[genre]) + ")")
    print(" Lagu terpanjang  : " + terpanjang[0] + " (" + format_durasi(terpanjang[3]) + ")")
    print(" Lagu terpendek   : " + terpendek[0] + " (" + format_durasi(terpendek[3]) + ")")
    print("=" * 40)

playlist = []
genre_set = set()

print("=" * 40)
print(" PLAYLIST MUSIK - PLAYTUNE")
print("=" * 40)

while True:
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
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip()
        try:
            durasi = int(input("Durasi (dalam detik): "))
            if durasi <= 0:
                print("Durasi harus berupa angka positif!")
            else:
                tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
        except ValueError:
            print("Durasi harus berupa angka!")

    elif pilihan == "2":
        tampilkan_playlist(playlist)

    elif pilihan == "3":
        print("Genre tersedia:", genre_set)
        genre_target = input("Masukkan genre yang ingin difilter: ").strip()
        hasil = filter_genre(playlist, genre_target)
        if len(hasil) == 0:
            print("Tidak ada lagu bergenre '" + genre_target + "'.")
        else:
            print("Lagu bergenre '" + genre_target + "':")
            nomor = 1
            for lagu in hasil:
                print(" " + str(nomor) + ". " + lagu[0] + " - " + lagu[1]
                      + " (" + format_durasi(lagu[3]) + ")")
                nomor += 1

    elif pilihan == "4":
        if len(playlist) == 0:
            print("Playlist masih kosong.")
        else:
            tampilkan_playlist(playlist)
            try:
                nomor = int(input("Nomor lagu yang ingin dihapus: "))
                hapus_lagu(playlist, nomor)
                genre_set.clear()
                for lagu in playlist:
                    genre_set.add(lagu[2])
            except ValueError:
                print("Nomor lagu harus berupa angka!")

    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak valid, masukkan angka 1-6.")
