def hitung_statistik(*args):
  """Fungsi untuk menghitung rata-rata, nilai tertinggi, dan nilai terendah

  sekaligus menggunakan Arbitrary Arguments (*args).
  """
  if not args:
    return None, None, None
  
  rata_rata = sum(args) / len(args)
  nilai_tertinggi = max(args)
  nilai_terendah = min(args)
  
  return rata_rata, nilai_tertinggi, nilai_terendah


def main():
  daftar_nilai = []
  
  while True:
    masukan = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if masukan == "":
      break
    try:
      nilai = float(masukan)
      daftar_nilai.append(nilai)
    except ValueError:
      print("Masukkan angka yang valid.")

  if len(daftar_nilai) == 0:
    print("Data nilai tidak tersedia.")
  else:
    rata, tertinggi, terendah = hitung_statistik(*daftar_nilai)
    
    def format_angka(val):
      return int(val) if val.is_integer() else val

    print(f"Rata-rata kelas: {format_angka(rata)}")
    print(f"Nilai tertinggi: {format_angka(tertinggi)}")
    print(f"Nilai terendah: {format_angka(terendah)}")



main()