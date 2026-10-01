def hitung_mundur(n):
    """Fungsi rekursif untuk menampilkan hitung mundur dari n hingga 0"""
    print(n)
    if n == 0:
        print("Luncurkan!")
        return
    hitung_mundur(n - 1)


def main():
    while True:
        try:
            angka_awal = int(input("Masukkan angka awal hitung mundur: "))
            if angka_awal < 0:
                print("Input tidak valid, angka tidak boleh negatif.")
            else:
                hitung_mundur(angka_awal)
                break
        except ValueError:
            print("Masukkan angka yang valid.")


main()