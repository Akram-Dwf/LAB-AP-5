print ("---Rekapitulasi Transaksi Dins Store---")
print ("Ketik '0' untuk menutup toko dan mengakhiri sesi.")

while True:
    try:
        jumlah = int(input("masukkan jumlah item: "))
    except : 
        print ("input harus berupa angka!")
        continue
    if jumlah == 0:
        print("toko ditutup. Sesi rekap selesai.")
        break
    elif jumlah < 0:
        print ("jumlah tidak boleh negatif")
        continue
    elif jumlah > 100:
        print("maksimal 100 item per transaksi!")
        continue
    else:
        print(f"transaksi {jumlah} item berhasil!")