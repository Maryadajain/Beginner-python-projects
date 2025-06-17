import random

easy_words = ["cat","apple","tiger", "flower", "code","computer","AI","Program", "India"]
medium_words = ["elephant", "giraffe", "computer", "programming", "python", "javascript", "developer"]
hard_words = ["unstoppable","extraordinary", "unbelievable", "incomprehensible", "unpredictable", "unquestionable"]

print("Welcome to the Password Guessing Game!"
      "\nChoose a difficulty level: easy, medium, or hard.")

level= input("Enter your choice: ").lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)    
elif level == "hard":
    secret = random.choice(hard_words)  
else:
    print("Invalid choice! Defaulting to easy level.")
    secret = random.choice(easy_words)

attempts = 0
print("Guess the secret word!")

while True:
    guess= input("Enter your guess: ").lower()
    attempts += 1
    if guess == secret:
        print(f"Congratulations! You've guessed the word '{secret}' in {attempts} attempts.")
        break
    hint = ""
    for i in range(len(secret)): # Generate hint
        if i < len(guess) and guess[i] == secret[i]: # Check if the guessed character matches the secret word
            hint += guess[i] # Correct character
        else:
            hint += "_"
    
    print(f"Hint: {hint}")

print("Game Over!")




