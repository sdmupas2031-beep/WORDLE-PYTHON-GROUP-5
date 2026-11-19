#CREATING FUNCTIONS
# Clean up any None entries just in case
for cat in STEM_WORD_BANK:
    STEM_WORD_BANK[cat] = {k: v for k, v in STEM_WORD_BANK[cat].items() if v is not None}

def choose_category():
    """Displays a menu for the user to pick a STEM category."""
    categories = list(STEM_WORD_BANK.keys())
    print(f"\n{CYAN}{BOLD}=== STEM WORDLE: SELECT A CATEGORY ==={RESET}")
    for idx, name in enumerate(categories, start=1):
        print(f"  {idx}. {name} ({len(STEM_WORD_BANK[name])} words)")
    print(f"  {len(categories) + 1}. All STEM Categories (Mixed)")

    while True:
        choice = input("\nEnter category number: ").strip()
        if choice.isdigit():
            choice_num = int(choice)
            if 1 <= choice_num <= len(categories):
                selected = categories[choice_num - 1]
                return selected, STEM_WORD_BANK[selected]
            elif choice_num == len(categories) + 1:
                # Merge all categories into one dictionary
                combined = {}
                for cat_dict in STEM_WORD_BANK.values():
                    combined.update(cat_dict)
                return "All STEM Categories", combined
        print("Invalid choice. Please enter a valid number from the menu.")
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
    result = [""] * len(secret) # Array to hold formatted letters
    secret_chars = list(secret) # Convert secret word into an array of characters

     #First loops
    for i in range(len(guess)):
        if guess[i] == secret_chars[i]:
            result[i] == f"{GREEN}{guess[i]}{RESET}"
            secret_chars[i] = None

    for i in range(len(guess)):
        if guess[i] == "":
            if guess[i] in secret_chars:
                result[i] = f"{YELLOW}{guess[i]}{RESET}"
                secret_chars[secret_chars.index(guess[i])] = None
            else:
                result[i] = f"{GRAY}{guess[i]}{RESET}"
    return " ".join(result)

    def play_game():
    max_attempts = 6
    guess_history = []
    #Loops for the attempts, sheena, note that there is no clear "board" of this so basin dili siya mu work, just re check pls
    for attempt in range(1, max_attempts + 1):
        print(f"Attempt {attempt} of {max_attempts}")
        guess = get_valid_guess(len(secret_word))

        feedback = evaluate_guess(secret_word, guess)
        guess_history.append(feedback)

        display(guess_history)
        print(f"Attempts left: {max_attempts - attempt}\n")

        if guess == secret_word:
            print(f"{GREEN} You won in {attempt} tries.{RESET}")
            return
    
    print(f"{RED}Out of tries! The word was: {secret_word}{RESET}")

if __name__ == "__main__":
    play_game()
