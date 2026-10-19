def maju(a, b):
    
    if a == 0:
        print(a)
        return print("MELUNCUR!!!")
    if a < 0:
        print("angka tidak valid")
        return
    
    print(a)
    a = a - 1
    
    if a >= b:
        maju(a, b)

    
    
a = int(input("Masukkan angka : "))
b = 0

maju(a, b)