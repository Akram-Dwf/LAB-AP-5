def summarize_scores(*scores):
    """Return the average, highest, and lowest of any number of scores."""
    average = sum(scores) / len(scores)
    return average, max(scores), min(scores)


scores = []
while True:
    score_input = input("Enter the student's exam scores (or enter blank to exit.): ")
    if score_input == "":
        break
    try:
        score = float(score_input)
    except ValueError:
        print("Input must be a number.")
        continue
    scores.append(score)
             
if len(scores) == 0:
    print("The score data doesn't exist.")
else:
    average, highest, lowest = summarize_scores(*scores)
    print(f"Class average: {average}")
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")