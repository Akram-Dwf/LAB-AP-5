from datetime import datetime
import random
import os


def buat_id_transaksi(nama_kasir):
    kata = nama_kasir.split()
    insisial = ""
    for i in kata:
        insisial += i[0].upper()

    sekarang = datetime.now()
    tanggal_waktu = sekarang.strftime("%y%m%d%H%M")
    acak = random.randint(100,999)

    return insisial + tanggal_waktu + str(acak)

def cari_invoice(id_cari):
    alamat = "invoices/" + id_cari + ".txt"
    if os.path.exists(alamat) == True:
        with open(alamat, "r") as file:
            isi = file.read()
            print(isi)
    else:
        print("invoice tidak ditemukan")

def buat_transaksi():      

    nama = input("masukkan nama kasir: ")
    simpan_id = buat_id_transaksi(nama)
    os.makedirs("invoices", exist_ok=True)
    keranjang = []

    while True:
        produk = input('masukkan nama produk (tekan enter jika selesai): ')
        if produk == '':
            break
        try:
            harga = int(input('masukkan harga barang: '))
            jumlah = int(input('masukkan jumlah produk: '))
            keranjang.append([produk, harga, jumlah])
            
        except ValueError:
            print("input harus angka, input diulang")
            continue


    total = 0
    for a in keranjang:
        total += a[1] * a[2]

    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alamat = "invoices/" + simpan_id + ".txt"

    with open(alamat, "w") as file:
        file.write("===== INVOICE =====\n")
        file.write(f"ID Transaksi : {simpan_id}\n")
        file.write(f"Kasir        : {nama}\n")
        file.write(f"Waktu        : {waktu}\n")
        file.write("-------------------\n")
        for a in keranjang:
            subtotal = a[1] * a[2]
            file.write(f"{a[0]} | Rp. {a[1]} x {a[2]} = Rp. {subtotal}\n")
        file.write("-------------------\n")
        file.write(f"TOTAL : Rp. {total}\n")

    sudah_ada = os.path.exists("trx_history.txt")
    nominal = f"Rp. {total}"
    with open("trx_history.txt", "a") as history:
        if not sudah_ada:
            history.write("=" * 65 + "\n")
            history.write(f"| {'Waktu':<19} | {'ID Transaksi':<18} | {'Nominal Transaksi':<18} |\n")
            history.write("=" * 65 + "\n")
        history.write(f"| {waktu:<19} | {simpan_id:<18} | {nominal:<18} |\n")
        history.write("=" * 65 + "\n")

def  history():
    with open("trx_history.txt", "r") as h:
        buka = h.read()
        print(buka)



while True:
    print("="*10 + "MENU KASIR" + "="*10)
    print("1. buat Transaksi")
    print("2. Cari invoice")
    print("3. buka history")
    print("4. keluar")

    pilihan = input("pilihan menu: ")
    if pilihan == "1":
        buat_transaksi()
    elif pilihan == "2":
        id_cari = input("masukkan nama id: ")
        cari_invoice(id_cari)
    elif pilihan == "3":
        history()
    elif pilihan == "4":
        print("="*10 + " TERIMA KASIH TELAH BERBELANJA " + "="*10)
        break
    else:

        print()
        print("PESAN TIDAK VALID")
        print(f"input '{pilihan}' tidak ditemukan")
        print()
        continue