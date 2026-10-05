scores = [80, 55, 90, 70, 45, 100]
total = 0
highest = scores[0]
lowest = scores[0]
passed = 0
failed = 0
# to get total
for score in scores:
    total += score
# to get highest score
    if score > highest:
        highest = score
# lowest score
    if score < lowest:
        lowest = score
# students who passed
    passed += 1
# those who failed
    failed += 1
average = total / len(scores)


print("Student Score AnalySIS".title())
print("----------------------")
print()
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
