import re
sebelum = []
sesudah = []
nomor_valid = []

def validasi_nomor(nomor):
    pola = r'^08\d{8,11}'
    return bool(re.fullmatch(pola, nomor))

print('=' * 3 + ' Pembersihan Data Nomor Telepon ' + '=' * 3)
jumlah = int(input('Masukkan jumlah data: '))
for i in range(jumlah):
    print()
    nomor = input(f'Nomor ke-{i+1}: ')
    bersih = re.sub(r'[\s\-]','', nomor)
    sebelum.append(nomor)
    sesudah.append(bersih)
    if validasi_nomor(bersih):
        nomor_valid.append(bersih)

print('\n--- Hasil Pembersihan ---')
for i in range(len(sebelum)):
    print(f'\nData {i+1}:')
    print(f'Sebelum : {sebelum[i]}')
    print(f'Sesudah : {sesudah[i]}')
    if validasi_nomor(sesudah[i]):
        print('Status  : Valid')
    else:
        print('Status  : Tidak valid')

print(f'\nJumlah nomor valid: {len(nomor_valid)}')