tujuan = input("Tujuan (pantai/pegunungan/kota) : ")
waktu = input("pagi/malam : ")
tipepengunjung = input("anak/dewasa : ")

match tujuan:
    case "Pantai":
        if waktu == "pagi":
            print("Paket A")
        else:
            print("Paket C")
    case "Pegunungan":
        if waktu == "pagi" and tipepengunjung == "dewasa":
            print("Paket B")
        else:
            print("TIdak ada paket yang cocok")
    case "Kota":
        if waktu == "malam":
            print("Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case _:
        if waktu == "malam" and tipepengunjung == "dewasa":
            print("Paket C")


