print("--- Setup Denah Bioskop ---")

while True:
    try:
        jumlah_baris = int(input("Masukkan jumlah baris:"))
        if jumlah_baris <= 0:
            print("Jumlah baris harus lebih dari 0 yaa\n")
            
        break
    except:
        print("Input baris harus berupa angka yaa\n")


while True:
    try:
        jumlah_kursi = int(input("Masukkan jumlah kursi per baris: "))
        if jumlah_kursi <= 0:
            print("Jumlah kursi harus lebih dari 0 yaa\n")
            continue
        break 
    except:
        print("Input kursi harus berupa angka yaa\n")

print("\n--- Daftar Kursi Tersedia ---")


for b in range(1,jumlah_baris + 1):
    for k in range(1, jumlah_kursi + 1):
        if k == 13:
            break
        if b == 1 and k % 2 == 1:
            continue  

        print(f"Baris {b}, Kursi {k}")