import re
username_valid = []

def validasi_username(username):
    pola = r'[a-zA-Z][A-Za-z0-9_]{4,11}'
    return bool(re.fullmatch(pola, username))


print('='*3 + ' Registrasi Username '+ '='*3)
while True:
    username = input('\nMasukkan username (ketik "selesai" untuk berhenti): ')

    if username == 'SELESAI' or username == 'selesai':
        break
    if validasi_username(username):
        print('Username Tersedia!!')
        username_valid.append(username)
    else:
        print('Username Tidak Ditemukan!!')

print()
print('='*3 + ' REKAPITULASI ' + '='*3)
print('username valid: ')
print()

for i, nama in enumerate(username_valid, 1):
    print(f'{i}. {nama}')
    jumlah = len(username_valid) 
print(f'jumlah username valid: {jumlah}')
