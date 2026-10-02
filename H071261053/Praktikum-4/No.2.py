def hitung_nilai(*nilai):
    rata_rata = sum(nilai) / len(nilai)
    nilai_tertinggi = max(nilai)
    nilai_terendah = min(nilai)

    return rata_rata, nilai_tertinggi, nilai_terendah

nilai_siswa = []

while True:

    try:
        input_nilai = (input("Masukkan nilai ujian siswa (Kosongkan untuk selesai): "))

        if input_nilai == "" :
            break

        input_nilai = int(input_nilai)
        nilai_siswa.append(float(input_nilai))
        
    except ValueError:
         print("Input tidak valid. Nilai ujian harus berupa angka!")


if len(nilai_siswa) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata_rata, nilai_tertinggi, nilai_terendah = hitung_nilai(*nilai_siswa)

    print(f"Rata-rata kelas: {rata_rata}")
    print(f"Nilai tertinggi: {nilai_tertinggi}")
    print(f"Nilai terendah: {nilai_terendah}")
