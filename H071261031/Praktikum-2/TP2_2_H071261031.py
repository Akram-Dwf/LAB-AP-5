delivery_distance = int(input("Enter the delivery distance (km): "))
tariff = 0
express = input("Express Service (Y/N): ")
if delivery_distance < 5:
    tariff += 10000
elif 5 <= delivery_distance <= 20:
    tariff += 20000
elif delivery_distance > 20:
    tariff += 35000
tariff = tariff + 15000 if express == "Y" else tariff + 0
if express != "N" and delivery_distance < 0:
    print("Invalid input")
print("Total Delivery Tariff: Rp", tariff)
