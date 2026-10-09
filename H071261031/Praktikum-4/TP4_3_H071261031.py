import time

def countdown(number):
  if number < 0:
    return
  print(number)
  time.sleep(1)
  countdown(number - 1)

while True:
    try:
        countdown_input = int(input("Enter a number to countdown: "))
        countdown(countdown_input)
        if countdown_input < 0:
            print("Input must be greater than 0.")
            continueghn
        print("Launch!")
        break
    except ValueError:
        print("Input must be a number.")
        continue