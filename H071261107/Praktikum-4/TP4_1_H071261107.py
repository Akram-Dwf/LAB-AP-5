def hitung_subtotal(harga, jumlah, member=False):
    subtotal = harga * jumlah 
    if member == "y":
        subtotal = subtotal * 0.9
    else: 
        subtotal = subtotal
    
    return int(subtotal)
        
total = 0
print("Selamat datang di kasir Minimarket!")
member = input("Apakah anda Member? : ").lower()

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai) : ")
    if nama_barang == "":
            break
    harga = int(input("Harga barang : "))
    jumlah = int(input("Jumlah barang : "))
    
    subtotal = hitung_subtotal(harga,jumlah,member)
    
    total += subtotal
    
    print(f"Subtotal Roti :{subtotal}")

print(f"Total belanja : {total}")