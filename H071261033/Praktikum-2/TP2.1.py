level_pedas = int(input("masukkan presentase cabai :"))

if level_pedas >= 0 and level_pedas <= 10:
    print("level aman")
elif level_pedas >= 11 and level_pedas <= 40:
    print("level sedang")
elif level_pedas >= 41 and level_pedas <= 70:
    print("level pedas")
elif level_pedas >= 70:
    print("level ekstrem")
else:
    print("invalid")
 