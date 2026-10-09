#rekapitulasi transaksi Dins Store

print("--- Rekapitulasi Transaksi Dins Store ---")
print("Ketik 0 untuk menutup toko dan mengakhiri sesi.")
print()

jumlah = 1

while jumlah != 0 :
    try :
        jumlah = int(input("Masukkan jumlah item: "))

        if jumlah < 0 :
            print("Jumlah tidak boleh negatif!")

        elif jumlah >100 :
            print("Maksimal 100 item per transaksi!")

        elif jumlah == 0 :
            print("Toko ditutup. Sesi rekap selesai.")

        else:
            print("Transaksi", jumlah, "item berhasil!")

        print()

    except :
        print("Input harus berupa angka!")
        print()

