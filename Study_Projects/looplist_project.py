scores = [80, 55, 90, 70, 45, 100]

total = 0
passed = 0
failed = 0
highest = scores[0]
lowest = scores[0]

for score in scores:
    total += score

    if score >= 60:
        passed += 1
    else:
        failed += 1

    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

average = total / len(scores)

print("StUDENT SCORE ANALYSIS".title())
print("-----------------------")
print("Scores:", scores)
print()
print("Total Score:", total)
print("Average Score:", round(average, 2))
print()
print("Highest Score:", highest)
print("Lowest Score:", lowest)
print()
print("Students who passed:", passed)
print("Students who failed:", failed)