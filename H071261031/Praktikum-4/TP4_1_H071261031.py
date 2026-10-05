def calculate_subtotal(price, quantity, is_member=False):
    """Calculate the subtotal for one item; members get a 10% discount."""
    subtotal = price * quantity
    if is_member:
        subtotal = subtotal * 90 // 100
    return subtotal

print("Welcome to the Minimarket Cashier!")
status = input("Are you a member? (y/n): ")
is_member = status.strip().lower() == "y"

total = 0
while True:
    item_name = input("Enter the item name (or enter blank to exit.): ")
    if item_name == "":
        break
    price = int(input("Item price: "))
    quantity = int(input("Item amount: "))

    subtotal = calculate_subtotal(price, quantity, is_member)
    print(f"Subtotal {item_name}: Rp{subtotal}")
    total += subtotal

print(f"Total price: Rp{total}")