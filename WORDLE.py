import random

# Standard ANSI Color Codes (Built-in, works in OnlineGDB!)
GREEN = "\033[92m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
RED = "\033[91m"
RESET = "\033[0m"

# 1. ARRAYS (Lists in Python)
WORD_BANK = [
    "APPLE", "BRAVE", "CRANE", "DRIVE", "EAGLE",
    "FLAME", "GRAPE", "HOUSE", "INPUT", "JOKER"
]

# 2. FUNCTIONS
def pick_random_word(words):
    """Selects and returns a random word from the array."""
    return random.choice(words)

def get_valid_guess(word_length):
    """Prompts the user until they enter a valid 5-letter alphabetic guess."""
    while True:
        guess = input(f"Enter a {word_length}-letter word: ").strip().upper()
        if len(guess) == word_length and guess.isalpha():
            return guess
        print(f"Invalid input. Please enter exactly {word_length} letters.")

def evaluate_guess(secret, guess):
    """Compares the guess against the secret word and returns a color-coded string."""
    result = [""] * len(secret)       # Array to hold formatted letters
    secret_chars = list(secret)       # Convert secret word into an array of characters

    # First pass: Check for exact matches (Green)
    for i in range(len(guess)):
        if guess[i] == secret_chars[i]:
            result[i] = f"{GREEN}{guess[i]}{RESET}"
            secret_chars[i] = None    # Mark character as used

    # Second pass: Check for misplaced letters (Yellow) or misses (Gray)
    for i in range(len(guess)):
        if result[i] == "":           # Skip letters already marked Green
            if guess[i] in secret_chars:
                result[i] = f"{YELLOW}{guess[i]}{RESET}"
                secret_chars[secret_chars.index(guess[i])] = None
            else:
                result[i] = f"{GRAY}{guess[i]}{RESET}"

    return " ".join(result)

def play_game():
    """Main game loop managing attempts, history, and win/loss states."""
    secret_word = pick_random_word(WORD_BANK)
    max_attempts = 6
    attempt = 0
    guess_history = []                # Array to store previous color-coded guesses

    print("=== PYTHON WORDLE ===")
    print("Guess the 5-letter word in 6 tries.\n")

    # 3. ITERATIVE CONTROL STRUCTURE (Main Game Loop)
    while attempt < max_attempts:
        guess = get_valid_guess(len(secret_word))
        attempt += 1

        colored_feedback = evaluate_guess(secret_word, guess)
        guess_history.append(colored_feedback)

        print("\n--- Board ---")
        for row in guess_history:
            print(row)
        print(f"Attempts left: {max_attempts - attempt}\n")

        if guess == secret_word:
            print(f"{GREEN}You won in {attempt} tries!{RESET}")
            return

    print(f"{RED}Out of tries! The word was: {secret_word}{RESET}")

if __name__ == "__main__":
    play_game()