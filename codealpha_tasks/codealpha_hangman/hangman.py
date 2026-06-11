import random
WORDS = ["python", "hangman", "coding", "laptop", "keyboard"]
HANGMAN_STAGES = [
    # 0 wrong guesses
    """
   +---+
   |   |
       |
       |
       |
       |
=========
    """,
    # 1 wrong guess
    """
   +---+
   |   |
   O   |
       |
       |
       |
=========
    """,
    # 2 wrong guesses
    """
   +---+
   |   |
   O   |
   |   |
       |
       |
=========
    """,
    # 3 wrong guesses
    """
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========
    """,
    # 4 wrong guesses
    """
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
=========
    """,
    # 5 wrong guesses
    """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
=========
    """,
    # 6 wrong guesses  →  game over
    """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========
    """,
]
MAX_WRONG = 6
def display_state(wrong_count: int, guessed: list, secret: str) -> None:
    """Print the gallows, masked word, and used letters."""
    print(HANGMAN_STAGES[wrong_count])
    masked = " ".join(letter if letter in guessed else "_" for letter in secret)
    print(f"  Word : {masked}")
    print(f"  Wrong guesses left : {MAX_WRONG - wrong_count}")
    print(f"  Letters used       : {', '.join(sorted(guessed)) or 'none'}\n")
def get_guess(guessed: list) -> str:
    """Prompt the player for a single, unseen letter."""
    while True:
        guess = input("  Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠  Please enter a single letter.\n")
        elif guess in guessed:
            print(f"  ⚠  You already tried '{guess}'. Pick another.\n")
        else:
            return guess
def play() -> None:
    secret = random.choice(WORDS)
    guessed: list[str] = []
    wrong = 0
    print("\n" + "=" * 45)
    print("         W E L C O M E   T O   H A N G M A N")
    print("=" * 45)
    print(f"  The word has {len(secret)} letters. Good luck!\n")
    while wrong < MAX_WRONG:
        display_state(wrong, guessed, secret)
        if all(letter in guessed for letter in secret):
            print(f"  🎉  You won!  The word was '{secret}'.\n")
            return
        guess = get_guess(guessed)
        guessed.append(guess)
        if guess in secret:
            print(f"  ✔  '{guess}' is in the word!\n")
        else:
            wrong += 1
            print(f"  ✘  '{guess}' is NOT in the word. ({MAX_WRONG - wrong} chances left)\n")
    print(HANGMAN_STAGES[MAX_WRONG])
    print(f"  💀  Game over!  The word was '{secret}'.\n")
def main() -> None:
    while True:
        play()
        again = input("  Play again? (y / n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing Hangman! Bye 👋\n")
            break
if __name__ == "__main__":
    main()