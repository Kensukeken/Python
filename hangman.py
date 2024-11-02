import random

def get_random_word():
    words = ["python", "java", "kotlin", "javascript"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '*' for letter in word])

def hangman():
    word = get_random_word()
    guessed_letters = set()
    misses = 0

    while True:
        print("Word: " + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                print(f"Number of misses: {misses}")
                break
        else:
            guessed_letters.add(guess)
            misses += 1
            print(f"Incorrect guess. Misses: {misses}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        hangman()

if __name__ == "__main__":
    hangman()
