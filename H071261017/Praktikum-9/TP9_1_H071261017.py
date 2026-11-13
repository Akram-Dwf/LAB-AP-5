class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objektif):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objektif = nilai_objektif


    def hitung_skor_akhir(self):
        return (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objektif)
    
    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "unggul"
        return "perlu evaluasi"
        
    def tampilkan_data(self, no):
        status = self.status_performa()
        skor = self.hitung_skor_akhir()
        return f'| {no:<4} | {self.nama:^14} | {self.id_pemain:<12} | {self.role:<10} | {skor:<10.2f} | {status}'

def main():
    print('===== Sistem penilaian performa pemain =====')

    while True:
        try:
            jumlah_pemain = int(input('masukkan jumlah pemain: '))
            if jumlah_pemain < 0:
                raise ValueError
            break
        except ValueError:
            print('input harus berupa bilangan bulat non-negatif')
    data_pemain = []


    for i in range(jumlah_pemain):
        print(f'-- data pemain ke-{i+1}')
        print()
        while True:
            try:
                nama = input('Nama: ')
                id_pemain = input('ID pemain: ')
                role = input('Role: ')
                kill = float(input('Nilai kill: '))
                assist = float(input('Nilai Assist: '))
                objektif = float(input('Nilai Objektif: '))
                break
            except ValueError:
                print('Nilai kill, assist, dan objektif harus berupa angka. Silakan masukkan ulang data pemain.')

        pemain_baru = Pemain(nama, id_pemain, role, kill, assist, objektif)
    
        data_pemain.append(pemain_baru)

    print('===== REKAPITULASI PERFORMA PEMAIN =====')
    print(f"| {'no':<4} | {'nama: ':<14} | {'id pemain: ':<12} | {'role: ':<10} | {'skor:':<10} | {'status:'}")

    for i, pemain in enumerate(data_pemain, start=1):
        print(pemain.tampilkan_data(i))

    print('-' * 75)
main()