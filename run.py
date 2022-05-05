# The secret word the player is trying to guess
secertWord = "code"
lettersGuessed = ""

# The number of turns before the player loses
losecount = 5

# loop until the player has made too many faild tries
# will breack loop if they succeed instead
while losecount > 0:

    # get the players guessed letters
    guess = input("Enter A letter: ")
    allowedCharacters='abcdefghijklmnopqrstuvwxyz'
    while(len(guess) != 1 or guess not in allowedCharacters):
        guess = input("Thats not a letter, Enter A Letter: ")

    if guess in secertWord:
        # player guessed correctly
        print(f"Correct! there is {guess} more letters in the secret word.")
    else:
        losecount -= 1
        print(f"incorrect. there are no {guess} in the secert word. You have {losecount} tries left.")

    # makes a list of all letters guessed
    lettersGuessed = lettersGuessed + guess
    wrongLetterCount = 0

    for letter in secertWord:
        if letter in lettersGuessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrongLetterCount += 1
    print("")
    # if there are not lossed letters then the player won
    if wrongLetterCount == 0:
        print(f" Well Done! the secret word was: {secertWord}. You Win")
        break
else:
    print(f"Sorry, you failed and did not win. the word was {secertWord} Try Again")
