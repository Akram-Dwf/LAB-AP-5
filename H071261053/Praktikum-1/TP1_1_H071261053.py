menu = ["kopi susu", "matcha latte", "americano"]
harga = [180000, 22000, 15000]
jumlah = [4,3,5]

sub_kopi = harga[0]*jumlah[0]
sub_matcha = harga[1]*jumlah[1]
sub_americano = harga[2]*jumlah[2]
sub_total_pendapatan = sub_kopi + sub_matcha + sub_americano

BIAYA_OPERASIONAL = 15000
pendapatan_bersih = sub_total_pendapatan -  BIAYA_OPERASIONAL

jumlah_barang = sum(jumlah)
target_tercapai = sub_total_pendapatan > 200000 and jumlah_barang > 10

print (f"pendapatan bersih: {pendapatan_bersih}")
print (target_tercapai)
print (sub_total_pendapatan)