
class Pemain:
    def __init__(self, nama_pemain, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama_pemain = nama_pemain
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir (self):
        skor_akhir = (0.3*self.nilai_kill) + (0.3*self.nilai_assist) + (0.4*self.nilai_objective)
        return round(skor_akhir, 2)

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Evaluasi"

    def tampilkan_data(self, no):
        skor = self.hitung_skor_akhir()
        status = self.status_performa()
        print(f"| {no:<2} | {self.nama_pemain:<12} | {self.id_pemain:<12} | {self.role:<12} | {skor:<12} | {status:<16} |")


print("=== SISTEM PENILAIAN PERFORM PEMAIN ===")
while True:
    try:
        jumlah_pemain = int(input("Masukkan jumlah pemain: "))
        if jumlah_pemain <= 0:
            print("Jumlah pemain harus lebih dari 0. Silakan coba lagi.")
            continue
        break
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka bulat.")

daftar_pemain = []
for i in range(jumlah_pemain):
    print(f"\nMasukkan data pemain ke-{i+1}:")
    nama = input("Nama Pemain: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")

    while True:
        try:
            nilai_kill = float(input("Nilai Kill: "))
            nilai_assist = float(input("Nilai Assist: "))
            nilai_objective = float(input("Nilai Objective: "))
            if nilai_kill < 0 or nilai_assist < 0 or nilai_objective < 0:
                print("Data tidak valid")
                continue
            break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

    pemain = Pemain(nama,id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
    daftar_pemain.append(pemain)

garis = "-" * 85

print("=== REKAPTULASI PERFORMA PEMAIN ===")
print(garis)
print(f"| {'No':<2} | {'Nama Pemain':<12} | {'ID Pemain':<12} | {'Role':<12} | {'Skor Akhir':<12} | {'Status Performa':<16} |")
print(garis)

for i in range(len(daftar_pemain)):
    daftar_pemain[i].tampilkan_data(i+1)
print(garis)
