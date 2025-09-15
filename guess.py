import random

print("🎲 Welcome to Guess the Number! 🎲")
print("I'm thinking of a number… can you guess it?")

# Ask player for difficulty
level = input("Choose difficulty (easy / medium / hard): ").lower()

if level == "easy":
    max_number = 50
    print("😎 Easy mode selected. Number is between 1 and 50")
elif level == "medium":
    max_number = 100
    print("🤔 Medium mode selected. Number is between 1 and 100")
else:
    max_number = 200
    print("😈 Hard mode selected. Number is between 1 and 200")

# Generate the secret number
secret = random.randint(1, max_number)

attempts = 0
guess = None

while guess != secret:
    try:
        guess = int(input("👉 Your guess: "))
        attempts += 1

        if guess < secret:
            print("📉 Too low, chief! Aim higher.")
        elif guess > secret:
            print("📈 Too high! Calm down, Einstein.")
        else:
            print(f"🎉 Bingo! The number was {secret}.")
            print(f"💯 You guessed it in {attempts} tries. Respect ✨")

    except ValueError:
        print("Bruh, that’s not even a number. Try again.")
