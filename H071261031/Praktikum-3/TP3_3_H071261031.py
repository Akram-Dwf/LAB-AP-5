while True:
    try:
        max_seat = int(input("Enter the max seat in the bus: "))
    except ValueError:
        print("Input must be a number.")
        continue
 
    if max_seat <= 0:
        print("Input must be greater than 0.")
        continue
 
    break
print()
print("---- Bus Seat Reservation System Started ----")
akukaya = 0
while max_seat > 0:
    print()
    print(f"Remaining seat: {max_seat}")
    try:
        psnger_age = int(input("Enter the passenger's age: "))
    except ValueError:
        print("Input must be a number.")
        continue
    if 0 > psnger_age:
        print("Input must be greater than 0.")
        continue
    if 0 <= psnger_age <= 5:
        print("Category: Toddler - Free Ticket (Rp 0)")
        akunak = 0
    elif 6 <= psnger_age <= 12:
        print("Category: Kids - Price: Rp 50.000")
        akunak = 50000
    else:
        print("Category: Adult - Price: Rp 100.000")
        akunak = 100000
    akukaya = akukaya + akunak
    max_seat -=1
print()
print("---- All seats occupied ----")
print(f"Total bus travel revenue: Rp {akukaya}")













