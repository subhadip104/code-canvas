import random

secret_number = random.randint(1,10)

while True:
    try:
        usser = int(input("Guess the secret number in 1 and 10: "))
        if usser == secret_number:
            print("Congratulations You guessed it right.")
            break
        elif usser < secret_number:
            print("Try a higher number")
        else:
            print("Try a lower number")
    except ValueError:
        print("Please enter a valid integer.")

print(f"The secret number was {secret_number}")
