def passing_scores(scores):
    passed = []
    for each_score in range(len(scores)):  #defect 1 scores -1
        if scores[each_score] >= 50:             #2 scores[each_score] > 50
            passed.append(scores[each_score])
    return passed
print(passing_scores([49, 50, 80, 65]))

assert passing_scores([50]) == [50], 'Exactly 50 did not pass'
assert passing_scores([731]) == [731], 'Single passing score failed'
assert passing_scores([]) == [], 'Failed for an empty list'