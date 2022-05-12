import random


difficulty = {
    "easy": ["apple", "pear", "grape"],
    "normal": ["green", "blue", "orange"],
    "hard": ["water", "juice", "coffee"],
}

# The secret word the player is trying to guess
LETTERS_GUESSED = ""
# The number of turns before the player loses
LOSE_COUNT = 6


def choose(difficulty):
    """
    loop until the player has made too many failed tries
    will break loop if they succeed instead
    """
    choose_difficulty = input(
        "choose you difficulty Easy, Normal or Hard!!"
        ).lower()

    easy_word = random.choice(difficulty["easy"])
    normal_word = random.choice(difficulty["normal"])
    hard_word = random.choice(difficulty["hard"])
    while not (
        choose_difficulty == "easy"
        or choose_difficulty == "normal"
        or choose_difficulty == "hard"
    ):

        choose_difficulty = input(
            "choose you difficulty Easy,Normal or Hard!!"
            ).lower()
    return [easy_word, normal_word, hard_word, choose_difficulty]


def loses(normal_word, easy_word, hard_word, choose_difficulty):
    """
    a player gets to choose difficulty
    """
    if choose_difficulty == "normal":
        secret_word = normal_word
    elif choose_difficulty == "easy":
        secret_word = easy_word
    else:
        secret_word = hard_word
    return secret_word


def guesses(secret_word, LETTERS_GUESSED):
    """
    allows users to have a guess
    """
    global LOSE_COUNT
    guess = input("Enter A letter: ")
    allowed_characters = "abcdefghijklmnopqrstuvwxyz"

    while len(guess) != 1 or guess not in allowed_characters:
        guess = input("Thats not a letter, Enter A Letter: ")
    if guess in secret_word:
        print(
            f"Correct! {guess} in the secret word."
            )
    else:
        LOSE_COUNT -= 1
        print(
            f"incorrect. there are no {guess} in the secert word,"
            f"You have {LOSE_COUNT} tries left."
        )
    if guess in LETTERS_GUESSED:
        print("You have already guessed this letter, please try again.")

    # makes a list of all letters guessed
    return win_guess(LETTERS_GUESSED, guess, secret_word)


def win_guess(LETTERS_GUESSED, guess, secret_word):
    """
    checking to see if the player has won that round
    """
    LETTERS_GUESSED = LETTERS_GUESSED + guess
    wrong_letter_count = 0
    for index, letter in enumerate(secret_word):
        if letter in LETTERS_GUESSED:
            if index == 0:
                print(f" {letter.capitalize()}", end="")
            else:
                print(f" {letter}", end="")
        else:
            print(" _ ", end="")
            wrong_letter_count += 1
    print("")
    # if there are not lossed letters then the player won
    if wrong_letter_count == 0:
        print(f"Well Done! the secret word was: {secret_word}. You Win")
    elif LOSE_COUNT == 0:
        print("YOU LOOSE!!")
        print(f"The secret word was {secret_word}")
    else:
        print("There are still letters left. Please guess another letter")
        return guesses(secret_word, LETTERS_GUESSED)


def main():
    """
    run all programs functions
    """
    easy_word, normal_word, hard_word, choose_difficulty = choose(difficulty)
    secret_word = loses(
         normal_word, easy_word, hard_word, choose_difficulty
        )
    guesses(secret_word, LETTERS_GUESSED)
    return main()


if __name__ == "__main__":
    main()
