secret_number = 8
user_guess = int(input("Guess a number: "))
if user_guess > secret_number:
    print("Your guess is too high!")
elif user_guess < secret_number:
    print("Your guess is too low!")
else:
    print("Your guess is the same as the secret number!")