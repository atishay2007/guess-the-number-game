import random

print("🎲 Welcome to Guess the Number! 🎲")
print("I'm thinking of a number between 1 and 100... Can you guess it?")

secret = random.randint(1, 100)
attempts = 0
guess = None

while guess != secret:
    guess_input = input("👉 Your guess: ")
    
    if not guess_input.isdigit():
        print("Bruh, that’s not even a number. Try again.")
        continue

    guess = int(guess_input)
    attempts += 1

    if guess < secret:
        print("📉 Too low, chief! Aim higher.")
    elif guess > secret:
        print("📈 Too high! Calm down, Einstein.")
    else:
        print(f"🎉 Bingo! The number was {secret}.")
        print(f"💯 You cracked it in {attempts} tries. Respect ✨")
