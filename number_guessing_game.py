import random

# Number Guessing Game
print("🎯 Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 100.")

secret = random.randint(1, 100)  # Random number
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    try:
        guess = int(input(f"\nEnter guess ({max_attempts - attempts} left): "))
    except ValueError:
        print("❌ Invalid input! Enter a number.")
        continue

    if not 1 <= guess <= 100:
        print("❌ Number must be between 1 and 100.")
        continue

    attempts += 1

    if guess == secret:
        print(f"🎉 Correct! You guessed it in {attempts} tries.")
        break
    elif guess < secret:
        print("📈 Too low!")
    else:
        print("📉 Too high!")

if guess != secret:
    print(f"😔 Game Over! The number was {secret}")