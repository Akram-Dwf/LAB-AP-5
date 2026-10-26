total_belanja = 0
def sistem(harga, jumlah, adalah_member=False):
    harga_jumlah = harga * jumlah
    if adalah_member:
        harga_jumlah = harga_jumlah * (1 - 0.10)
        return int(harga_jumlah)
    return int(harga_jumlah)

print("Selamat datang di kasir Minimarket!")
while True:
    status_member = input("Apakah Anda member? (y/n): ")
    if status_member == "y":
        member = 1
        break
    elif status_member == "n":
        member = 2
        break
    else:
        print("Input yang anda masukkan tidak valid")
        continue

while True:
    try:
        nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
        if nama_barang == "":
            print(f"Total belanja: {total_belanja}")
            break
        harga_barang = int(input("Harga barang: "))
        if harga_barang < 0:
            raise ValueError() #angkanya atau data benar tapi dengan nilai yang tidak masuk akal/tidak cocok
        jumlah_barang = int(input("Jumlah barang: "))
        harga_jumlah = harga_barang * jumlah_barang
        if member == 1:
            subtotal = int(harga_jumlah * (1 - 0.10))
        else:
            subtotal = harga_jumlah
        total_belanja += subtotal
        print(f"Subtotal {nama_barang}: {subtotal}")
    except:
        print("Input yang anda masukkan tidak valid!")