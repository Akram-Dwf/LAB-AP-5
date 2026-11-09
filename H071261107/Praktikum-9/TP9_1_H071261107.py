class pemain:
    def __init__(self, nama, id, role, kill, assist, objective):
        self.nama = nama
        self.id = id
        self.role = role
        self.kill = kill
        self.assist = assist
        self.objective = objective

    def hitung_skor_akhir(self):
        skor = (0.3 * self.kill) + (0.3 * self.assist) + (0.4 * self.objective)
        return skor
    
    def status_performa(self):
        skor = self.hitung_skor_akhir()
        if skor >= 60:
            return "Unggul"
        elif skor < 60:
            return "Perlu Evaluasi"

    def tampilkan_data(self):
        info = {
            "Nama Pemain": self.nama,
            "ID Pemain": self.id,
            "Role Pemain": self.role,
            "Kill": self.kill,
            "Assist": self.assist,
            "Objective": self.objective,
            "Skor Akhir": f"{self.hitung_skor_akhir():.2f}",
            "Kategori": self.status_performa()
        }

        for label, nilai in info.items():
            print(f"{label}: {nilai}")
            print("-" * 35)


print("=== SISTEM PENIALAIAN PERFORMA PEMAIN ===")
jumlah = int(input("\nMasukkan jumlah pemain: "))
print("")

daftar = []

for i in range(jumlah):
    print(f"\n--- Data Pemain ke-{i+1} ---")
    nama = input("Nama: ")
    id = input("ID Pemain: ")
    role = input("Role: ")
    kill = int(input("Nilai Kill: "))
    assist = int(input("Nilai Assist: "))
    objective = int(input("Nilai Objective: "))
    
    pemain_baru = pemain(nama, id, role, kill, assist, objective)
    
    daftar.append(pemain_baru)

print("\n" + "=" * 76)
print(f"| {'NO':<3} | {'NAMA':<12} | {'ID':<10} | {'ROLE':<12} | {'SKORAKHIR':<10} | {'STATUS':<14} |")
print("-" * 76)

for indeks, p in enumerate(daftar, start=1):
    skor_format = f"{p.hitung_skor_akhir():.2f}"
    print(f"| {indeks:<3} | {p.nama.upper():<12} | {p.id:<10} | {p.role.upper():<12} | {skor_format:<10} | {p.status_performa():<14} |")

print("=" * 76)
