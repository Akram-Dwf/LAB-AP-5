while True:
    try:
        sisa_kursi = int(input("masukkan maksimal kursi bus:"))
        if sisa_kursi  <= 0:
            print("jumlah kursi harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("input jumlah kursi harus berupa angka!")

print("sistem reservasi PO BUS dimulai")
total_pendapatan = 0

while sisa_kursi > 0:
    print(f"sisa kursi: {sisa_kursi}")

    try:
        umur = int(input("masukkan umur penumpang: "))
    except ValueError:
        print("input umur harus berupa angka!")
        continue

    if umur < 0:
        print("umur tidak valid!")
        continue

    if 0 <= umur <= 5:
        harga = 0
        print("kategori: balita - tiket gratis (Rp 0)")
    elif 6 <= umur <= 12:
        harga = 5000
        print("kategori: anak - harga: Rp 50.000")
    else:
        harga = 100000
        print("kategori: dewasa - harga: Rp 100.000")

    total_pendapatan += harga
    sisa_kursi -= 1

print("semua kursi terisi")
print(f"total pendapatan perjalanan PO BUS kali ini: Rp{total_pendapatan}")