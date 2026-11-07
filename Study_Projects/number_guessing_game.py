import random

another_round = "yes"
while another_round == "yes":
    
    secret_number = random.randint(1, 100)
    attempts = 0

    correct_guess = False

    while not correct_guess:
        guess = input("Enter your guess: ").strip()
        try:
            valid_guess = int(guess)
        except ValueError as e:
            print("Invalid input. MUST be a number.")
            continue
        attempts += 1

        if valid_guess > secret_number:
            print("Too high, Go lower!")
        elif valid_guess < secret_number:
            print("Too low, Go higher!")
        else: #valid_guess == secret_number:
            print("Correct! You guessed right 🎉")
            correct_guess = True
            print("It took you", attempts, "attempts.")
    
    another_round = input("Would you like to play again? ").strip().lower()

    while another_round not in ["yes", "no"]:
        print("Invalid response. MUST be yes or no.")
        another_round = input("Would you like to play again? ").strip().lower()

print("Thanks for playing. Goodbye 👋")