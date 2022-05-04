
# The secret word the player is trying to guess
secertWord = "code"
lettersGuessed = ""

# The number of turns before the player loses
losecount = 5

# loop until the player has made too many faild tries
# will breack loop if they succeed instead
while losecount > 0:

    # get the players guessed letters
    guess = input("Enter a letter: ")

    if guess in secertWord:
        # player guessed correctly
        print(f"Correct! there is {guess} more letters in the secret word.")
    else:
        losecount -= 1
        print(f"incorrect. there are no{guess} in the secert word. You have {losecount} tries left.")

    # makes a list of all letters guessed
    lettersGuessed = lettersGuessed + guess
    wrongLetterCount = 0

    for letter in secertWord:
        if letter in lettersGuessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrongLetterCount += 1

    # if there are not lossed letters then the player won
    if wrongLetterCount == 0:
        print(f"Well Done! the secret word was:{secertWord}. You Win")
        break

