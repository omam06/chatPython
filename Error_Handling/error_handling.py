# try:
#     num1 = input("Enter 1st numnber: ")
#     num2 = input("Enter 2nd number: ")
#     firstnumber = int(num1)
#     secondnumber = int(num2)
#     result = firstnumber / secondnumber
# except ValueError:
#     print("Enter valid numnbers")
# except ZeroDivisionError as e:
#     print("Division by 0 not allowed")
#     print(type(e))
#     print(e)
# except Exception:
#     print("Something else went wrong!")
# else:
#     print(result)
# finally:
#     print("Calculation attempt completed.")

# print(issubclass(ValueError, Exception))                    #ValueError inherits from Exception

print()
try:
    num2 = int(input("Enter 2nd number: "))
    result = 10 / num2

except (ValueError, ZeroDivisionError) as e:
    print("Operation failed.")
    print(e)
    print(type(e).__name__)
except Exception as e:
    print("Something else went wrong!")
    print(e)
else:
    print(f"The answer is: {result}")
finally:
    print("Division attempt completed")
    