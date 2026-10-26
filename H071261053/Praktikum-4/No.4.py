def konversi_suhu(suhu, asal, tujuan):
    if asal not in ["C", "F", "K"] or tujuan not in ["C", "F", "K"]:
        raise ValueError("Skala suhu tidak dikenali.")

    if asal == tujuan :
        return suhu
    elif asal == "C" and tujuan == "F":
        return (suhu * 9/5) + 32
    elif asal == "C" and tujuan == "K":
        return suhu + 273.15
    elif asal == "F" and tujuan == "C":
        return (suhu - 32) * 5/9
    elif asal == "F" and tujuan == "K":
        return (suhu - 32) * 5/9 + 273.15
    elif asal == "K" and tujuan == "C":
        return suhu - 273.15
    elif asal == "K" and tujuan == "F":
        return (suhu - 273.15) * 9/5 + 32

print("==== Konversi Suhu ===")

while True:

    try:
        input_suhu = input("Masukkan suhu (atau 'selesai'untuk keluar): ")
    
        if input_suhu == "selesai":
            break

        if input_suhu == "" :
            print("Input tidak valid. Suhu tidak boleh kosong!")
            continue

        input_suhu = float(input_suhu)

    except ValueError:
        print("Input tidak valid. Suhu harus berupa angka!")

    suhu = float(input("Masukkan suhu atau 'selesai' untuk keluar: "))
    asal = input("Masukkan skala asal (C/F/K): ").upper()
    tujuan = input("Masukkan skala tujuan (C/F/K): ").upper()

    try:
        hasil = konversi_suhu(suhu, asal, tujuan)
        print(f"Hasil: {suhu} {asal} = {hasil} {tujuan}")
    except ValueError as error:
        print(f"Error: {error}")