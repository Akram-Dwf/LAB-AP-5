print("--- Setup Denah Bioskop NontonYuk ---")

try:
    N = int(input("Jumlah Baris : "))

    if N < 0:
            print("Angka tidak boleh kurang dari 0")
    else:
        M = int(input("Jumlah Kursi : "))
        print("--Daftar kursi tersedia--")
        
        for baris in range (1, N+1):
            for kursi in range (1, M+1):

                if kursi == 13:
                    continue

                if baris == 1 and kursi % 2== 0:
                    continue
                
                print("Baris", baris, "kursi", kursi)
except:
    print("Tidak boleh huruf")