menu = ["Kopi Susu", "Matcha Latte", "Americano", "cappucino"]
harga = [18000, 22000, 15000, 13000, 8000]
jumlah = [4, 3, 5]
BIAYA_OPERASIONAL = 15000
sub_kopi = harga [0] * jumlah [0]
sub_matcha = harga [1] * jumlah [1]
sub_americano = harga [2] * jumlah [2]
sub_cappucino = harga [3] * jumlah [1]
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano, sub_cappucino] 
total_seluruh = sum(subtotal_pendapatan)
pendapatan_bersih = (total_seluruh) - (BIAYA_OPERASIONAL)
print ("subtotal =", total_seluruh)
print ("Pendapatan bersih =",pendapatan_bersih)
if total_seluruh > 200000 and sum(jumlah) > 10:
 print ("target tercapai") 
else :
 print ("tidak tercapai")