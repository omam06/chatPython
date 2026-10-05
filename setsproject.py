# SCHOOL ATTENDANCE ANALYZER
registered = {
    "Peter", "John", "Mary", "David",
    "Sarah", "Mike", "Jane"
}

present = {
    "John", "Mary", "Mike",
    "Daniel", "Sarah"
}

submitted_assignment = {
    "Peter", "John", "Mary",
    "Daniel"
}


absent = registered - present                         ##Part1 - set analysis
registered_present = registered & present
unregistered_present = present - registered
registered_submitted = registered & submitted_assignment
registered_not_submitted  = registered - submitted_assignment
everyone = registered | present | submitted_assignment
rate = len(registered_present) / len(registered) * 100

print('========= ATTENDANCE REPORT =========')
print('Total Students Registered:', len(registered))
print('Total Students Present:', len(present))          #Part2 - add statistics
print('Registered Students Present:', registered_present)
print(f'Attendance Rate: {rate:.2f}%')
print('Absent Students:', absent)
print('Unregistered Students Present:', unregistered_present)

print('Registered Students who submitted:', registered_submitted)
print('Registered Students who did NOT submit:', registered_not_submitted)

#Part4 - Flag unregistered ztudents who showed up
#can also use if statment - empty set considered False. non-empty is True
# if unregistered_present != set(): or if len(unreg_presnt) > 0:      can be writtten as       make warning mo useful by stating how many unregistered before saying their names
if unregistered_present:
    print('WARNING:', len(unregistered_present), 'Unregistered student(s) present.', 'Student(s):', unregistered_present)
else:
    print('No unregistered student showed up')      #program can now make decision based on contents of a set

#adding attendance status
if rate >= 80:
    print('Attendance Status: Excellent')
elif rate >= 60:
    print('Attendance Status: Good')
else:
    print('Attendance Status: Needs Improvement')
#create a set for students who need attention
needs_atention = absent | registered_not_submitted
print('The following students need attention:', needs_atention)
#what % of registered students need attention
attention_rate = len(needs_atention) / len(registered) * 100
print(f'Rate of Students who need Attention: {attention_rate:.2f}%')

if attention_rate >= 70:
    print('WARNING: State of Emergency! A great number of students need help')
elif attention_rate >= 40:
    print('Still gotta work on some students')
else:
    print('No Cause for Alarm')