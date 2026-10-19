def hitung_mundur(n):
    if n == 0:
        print(0)
        print("Luncurkan!")
        return

    print(n)
    hitung_mundur(n-1)

def main():
    n = int(input("Masukkan angka awal menghitung mundur: "))

    if n < 0 :
        print("Input tidak valid, angka tidak boleh negatif.")
        main()
        return

    hitung_mundur(n)

main ()