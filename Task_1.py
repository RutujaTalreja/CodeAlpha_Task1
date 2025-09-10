import random

word = random.choice(["apple", "train", "house", "cloud", "chair"])
guessed = ["_"] * len(word)
attempts = 6

while attempts > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    guess = input("Letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("Wrong! Left:", attempts)

if "_" not in guessed:
    print("You win!")
else:
    print("Game over! Word was", word)
