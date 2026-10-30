import os
import random
import datetime

GARIS = "=" * 40

def buat_invoice():
    daftar_belanja = []
    nama_kasir = input("Masukkan nama kasir: ")

    while True:
        try:
            nama_produk = input("Masukkan nama produk: ")
            harga_produk = int(input("Masukkan harga produk: "))
            jumlah_produk = int(input("Masukkan jumlah produk: "))
        except:
            print ("input yang anda masukkan salah")
            continue
        total_harga = harga_produk * jumlah_produk
        
        produk = {
            "nama": nama_produk,
            "harga": harga_produk,
            "jumlah": jumlah_produk,
            "total": total_harga
        }
        daftar_belanja.append(produk)  

        tambah = input("Tambah produk? (y/t): ").lower()
        if tambah == 't':
            break

    if not daftar_belanja:
        print("Belum ada produk yang diinput.")
        return

    waktu_sekarang = datetime.datetime.now()
    inisial_kasir = nama_kasir[0:2].upper()
    waktu_str_id = waktu_sekarang.strftime("%y%m%d%H%M")
    angka_acak = str(random.randint(100, 999))
    id_transaksi = f"{inisial_kasir}S{waktu_str_id}{angka_acak}" 

    if not os.path.exists("invoices"):
        os.makedirs("invoices")

    nama_file = f"invoices/{id_transaksi}.txt"

    with open(nama_file, 'w') as file_invoice:
        file_invoice.write("========================================\n")
        file_invoice.write("           INVOICE BELANJA              \n")
        file_invoice.write("========================================\n")
        file_invoice.write(f"ID Transaksi : {id_transaksi}\n")
        file_invoice.write(f"Kasir        : {nama_kasir}\n")
        file_invoice.write(f"Waktu        : {waktu_sekarang.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file_invoice.write("----------------------------------------\n")
        
        grand_total = 0
        for p in daftar_belanja:
            file_invoice.write(f"{p['nama']} (x{p['jumlah']}) : Rp {p['total']}\n")
            grand_total += p['total']
            
        file_invoice.write("----------------------------------------\n")
        file_invoice.write(f"Total Bayar  : Rp {grand_total}\n")
        file_invoice.write("========================================\n")

    waktu_str = waktu_sekarang.strftime('%Y-%m-%d %H:%M:%S')
    with open("trx_history.txt", "a") as file_history:
        file_history.write(f"{waktu_str} | {id_transaksi} | Rp {grand_total}\n")

    print(f"\nTransaksi berhasil! Invoice disimpan dengan nama {id_transaksi}.txt")

def cari_invoice():
    id_cari = input("Masukkan ID Transaksi (tanpa .txt): ")
    nama_file = f"invoices/{id_cari}.txt"
    
    try:
        with open(nama_file, 'r') as file_baca:
            print("\n" + file_baca.read())
    except:
        print(f"Error: Invoice dengan ID '{id_cari}' tidak ditemukan.")


def lihat_riwayat():
    try:
        with open("trx_history.txt", 'r') as file_riwayat:
            print("\nRIWAYAT TRANSAKSI:")
            print(file_riwayat.read())
    except:
        print("Belum ada riwayat transaksi yang tercatat.")

while True:
    print("\n" + GARIS)
    print("     SELAMAT DATANG DI LIVY STORE     ")
    print(GARIS)
    print("1. Buat Invoice Baru (Transaksi)")
    print("2. Cari dan Tampilkan Invoice")
    print("3. Lihat Riwayat Transaksi")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1-4): ")
    
    if pilihan == '1':
        buat_invoice()
    elif pilihan == '2':
        cari_invoice()
    elif pilihan == '3':
        lihat_riwayat()
    elif pilihan == '4':
        print("Terima kasih telah menggunakan aplikasi kasir!")
        break
    else:
        print("Pilihan tidak valid!")