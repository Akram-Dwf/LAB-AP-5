menu = ["kopi susu", "matcha latte", "americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopiSusu = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

totalCupTerjual = sum(jumlah)

subTotalPendapatan = [sub_kopiSusu, sub_matcha, sub_americano]
pendapatanKotor = sum(subTotalPendapatan)

BIAYA_OPERASIONAL = 15000
pendapatanBersih = pendapatanKotor - BIAYA_OPERASIONAL

targetTercapai = pendapatanKotor > 200000 and totalCupTerjual > 10

print("Pendapatan bersih:", pendapatanBersih)
print("Target tercapai:", targetTercapai)