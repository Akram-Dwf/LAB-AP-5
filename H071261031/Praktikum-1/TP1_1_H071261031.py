menu = ["Kopi Susu", "Matcha Latte", "Americano", "Es Teh"]
harga = [18000, 22000, 15000, 5000, 3000]
jumlah = [4, 3, 5, 2]

sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]
sub_esteh_kecil = harga[4] * jumlah[3]
sub_esteh_besar = harga[3] * jumlah[3]
sub_all_esteh = sub_esteh_besar + sub_esteh_kecil
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano, sub_esteh_kecil, sub_esteh_besar]

total_seluruh = sum(subtotal_pendapatan)

BIAYA_OPERASIONAL = 15000

pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

jumlah_barang = sum(jumlah)

target_tercapai = total_seluruh > 200000 and jumlah_barang > 10

print("Subtotal Kopi: Rp", sub_kopi)
print("Subtotal Matcha: Rp", sub_matcha)
print("Subtotal Americano: Rp", sub_americano)
print("Subtotal Es Teh: Rp", sub_all_esteh)
print("Pendapatan Bersih: Rp", pendapatan_bersih)
print("Hasil Target: ", target_tercapai)
