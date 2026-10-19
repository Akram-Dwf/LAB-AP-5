def hitung_subtotal(harga, jumlah, adalah_member=False):
    """Menghitung subtotal satu jenis barang, diskon 10% jika member."""
    subtotal = harga * jumlah
    if adalah_member:
        subtotal = subtotal * 0.9
    return int(subtotal)


def main():
    print("\n====Selamat datang di Kasir Minimarket! ====\n")
    adalah_member = input("Apakah Anda member? (y/n): ").strip().lower() == "y"
    total_belanja = 0

    while True:
        nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ").strip()
        if nama_barang == "":
            break

        try:
            harga = int(input("Harga barang: "))
            jumlah = int(input("Jumlah barang: "))
        except ValueError:
            print("input harus berupa angka!!")
            continue

        subtotal = hitung_subtotal(harga, jumlah, adalah_member)
        print(f"Subtotal {nama_barang}: Rp{subtotal}")
        total_belanja += subtotal

    print(f"Total belanja: Rp{total_belanja}")


main()