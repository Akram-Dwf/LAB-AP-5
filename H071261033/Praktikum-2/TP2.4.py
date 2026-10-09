# tujuan = input("masukkan tujuan(pantai/pegunungan/kota): ")
# waktu = input("masukkan panta (pagi/malam): ")
# pengunjung = input("masukkan tipe pengunjung (anak/dewasa): ")

# match tujuan:
#     case "pantai":
#         if waktu == "pagi":
#             print("paket rekomendasi: paket A")
#         elif waktu =="malam" and pengunjung == "dewasa":
#             print("paket rekomendasi: paket C")
#         else:
#             print("tidak ada paket yang cocok")

#     case "pegunungan":
#         if waktu == "pagi" and pengunjung == "dewasa":
#             print("paket rekomendasi: paket B")
#         elif waktu == "malam" and pengunjung == "dewasa":
#             print("paket rekomendasi: paket C")
#         else:
#             print("tidak ada paket yang cocok")

#     case "kota":
#         if waktu == "malam":
#             print("paket rekomendasi: C")
#         else:
#             ("tidak ada paket yang cocok")

#     case _:
#         print("tidak ada paket yang cocok")

tujuan = input("masukkan tujuan (pantai/pegunungan/kota): ")
waktu = input("masukkan waktu (pagi/malam): ")
pengunjung = input("masukkan tipe pengunjung (anak/dewasa): ")

match tujuan:
    case "pantai":
        if waktu == "pagi":
            print("paket A")
        elif waktu == "malam" and pengunjung == "dewasa":
            print("paket C")
        else:
            print("tidak ada paket yang cocok")

    case "pegunungan":
        if waktu == "pagi" and pengunjung == "dewasa":
            print("paket B")
        elif waktu == "malam" and pengunjung == "dewasa":
            print("paket C")
        else:
            print("tidak ada paket yang cocok")

    case "kota":
        if waktu == "malam":
            print("paket C")
        else:
            print("tidak ada paket yang cocok")

    case _:
        print("tidak ada paket yang cocok")
