print("Rekapitulasi Transaksi Dins Store")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi")

while True:
    input_str = input("masukkan jumlah item :")

    try:
        jumlah = int(input_str)
    except ValueError:
        print("input harus angka!")
        continue

    if jumlah == 0:
        print("toko ditutup, Sesi rekap selesai")
        break
    elif jumlah <= 0:
        print("jumlah tidak boleh negatif")
    elif jumlah >= 100:
        print("maksimal 100 item per transaksi!")
    else:
        print(f"transaksi {jumlah} item berhasil")