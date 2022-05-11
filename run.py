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


def choose_difficulty(difficulty):
    """
    loop until the player has made too many faild tries
    will breack loop if they succeed instead
    """
    choose_difficulty = input(
        "choose you difficulty Easy, Normal or Hard!!"
        ).lower()
    while not (
        choose_difficulty == "easy"
        or choose_difficulty == "normal"
        or choose_difficulty == "hard"
    ):
        easy_word = random.choice(difficulty["easy"])
        normal_word = random.choice(difficulty["normal"])
        hard_word = random.choice(difficulty["hard"])
        choose_difficulty = input(
            "choose you difficulty Easy,Normal or Hard!!"
            ).lower()
        print(choose_difficulty, easy_word, normal_word, hard_word)


def loses(lose_count, normal_word, easy_word, hard_word, secret_word):
    """
    player gets to choose diiculty
    """
    while lose_count > 0:
        if choose_difficulty == "normal":
            secret_word = normal_word
        elif choose_difficulty == "easy":
            secret_word = easy_word
        else:
            secret_word == hard_word
    return secret_word


def guesses(secret_word, lose_count, LETTERS_GUESSED):
    """ """
    guess = input("Enter A letter: ")
    allowed_characters = "abcdefghijklmnopqrstuvwxyz"
    while len(guess) != 1 or guess not in allowed_characters:
        guess = input("Thats not a letter, Enter A Letter: ")

    if guess in secret_word:
        # player guessed correctly
        print(f"Correct! there is {guess} more letters in the secret word.")
    else:
        lose_count -= 1
        print(guess)
        print(
            f"incorrect. there are no {guess} in the secert word, "
            f"You have {lose_count} tries left."
        )
    if guess in LETTERS_GUESSED:
        print("You have already guessed this letter, please try again.")

    # makes a list of all letters guessed


def letters_guess(LETTERS_GUESSED, guess, secret_word):
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
        print(f" Well Done! the secret word was: {secret_word}. You Win")

    else:
        print(f"Sorry, you failed. The word was {secret_word} Try Again")


def main():
    """
    run all programs functions
    """
    choose_difficulty(difficulty)
    loses(
        lose_count, normal_word, easy_word, hard_word, secret_word
        )
    guesses(secret_word, lose_count, LETTERS_GUESSED)
    letters_guess(LETTERS_GUESSED, guess, secret_word)


main()
