# SUDENT SCORE PROCESSING
# find average score
def average_score(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)
scores = [45, 72, 88, 31, 95, 60]
result = average_score(scores)
print(result)


# find passing scores
def passing_scores(scores):
    passed = []
    for score in scores:
        if score >= 60:
            passed.append(score)
    return passed
new_list = passing_scores(scores)
print(new_list)

# transform the passing scores (+5 to each)
def add_bonus(new_list):
    new_scores = []
    for score in new_list:
        new_scores.append(score + 5)
    return new_scores
bonused = add_bonus(new_list)
print(bonused)

# find highest score
def highest_score(bonused):
    highest = bonused[0]
    for score in bonused:
        if score > highest:
            highest = score
    return highest
output = highest_score(bonused)
print(output)

# put our functions together
def process_scores(scores):
    passed = passing_scores(scores)
    bonused = add_bonus(passed)
    highest = highest_score(bonused)
    return highest

result = process_scores(scores)
print(result)