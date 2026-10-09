print ("--- Setup denah bioskop NontonYuk ---")

while True:
    try:
        baris_total = int(input("masukkan jumlah baris: "))
        if baris_total <= 0:
                print("jumlah baris harus lebih 0!")
                continue
        break
    except:
           print("input baris harus berupa angka!")
while True:
      try:
            kursi_total = int(input("masukkan jumlah kursi perbaris: "))
            if kursi_total <=0:
                  print ("jumlah kursi harus lebih dari 0!")
                  continue
            break   
      except:
            print("input kursi harus berupa angka!")
print()
print("--- Daftar kursi tersedia ---")
for baris in range(1, baris_total + 1):
      for kursi in range(1, kursi_total + 1):
            if kursi == 13:
                  continue
            if baris == 1 and kursi % 2 == 0:
                  continue
            print(f"baris {baris} - kursi {kursi}")