menu =["kopi", "matcha latte","Americano"]
harga =[18000, 22000, 15000]
jumlah =[4,3,5]

sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

subtotal_pendapatan = [sub_kopi, sub_matcha,sub_americano]

total_seluruh = sum(subtotal_pendapatan)
BIAYA_OPERASIONAL = 15000

pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

barang_terjual = sum(jumlah)

target_tercapai = (pendapatan_bersih > 200000) and (barang_terjual > 10)
print (target_tercapai)

print ("subtotal minuman:", subtotal_pendapatan )
print ("Pendapatan bersih:", pendapatan_bersih )
print ("hasil target:", target_tercapai )

