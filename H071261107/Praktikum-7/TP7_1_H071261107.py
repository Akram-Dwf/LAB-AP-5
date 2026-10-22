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
        namakasir = input("Masukkan Inisial Nama Kasir: ").upper()

        sekarang = datetime.datetime.now()
        waktu = sekarang.strftime("%y%m%d%H%M")
        waktulengkap = datetime.datetime.now()
        angka_acak = random.randint(100, 999)

        idtransaksi = namakasir + waktu + str(angka_acak)
        namafile = "invoices/" + idtransaksi + ".txt"

        total = 0

        with open(namafile, "w") as file:
            file.write("========== INVOICE ==========\n")
            file.write("Kasir: " + namakasir + "\n")
            file.write("ID Transaksi: " + idtransaksi + "\n")
            file.write("Waktu: " + str(waktulengkap) + "\n")
            file.write("-----------------------------\n")

            while True:
                namaproduk = input("Masukkan Nama Produk (Kosongkan untuk selesai): ")
                if namaproduk == "":
                    break
                try:
                    hargaproduk = int(input("Masukkan Harga Produk: "))
                    jumlahproduk = int(input("Masukkan Jumlah Produk: "))
                    subtotal = hargaproduk * jumlahproduk
                    total += subtotal
                    if hargaproduk < 0 or jumlahproduk < 0:
                        print("Harga dan jumlah harus bernilai positif. Silakan coba lagi.")
                        continue
                except ValueError:
                    print("Harga dan jumlah harus berupa angka. Silakan coba lagi.")
                    continue
                file.write("Produk: " + namaproduk + "\n")
                file.write("Harga: Rp" + str(hargaproduk) + "\n")
                file.write("Jumlah: " + str(jumlahproduk) + "\n")
                file.write("Subtotal: Rp" + str(subtotal) + "\n")
                file.write("-----------------------------\n")

            file.write("Total Belanja: Rp" + str(total) + "\n")
            file.write("=============================\n")

        with open("trx_history.txt", "a") as file:
            if os.path.getsize("trx_history.txt") == 0:
                file.write("Waktu | ID Transaksi | Nominal Transaksi\n")

            file.write("| " + str(waktulengkap) + " | " + idtransaksi + " | Rp" + str(total) + "\n")

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
                print("\n" + file.read())
        else:
            print("Belum ada riwayat transaksi.")

    elif pilihan == "4":
        print("Terima kasih telah menggunakan aplikasi kasir.")
        break

    else:
        print("Pilihan tidak valid!")
