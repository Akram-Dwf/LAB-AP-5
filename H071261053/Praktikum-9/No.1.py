class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        skor = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return skor

    def status_performa(self):
        skor = self.hitung_skor_akhir()
        if skor >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self):
        skor = self.hitung_skor_akhir()
        status = self.status_performa()
        return f"{self.nama:<12} | {self.id_pemain:<12} | {self.role:<12} | {skor:>10.2f} | {status:<16}"

daftar_pemain = []

print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
while True:
    try:
        jumlah_pemain = int(input("\nMasukkan jumlah pemain: "))
        if jumlah_pemain <= 0:
            print("Jumlah pemain harus lebih dari 0!")
        else:
            break
    except:
        print("Input yang anda masukkan tidak valid!")
        continue

for i in range(1, jumlah_pemain + 1):
    print(f"\n-- Data Pemain ke-{i} --")

    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")

    while True:
        try:
            nilai_kill = int(input("Nilai Kill: "))
            if nilai_kill < 0: 
                print("Nilai tidak boleh negatif!")
            else:
                break
        except ValueError:
            print("Nilai harus berupa angka!")

    while True:
        try:
            nilai_assist = int(input("Nilai Assist: "))
            if nilai_assist < 0:
                print("Nilai tidak boleh negatif!")
            else:
                break
        except:
            print("Nilai harus berupa angka!")

    while True:
        try:
            nilai_objective = int(input("Nilai Objective: "))
            if nilai_objective < 0:
                print("Nilai tidak boleh negatif!")
            else:
                break
        except:
            print("Nilai harus berupa angka!")

            
    pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)

    daftar_pemain.append(pemain)

print("\n=== REKAPITULASI PERFORMA PEMAIN ===")

print("=" * 88)
print(f"{'No':<3} | {'Nama':<12} | {'ID Pemain':<12} | {'Role':<12} | {'Skor Akhir':>10} |{'Status':<16}")
print("=" * 88)

for i, pemain in enumerate(daftar_pemain, start=1):
    print(f"{i:<3} | {pemain.tampilkan_data()}")

print("=" * 88)

