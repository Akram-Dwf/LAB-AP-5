import os
import random
from datetime import datetime

folder_saat_ini = os.path.dirname(os.path.abspath(__file__))
folder_invoice = os.path.join(folder_saat_ini, "invoices")
file_riwayat = os.path.join(folder_saat_ini, "trx_history.txt")
os.makedirs(folder_invoice, exist_ok=True)

def buat_id_transaksi(nama_kasir, waktu):
    inisial = ""

    for nama in nama_kasir.split():
        inisial += nama[0].upper()

    tahun = waktu.strftime("%y")
    bulan = waktu.strftime("%m")
    tanggal = waktu.strftime("%d")
    jam_menit = waktu.strftime("%H%M")

    angka_acak = random.randint(100, 999)

    id_transaksi = (
        inisial
        + tahun
        + bulan
        + tanggal
        + jam_menit
        + str(angka_acak)
    )

    return id_transaksi

def simpan_riwayat(waktu, id_transaksi, total):
    file_baru = not os.path.exists(file_riwayat)

    with open(file_riwayat, "a", encoding="utf-8") as file:
        if file_baru or os.path.getsize(file_riwayat) == 0:
            file.write(
                f"{'Waktu':20} | {'ID Transaksi':20} | "
                f"Nominal Transaksi\n"
            )
            file.write("-" * 75 + "\n")

        waktu_teks = waktu.strftime("%Y-%m-%d %H:%M:%S")

        file.write(
            f"{waktu_teks:20} | "
            f"{id_transaksi:20} | "
            f"Rp. {total}\n"
        )

def buat_invoice(nama_kasir, daftar_produk):
    waktu = datetime.now()
    id_transaksi = buat_id_transaksi(nama_kasir, waktu)

    total_transaksi = 0

    nama_file = os.path.join(
        folder_invoice, id_transaksi + ".txt"
    )

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("========== INVOICE ==========\n")
        file.write(f"ID Transaksi : {id_transaksi}\n")
        file.write(f"Nama Kasir   : {nama_kasir}\n")
        file.write(f"Waktu        : {waktu.strftime('%d-%m-%Y %H:%M:%S')}\n")
        file.write("-" * 65 + "\n")

        file.write(f"{'Nama Produk':20} | {'Harga':10} | "
            f"{'Jumlah':6} | {'Subtotal':10}\n"
        )

        file.write("-" * 65 + "\n")

        for produk in daftar_produk:
            nama_produk = produk["nama"]
            harga = produk["harga"]
            jumlah = produk["jumlah"]

            subtotal = harga * jumlah
            total_transaksi += subtotal

            file.write(
                f"{nama_produk:20} | "
                f"{harga:10} | "
                f"{jumlah:6} | "
                f"{subtotal:10}\n"
            )

        file.write("-" * 65 + "\n")
        file.write(f"TOTAL PEMBAYARAN: Rp. {total_transaksi}\n")
        file.write("==============================\n")

    simpan_riwayat(waktu, id_transaksi, total_transaksi)

    print("\nTransaksi berhasil!")
    print("ID Transaksi:", id_transaksi)
    print("Total pembayaran: Rp.", total_transaksi)
    print("Invoice tersimpan di:", nama_file)

def cari_invoice():
    id_transaksi = input("Masukkan ID transaksi: ").strip()

    nama_file = os.path.join(
        folder_invoice, id_transaksi + ".txt"
    )

    if os.path.isfile(nama_file):
        with open(nama_file, "r", encoding="utf-8") as file:
            isi_invoice = file.read()

        print("\n" + isi_invoice)

    else:
        print("Invoice tidak ditemukan.")

def tampilkan_riwayat():
    if os.path.isfile(file_riwayat):
        with open(file_riwayat, "r", encoding="utf-8") as file:
            isi_riwayat = file.read()

        print("\n" + isi_riwayat)

    else:
        print("Belum ada riwayat transaksi.")

print("================================")
print("     APLIKASI KASIR SEDERHANA")
print("================================")

nama_kasir = input("Masukkan nama kasir: ").strip()

while nama_kasir == "":
    print("Nama kasir tidak boleh kosong.")
    nama_kasir = input("Masukkan nama kasir: ").strip()


while True:
    print("\n========== MENU KASIR ==========")
    print("1. Buat transaksi")
    print("2. Cari invoice")
    print("3. Riwayat transaksi")
    print("4. Keluar")
    print("================================")

    pilihan = input("Pilih menu: ").strip()

    if pilihan == "1":
        daftar_produk = []

        while True:
            nama_produk = input(
                "\nNama produk (ketik selesai untuk berhenti): "
            ).strip()

            if nama_produk.lower() == "selesai":
                break

            if nama_produk == "":
                print("Nama produk tidak boleh kosong.")
                continue

            try:
                harga = int(input("Harga produk: "))
                jumlah = int(input("Jumlah beli: "))

                if harga <= 0 or jumlah <= 0:
                    print("Harga dan jumlah harus lebih dari 0.")
                    continue

            except ValueError:
                print("Harga dan jumlah harus berupa angka.")
                continue

            produk = {
                "nama": nama_produk,
                "harga": harga,
                "jumlah": jumlah
            }

            daftar_produk.append(produk)

            print("Produk berhasil ditambahkan.")

        if len(daftar_produk) > 0:
            buat_invoice(nama_kasir, daftar_produk)

        else:
            print("Transaksi dibatalkan karena belum ada produk.")

    elif pilihan == "2":
        cari_invoice()

    elif pilihan == "3":
        tampilkan_riwayat()

    elif pilihan == "4":
        print("Terima kasih telah menggunakan aplikasi kasir.")
        break

    else:
        print("Pilihan tidak valid. Pilih menu 1 sampai 4.")
