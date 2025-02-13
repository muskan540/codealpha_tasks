import random  

def hangman_game():
    words = ["monkey", "moon", "sunday", "programming"]
    word = random.choice(words) 
    guessed_word = ["_"] * len(word)
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word:")
    print(" ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")

        print(" ".join(guessed_word))

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over. The word was:", word)

hangman_game()