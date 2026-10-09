while True:
    try:
        item_amnt = int(input("Enter the amount of item(s): "))
    except ValueError:
        print("Input should be a number")
    if item_amnt == 0:
        print("Shop closed, recap session finished.")
        break
    elif 0 < item_amnt <= 100:
        print(f"Transaction for {item_amnt} item(s) successful.")
    elif item_amnt < 0:
        print("The amount can't be negative.")
    elif item_amnt > 100:
        print('Maximum of 100 items per transaction.')
    
