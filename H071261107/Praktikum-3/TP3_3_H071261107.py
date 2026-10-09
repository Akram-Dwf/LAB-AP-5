N = int(input("Masukkan maksimal kursi bus : "))

sisa = N
total = 0

while N > 0:
    umur = int(input("Masukkan umur: "))

    if umur <= 0:
        print("Umur tidak valid!")
        continue
    if umur <= 5:
        harga = 0
    elif umur <= 12:
        harga = 50000
    else:
        harga = 100000
    
    total += harga
    N -= 1
    
print ("Total Pendapatan: Rp", total)