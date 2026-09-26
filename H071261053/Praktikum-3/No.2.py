#Denah Kursi Bioskop

print("--- Setup Denah Bioskop NontonYuk ---")

jumlah_baris = 0

while jumlah_baris <= 0 :
    try :
        jumlah_baris = int(input("Masukkan jumlah baris: "))

        if jumlah_baris <= 0 :
            print("Jumlah baris harus lebih dari 0!")

    except :
        print("Input baris harus berupa angka!")

        print()

jumlah_kursi = int(input("Masukkan jumlah kursi per baris: "))

print("--- Daftar Kursi Tersedia ---")

baris = 1

while baris <= jumlah_baris :

    kursi = 1

    while kursi <= jumlah_kursi :

        if kursi == 13 :
            kursi += 1
            continue

        if baris == 1 and kursi % 2 == 0:
            kursi += 1
            continue

        print("baris", baris, "kursi", kursi)

        kursi += 1
        
    baris += 1
