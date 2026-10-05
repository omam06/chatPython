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

# Now calculate the average score.
total = 0
for key, student in students.items():
    total += student['score']
average = total / len(students)
print('Average Score is:', average)

#highest score
highest = 0
highest_student = 
for key, student in students.items():
    if student['score'] > highest:
        highest = student['score']
        highest_student.append(student['name'])
print(highest)
print(highest_student)