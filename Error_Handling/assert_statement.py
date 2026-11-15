# Assert is used to check whether a condition is true.

age = 21
assert age >= 18, "Must be atleast 18 to enter"
print("Access granted!")
print()

temperature = 40
try:
    assert temperature <= 35, "Temperature is too high!"
except AssertionError as e:
    print(e)
print("Continuing program...") AssertRaisesRegex