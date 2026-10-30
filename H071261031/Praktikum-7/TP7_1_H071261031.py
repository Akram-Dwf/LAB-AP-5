from datetime import datetime
from pathlib import Path
import random
import re


FOLDER_INVOICE = Path("invoices")
FILE_HISTORY = Path("trx_history.txt")


def siapkan_penyimpanan():
    FOLDER_INVOICE.mkdir(exist_ok=True)

    if not FILE_HISTORY.exists():
        with FILE_HISTORY.open("w", encoding="utf-8") as file:
            file.write("=" * 78 + "\n")
            file.write(
                f"| {'Waktu':19} | {'ID Transaksi':17} | {'Nominal Transaksi':25} |\n"
            )
            file.write("=" * 78 + "\n")


def minta_teks(pesan):
    while True:
        nilai = input(pesan).strip()
        if nilai:
            return nilai
        print("Input tidak boleh kosong. Silakan coba lagi.")


def minta_angka_bulat(pesan, minimum=1):

    while True:
        try:
            nilai = int(input(pesan))
            if nilai < minimum:
                print(f"Masukkan angka minimal {minimum}.")
                continue
            return nilai
        except ValueError:
            print("Input harus berupa bilangan bulat.")


def buat_id_transaksi(nama_kasir, waktu):
    kata = re.findall(r"[A-Za-z0-9]+", nama_kasir)
    inisial = "".join(k[0] for k in kata).upper()[:3]

    if not inisial:
        inisial = "KSR"
    inisial = inisial.ljust(3, "X")

    while True:
        id_transaksi = (
            f"{inisial}{waktu.strftime('%y%m%d%H%M')}"
            f"{random.randint(100, 999)}"
        )
        if not (FOLDER_INVOICE / f"{id_transaksi}.txt").exists():
            return id_transaksi


def format_rupiah(nominal):
    return f"Rp. {nominal:,}".replace(",", ".")


def buat_invoice():
    print("\n=== BUAT TRANSAKSI BARU ===")
    nama_kasir = minta_teks("Nama kasir: ")
    waktu = datetime.now()
    daftar_produk = []

    while True:
        print(f"\nProduk ke-{len(daftar_produk) + 1}")
        nama_produk = minta_teks("Nama produk: ")
        harga = minta_angka_bulat("Harga satuan (Rp): ", minimum=0)
        jumlah = minta_angka_bulat("Jumlah dibeli: ", minimum=1)

        daftar_produk.append({
            "nama": nama_produk,
            "harga": harga,
            "jumlah": jumlah,
            "subtotal": harga * jumlah,
        })

        lagi = input("Tambah produk lain? (y/n): ").strip().lower()
        if lagi != "y":
            break
            if lagi != 'n':
                print('Input tidak boleh selain y/n')


    total = sum(item["subtotal"] for item in daftar_produk)
    id_transaksi = buat_id_transaksi(nama_kasir, waktu)
    path_invoice = FOLDER_INVOICE / f"{id_transaksi}.txt"

    # Menulis invoice ke file teks
    with path_invoice.open("w", encoding="utf-8") as file:
        file.write("=" * 48 + "\n")
        file.write("                 INVOICE BELANJA\n")
        file.write("=" * 48 + "\n")
        file.write(f"ID Transaksi : {id_transaksi}\n")
        file.write(f"Waktu        : {waktu.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Nama kasir   : {nama_kasir}\n")
        file.write("-" * 48 + "\n")
        file.write(f"{'Produk':18} {'Harga':>10} {'Qty':>5} {'Subtotal':>12}\n")
        file.write("-" * 48 + "\n")

        for item in daftar_produk:
            nama = item["nama"][:18]
            file.write(
                f"{nama:18} {format_rupiah(item['harga']):>10} "
                f"{item['jumlah']:>5} {format_rupiah(item['subtotal']):>12}\n"
            )

        file.write("-" * 48 + "\n")
        file.write(f"TOTAL: {format_rupiah(total)}\n")
        file.write("=" * 48 + "\n")
        file.write("Terima kasih telah berbelanja!\n")

    # Menambahkan transaksi ke tabel riwayat
    with FILE_HISTORY.open("a", encoding="utf-8") as file:
        file.write(
            f"| {waktu.strftime('%Y-%m-%d %H:%M:%S'):19} "
            f"| {id_transaksi:17} "
            f"| {format_rupiah(total):25} |\n"
        )
        file.write("=" * 78 + "\n")

    print("\nTransaksi berhasil disimpan!")
    print(f"Invoice tersimpan di: {path_invoice}")
    print(f"Total pembayaran: {format_rupiah(total)}")
    print("\n--- INVOICE ---")
    print(path_invoice.read_text(encoding="utf-8"))


def tampilkan_riwayat():
    print("\n=== RIWAYAT TRANSAKSI ===")
    if FILE_HISTORY.exists():
        print(FILE_HISTORY.read_text())
    else:
        print("Belum ada riwayat transaksi.")

def cari_invoice():
    print("\n=== CARI INVOICE ===")
    id_transaksi = minta_teks("Masukkan ID transaksi (tanpa .txt): ").strip()

    # Pengguna boleh menempelkan .txt; program tetap menormalkan input.
    if id_transaksi.lower().endswith(".txt"):
        id_transaksi = id_transaksi[:-4]

    path_invoice = FOLDER_INVOICE / f"{id_transaksi}.txt"
    if path_invoice.is_file():
        print("\n--- INVOICE DITEMUKAN ---")
        print(path_invoice.read_text(encoding="utf-8"))
    else:
        print("Invoice tidak ditemukan. Periksa kembali ID transaksi.")



def main():
    siapkan_penyimpanan()

    while True:
        print("\n========== APLIKASI KASIR ==========")
        print("1. Buat transaksi / invoice")
        print("2. Cari invoice")
        print("3. Tampilkan riwayat transaksi")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            buat_invoice()
        elif pilihan == "2":
            cari_invoice()
        elif pilihan == "3":
            tampilkan_riwayat()
        elif pilihan == "4":
            print("Program kasir selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1 sampai 4.")


if __name__ == "__main__":
    main()
