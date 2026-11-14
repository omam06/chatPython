try:
    number = int(input("Enter a number: "))
   
except ValueError:
    print("Invalid number!")

except ZeroDivisionError:
    print("Division by 0 not allowed")

else:
    result = 100 / number
    print(result)
finally:
    print("Program completed.")
print("Thats it!")