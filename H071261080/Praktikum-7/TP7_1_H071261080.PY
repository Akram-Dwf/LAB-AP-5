import datetime
import random
import os

os.makedirs("invoices", exist_ok=True)

while True:
    print("\n===== APLIKASI KASIR =====")
    print("1. Buat Invoice")
    print("2. Cari Invoice")
    print("3. Riwayat Transaksi")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        while True:
            namakasir = input("Masukkan Nama Kasir: ").strip()
            valid = namakasir != ""
            for huruf in namakasir:
                if huruf.lower() not in "abcdefghijklmnopqrstuvwxyz ":
                    valid = False
            if valid:
                break
            print("Error! Nama kasir harus berupa huruf, tidak boleh angka.")
        inisial = ""
        for kata in namakasir.split():
            inisial += kata[0].upper()

        sekarang = datetime.datetime.now()
        waktu = sekarang.strftime("%y%m%d%H%M")
        waktulengkap = sekarang.strftime("%Y-%m-%d %H:%M:%S")
        angka_acak = random.randint(100, 999)

        idtransaksi = inisial + waktu + str(angka_acak)
        namafile = "invoices/" + idtransaksi + ".txt"
        total = 0
        with open(namafile, "w") as file:
            file.write("========== INVOICE ==========\n")
            file.write("Kasir: " + namakasir + "\n")
            file.write("ID Transaksi: " + idtransaksi + "\n")
            file.write("Waktu: " + waktulengkap + "\n")
            file.write("-----------------------------\n")

            while True:
                namaproduk = input("Masukkan Nama Produk (Kosongkan untuk selesai): ")
                if namaproduk == "":
                    break
                while True:
                    try:
                        hargaproduk = int(input("Masukkan Harga Produk: "))
                        if hargaproduk > 0:
                            break
                        print("Error! Harga tidak boleh negatif atau nol.")
                    except ValueError:
                        print("Error! Harga harus berupa angka.")
                while True:
                    try:
                        jumlahproduk = int(input("Masukkan Jumlah Produk: "))
                        if jumlahproduk > 0:
                            break
                        print("Error! Jumlah tidak boleh negatif atau nol.")
                    except ValueError:
                        print("Error! Jumlah harus berupa angka.")

                subtotal = hargaproduk * jumlahproduk
                total += subtotal
                file.write("Produk: " + namaproduk + "\n")
                file.write("Harga: Rp" + str(hargaproduk) + "\n")
                file.write("Jumlah: " + str(jumlahproduk) + "\n")
                file.write("Subtotal: Rp" + str(subtotal) + "\n")
                file.write("-----------------------------\n")

            file.write("Total Belanja: Rp" + str(total) + "\n")
            file.write("=============================\n")

        garis = "=" * 66
        with open("trx_history.txt", "a") as file:
            if os.path.getsize("trx_history.txt") == 0:
                file.write(garis + "\n")
                file.write("| Waktu | ID Transaksi | Nominal Transaksi |\n")
                file.write(garis + "\n")
            file.write("| " + waktulengkap + " | " + idtransaksi + " | Rp. " + str(total) + " |\n")
            file.write(garis + "\n")

        print("\nTransaksi Berhasil!")
        print("ID Transaksi:", idtransaksi)
        print("Invoice disimpan di:", namafile)
        print("Total Belanja: Rp" + str(total))

    elif pilihan == "2":
        idcari = input("Masukkan ID Transaksi: ")
        namafile = "invoices/" + idcari + ".txt"

        if os.path.exists(namafile):
            with open(namafile, "r") as file:
                print("\n" + file.read())
        else:
            print("Invoice tidak ditemukan!")

    elif pilihan == "3":
        if os.path.exists("trx_history.txt"):
            with open("trx_history.txt", "r") as file:
                print("\n", file.read())
        else:
            print("Belum ada riwayat transaksi.")

    elif pilihan == "4":
        print("Terima kasih telah menggunakan aplikasi kasir.")
        break

    else:
        print("Pilihan tidak valid!")