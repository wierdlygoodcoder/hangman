import random

easy = {
     "word_1": "apple",
     "word_2": "pear",
     "word_3": "grape",
     }
# test_easy = random.choice(list(easy.values()))
normal = {
    "word_1": "green",
    "word_2": "blue",
    "word_3": "orange"
    }
# test_normal = random.choice(list(normal.values()))
hard = {
    "word_1": "water",
    "word_2": "juice",
    "word_3": "coffee"
    }
# test_hard = random.choice(list(hard.values()))
# print(test_easy, test_normal, test_hard)
difficulty = {
    "easy": easy,
    "normal": normal,
    "hard": hard
}

# The secret word the player is trying to guess
letters_guessed = ""
# The number of turns before the player loses
lose_count = 5

# loop until the player has made too many faild tries
# will breack loop if they succeed instead
choose_difficulty = input("choose you difficulty Easy Normal or Hard!!")
if choose_difficulty == "easy":
    num = random.choice(list(easy.values()))
    print(choose_difficulty, num)

while lose_count > 0:

    secert_word = num

    # get the players guessed letters
    guess = input("Enter A letter: ")
    allowed_characters = 'abcdefghijklmnopqrstuvwxyz'
    while(len(guess) != 1 or guess not in allowed_characters):
        guess = input("Thats not a letter, Enter A Letter: ")

    if guess in secert_word:
        # player guessed correctly
        print(f"Correct! there is {guess} more letters in the secret word.")
    else:
        lose_count -= 1
        print(letters_guessed)
        print(
            f"incorrect. there are no {guess} in the secert word, "
            f"You have {lose_count} tries left."
            )
    if guess in letters_guessed:
        print("You have already guessed this letter, please try again.")

    # makes a list of all letters guessed
    letters_guessed = letters_guessed + guess
    wrong_letter_count = 0

    for index, letter in enumerate(secert_word):
        if letter in letters_guessed:
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
        print(f" Well Done! the secret word was: {secert_word}. You Win")
        break


else:
    print(
        "Sorry, you failed and did not win."
        f"The word was {secert_word} Try Again"
        )
