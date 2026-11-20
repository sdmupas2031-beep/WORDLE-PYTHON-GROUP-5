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
def pick_random_word(category_dict):
    """Selects and returns a random (word, info_dict) pair from the chosen category."""
    word = random.choice(list(category_dict.keys()))
    return word, category_dict[word]

def get_valid_guess(word_length, word_info, hint_used):
    """Prompts the user for a valid 5-letter guess or allows typing 'HINT'."""
    while True:
        prompt = f"Enter a {word_length}-letter word"
        if not hint_used:
            prompt += " (or type 'HINT' for definition)"
        guess = input(f"{prompt}: ").strip().upper()

        if guess == "HINT":
            print(f"\n{CYAN}[HINT] ({word_info['pos']}) {word_info['def']}{RESET}\n")
            hint_used = True
            continue

        if len(guess) == word_length and guess.isalpha():
            return guess, hint_used
            print(f"Invalid input. Please enter exactly {word_length} letters.")

def evaluate_guess(secret, guess):
    """Compares the guess against the secret word and returns a color-coded string."""
    result = [""] * len(secret)
    secret_chars = list(secret)

    # First pass: Exact matches (Green)
    for i in range(len(guess)):
        if guess[i] == secret_chars[i]:
            result[i] = f"{GREEN}{guess[i]}{RESET}"
            secret_chars[i] = None
    # Second pass: Misplaced letters (Yellow) or misses (Gray)
    for i in range(len(guess)):
        if result[i] == "":
            if guess[i] in secret_chars:
                result[i] = f"{YELLOW}{guess[i]}{RESET}"
                secret_chars[secret_chars.index(guess[i])] = None
            else:
                result[i] = f"{GRAY}{guess[i]}{RESET}"

    return " ".join(result)
    

    def display_vocab_card(word, info):
        """Prints the educational breakdown of the target word."""
        print(f"\n{CYAN}--- VOCABULARY CARD ---{RESET}")
        print(f"{BOLD}{word}{RESET} ({info['pos']})")
        print(f"  {BOLD}Definition:{RESET} {info['def']}")
        print(f"  {BOLD}Example:{RESET}    \"{info['example']}\"")
        print(f"{CYAN}-----------------------{RESET}\n")
    

    def play_round(missed_words):
        """Plays a single round of STEM Wordle and records missed words."""
        category_name, category_dict = choose_category()
        secret_word, word_info = pick_random_word(category_dict)
        max_attempts = 6
        attempt = 0
        guess_history = []
        hint_aused = False
        
        print(f"\n{BOLD}Category:{RESET} {category_name}")
        print(f"Guess the {len(secret_word)}-letter STEM term in {max_attempts} tries.\n")
        
        while attempt < max_attempts:
            guess, hint_used = get_valid_guess(len(secret_word), word_info, hint_used)
            attempt += 1
            colored_feedback = evaluate_guess(secret_word, guess)
            guess_history.append(colored_feedback)
            
            print("\n--- Board ---")
            for row in guess_history:
                print(row)
            print(f"Attempts left: {max_attempts - attempt}\n")


    print(f"\n{BOLD}Category:{RESET} {category_name}")
    print(f"Guess the {len(secret_word)}-letter STEM term in {max_attempts} tries.\n")
