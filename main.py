# import random

# secret_number = random.randint(1,10)

# while True:
#     try:
#         usser = int(input("Guess the secret number in 1 and 10: "))
#         if usser == secret_number:
#             print("Congratulations You guessed it right")
#             break
#         elif usser < secret_number:
#             print("Try a higher number")
#         else:
#             print("Try a lower number")
#     except ValueError:
#         print("Please enter a valid integer")

# print(f"The secret number was {secret_number}")



# import random

# secret_number = random.randint(1, 5)
# max_attempts = 3  

# print(f"Welcome to the Number Guessing Game! You have {max_attempts} attempts.")

# for attempt in range(max_attempts):
#     try:
#         user_guess = int(input(f"Attempt {attempt + 1}: Guess the secret number: "))
#         if user_guess == secret_number:
#             print("Congratulations! You guessed it right.")
#             break
#         elif user_guess < secret_number:
#             print("Try a higher number.")
#         else:
#             print("Try a lower number.")
#     except ValueError:
#         print("Please enter a valid integer.")

# if user_guess != secret_number:
#     print(f"Sorry, you're out of attempts. The secret number was {secret_number}. Better luck next time!")
