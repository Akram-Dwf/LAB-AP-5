def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal = subtotal - (subtotal * 10/100) #Member dapat diskon 10%
    return subtotal

print("Selamat datang di Kasir Minimarket!")

status_member = input("Apakah Anda member? (y/n): ")
adalah_member = status_member == "y"

total = 0

while True:
    nama_barang = input("Masukkan nama barang (Kosongkan untuk selesai): ")

    if nama_barang == "" :
        break

    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    subtotal = hitung_subtotal(harga, jumlah, adalah_member)
    print(f"Subtotal untuk {nama_barang}: Rp {subtotal}")
    total = total + subtotal

print(f"Total belanja: Rp {total}")

