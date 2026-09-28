print('---- NontonYuk Cinema Seating Layout Setup ----')
while True:
    try:
        row_amnt = int(input('Enter the row(s) amount: '))
    except ValueError:
        print("Input must be a number.")
        continue
    if row_amnt <= 0:
        print("Input must be bigger than 0.")
        continue
    break
while True:
    try:
        seat_amnt = int(input('Enter the seat(s) amount: '))
    except ValueError:
        print("Input must be a number.")
        continue
    if seat_amnt <= 0:
        print("Input must be bigger than 0.")
        continue
    break
print()
print("---- List of seats available ----")
for x in range(1, row_amnt + 1):
    for y in range(1, seat_amnt + 1):
        if y == 13:
            continue
        if x == 1 and y % 2 == 0:
            continue
        print(f'Row {x} - Seat {y}')
