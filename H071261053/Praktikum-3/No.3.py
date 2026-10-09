# PO BUS

jumlah_kursi = 0

while jumlah_kursi <= 0 :
    try :
        jumlah_kursi = int(input("Masukkan maksimal kursi bus: "))
    except :
        print("Input jumlah kursi harus berupa angka!")

print("--- Sistem Reservasi PO BUS Dimulai ---")

sisa_kursi = jumlah_kursi
pendapatan = 0

while sisa_kursi > 0 :
    print("Sisa kursi", sisa_kursi)

    try :
        umur = float(input("Masukkan umur penumpang: "))

        if umur < 0 :
            print("Umur tidak valid!")
            continue

        elif umur <= 5 :
            harga = 0
            print("Kategori: Balita - Tiket Gratis (Rp 0)")

        elif umur <= 12 :
            harga = 50000
            print("Kategori: Anak - Harga: Rp. 50.000")

        else :
            harga= 100000
            print("Kategori: Dewasa - Harga: Rp.100.000")

        sisa_kursi -= 1
        pendapatan += harga

    except : 
        print("Input umur harus berupa angka")

    print()

print("--- Semua Kursi Terisi ---")
print("Total pendapatan perjalanan PO BUS kali ini: Rp", pendapatan)
