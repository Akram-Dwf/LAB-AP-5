siswa = []
def perhitungan(*nilai):
    rata_rata = sum(nilai) / len(nilai)
    nilai_tertinggi = max(nilai)
    nilai_terendah = min(nilai)
    return rata_rata, nilai_tertinggi, nilai_terendah

while True:
    try:
        nilai_ujian = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
        if nilai_ujian == "":
            break
        nilai = float(nilai_ujian)
        siswa.append(nilai)
    except:
        print("Input yang anda masukkan tidak valid")

try:
    rata_rata, nilai_tertinggi, nilai_terendah = perhitungan(*siswa)
    print(f"Rata-rata kelas: {rata_rata}")
    print(f"Nilai tertinggi: {nilai_tertinggi}")
    print(f"Nilai terendah: {nilai_terendah}")
except:
    print("Data tidak tersedia")