def show():
    print(name)
name = 'Wunna'
show()

print()
# can access global var. but not local var.
names = 'Thuggga'
def show():
    age = 47
    print(age)
show()
print(names)
#print(age)

print()
# to make func. change global var.
score = 'Keith'
def chscore():
    global score
    score = 'Metrooo'
chscore()
print(score)