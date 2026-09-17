chili = int(input("Spiciness level: "))
if 0 <= chili <= 10:
    print("Safe level of spiciness")
elif 11 < chili <= 40:
    print("Regular level of spiciness")
elif 41 < chili <= 70:
    print("High level of spiciness")
elif chili < 0:
    print("Invalid input")
else:
    print("Extreme level of spiciness")