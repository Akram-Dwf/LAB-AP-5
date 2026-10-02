def rekap_nilai(*nilai):
    rata = sum(nilai) / len(nilai)
    tertinggi = max(nilai)
    terendah = min(nilai)

    return rata, tertinggi, terendah

daftar_nilai = []

while True:
    nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if nilai == "":
        break
    try:
        float(nilai)

    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")
        continue
    daftar_nilai.append(float(nilai))


if len(daftar_nilai) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata, tertinggi, terendah = rekap_nilai(*daftar_nilai)

    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")