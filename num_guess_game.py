import random
n = random.randrange(1,100)
guess = input("Enter a number: ")
while n != guess:
    if guess < n:
        print("You guessed too low.")
        guess = input("Enter a number again: ")
    elif guess > n:
        print("You guessed too high.")
        guess = input("Enter a number again: ")
    else:
        break
print("Congratulations! You guessed correctly.")