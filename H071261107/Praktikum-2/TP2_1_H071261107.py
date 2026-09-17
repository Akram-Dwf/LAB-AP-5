level = int(input("masukkan level"))

if level >= 70:
    print ("Level Ekstrem")
elif level >= 41:
    print ("Level Pedas")
elif level >= 11:
    print ("Level Sedang")
elif level >= 0:
    print ("Level Aman")    
else:
    print ("Level tidak valid")    