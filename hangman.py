import random
words = ["code","bug","intern","dev","app"]
word = random.choice(words)
guessed_word = ["-"]*len(word)
incorrect_guesses = 0
maximum_guesses = 6
guessed_letters = []
while True:
    print("\n Current word "+" ".join(guessed_word))
    guess = input("Guess a letter").lower()
    if guess in guessed_letters:
        print("You already guessed this letter")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("corret guess")
        for i in range(len(word)):
            if word[i] == guess:guessed_word[i] = guess
    else:
         print("oops! incorrect guess")
         incorrect_guesses+=1
         print(f"dont give up! you still have {maximum_guesses-incorrect_guesses}chances left")
    if "-" not in guessed_word:
                    print("\n congratulations ! you guess the correct word",word)
                    break
    if incorrect_guesses==maximum_guesses:
                    print("\n Game Over,better luck next time!the correct word was",word)
                    break