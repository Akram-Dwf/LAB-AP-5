print('\n---setup denah bioskop---\n')

while True:
    try:
        jumlah_baris = int(input('masukkan jumlah baris: '))
        if jumlah_baris <= 0:
            print('jumlah baris harus lebih dari 0!')
            continue
        jumlah_kursi = int(input('masukkan jumlah kursi per baris: '))
        if jumlah_kursi <= 0:
            print('jumlah kursi harus lebih dari 0!')
            continue
        break
    except ValueError:
            print('input harus berupa angka')

print('\n=== Daftar kursi tersedia ===\n')             
for baris in range(1, jumlah_baris + 1):
    for kursi in range(1, jumlah_kursi + 1):
        if kursi == 13:
            continue
        if baris == 1 and kursi % 2 == 0:
            continue

        print(f'baris {baris} - kursi {kursi}')            