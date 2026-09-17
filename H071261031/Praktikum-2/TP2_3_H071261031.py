test_sc = int(input("Enter the test score: "))
if test_sc >= 80:
    print("You pass to the interview stage")
elif 65 < test_sc < 80:
    worke = int(input("Enter work experience (years): "))
    if worke >= 2:
        print("You pass with a condition")
    else:
        print("You failed.")
else:
    print("You failed.")


