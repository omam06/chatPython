#first count cjar w/o using len()
def count_characters(text):
    if text == "":
        return 0
    else:
        return 1 + count_characters(text[1:])
# print(count_characters("hello"))  
# print(count_characters("Python")) 
# print(count_characters(""))       
# print()

#next, count appearances
def count_appearance(text, target):        #to count 2 letters "an"
    if text == "":   #or len(txt) < len(taget)
        return 0
    elif text[0] == target:        # elif text[:len(target)] == target:
        return 1 + count_appearance(text[1:], target)                #return 1 + count_appearance(text[len(target):], target)
    else:
        return count_appearance(text[1:], target)                #ret count_appearance(text[1:], target)
# print(count_appearance("banana", "a"))
# print(count_appearance("mississippi", "s"))
# print()

#reverse a str
def reverse_text(text):
    if len(text) <= 1:
        return text
    return reverse_text(text[1:]) + text[0]
# print(reverse_text("Python"))
# print(reverse_text("Ouagadougou"))
# print()

#check palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    else:
        return is_palindrome(text[1:-1])
# print(is_palindrome("madam"))
# print(is_palindrome("racecar"))
# print(is_palindrome("python"))

print("===== RECURSIVE TEXT ANALYZER =====")
some_text = input("Enter a text: ").strip().lower()
print("The text has", count_characters(some_text), "characters.")
which_char = input("Which letter(s) in the text do you wanna count? ").strip().lower()
print(which_char + " appears", count_appearance(some_text, which_char), "times in the text.")
print("In reverse order, it is: " + reverse_text(some_text))
print("Is the text a palindrome?", is_palindrome(some_text))