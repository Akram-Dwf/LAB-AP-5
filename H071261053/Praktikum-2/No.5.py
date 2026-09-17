#rekomendasi paket wisata

tujuan = input("Masukkan tujuan wisata: (pantai/pegunungan/kota): ")
waktu = input("Masukkan waktu: (pagi/malam): ")
tipe_pengunjung = input("Masukkan tipe pengunjung: (anak/dewasa): ")

match tujuan:
    case "pantai":
        if waktu == "malam":
            print("Paket rekomendasi: paket a")
        else:
            print("Tidak ada paket yang cocok")

    case "pegunungan":
        if waktu == "pagi" and tipe_pengunjung == "dewasa":
            print("Paket rekomendasi: paket b")
        elif waktu == "malam" and tipe_pengunjung == "dewasa":
            print("Paket rekomendasi: paket c")
        else:
            print("Tidak ada paket yang cocok")

    case "kota":
        if waktu == "pagi":
            print("Paket rekomendasi: paket c")
        elif waktu == "malam" and tipe_pengunjung == "dewasa":
            print("Paket rekomendasi: paket c")
        else: 
            print("Tidak ada paket yang cocok")

    case _:
        print("Tidak ada paket yang cocok")
