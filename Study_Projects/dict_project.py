students = {
    'student1': {
        'name': 'John', 
        'age': 20, 
        'score': 75
    },
    'student2': {
        'name': 'Mary',
        'age': 19, 
        'score': 88
    }, 
    'student3': {
        'name': 'David',
        'age': 21, 
        'score': 62
    }
}

#show all names and scores
for key, student in students.items():
    print(f'{student["name"]} - {student["score"]}')
# print(students['student1']['name'])
print()


# Now calculate the average score.
total = 0
for key, student in students.items():
    total += student['score']
average = total / len(students)
# print('Average Score is:', average)

#highest score
highest = 0
highest_student = ""
for key, student in students.items():
    if student['score'] > highest:
        highest = student['score']
        highest_student = student['name']

#Find those who passed
passed = []
for _, student in students.items():
    if student['score'] >= 50:
        passed.append(student['name'])
    else:
        pass 

#Add a new student
students['student4'] = {'name': 'Peter', 'age': 20, 'score': 91}
print(students)

#update a students score
students['student3']['score'] = 66


#update highest score after adding new student & changing student3's score
highest = 0
highest_student = ''
for _, student in students.items():
    if student['score'] > highest:
        highest = student['score']
        highest_student = student['name']

#update avergae score as new score been added
total = 0
for _, student in students.items():
    total += student['score']

average = total / len(students)

#update list of passed students
passed = []
for _, student in students.items():
    if student['score'] >= 50:
        passed.append(student['name'])
print()

print('======== stuDeNT RePort ========'.upper())
print('Number of students:', len(students))
print('Average score:', average)
print(f'Highest scoring student and score: {highest_student} with {highest}')
print('Students who passed:', ", ".join(passed))

#Status of the Average Score
if average >= 80:
    print('Performance status: Excellent')
elif average >= 60:
    print('Performance status: Good')
else:
    ('Performance status: Needs Improvement')