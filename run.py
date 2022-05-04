
#The secret word the player is trying to guess
secertword = "code"
lettersGuessed = ""

#The number of turns before the player loses
losecount = 5

#loop until the player has made too many faild tries
#will breack loop if they succeed instead
while losecount > 0:

    #get the players guessed letters
    guess = input("Enter a letter: ")

    if guess in secertword:
        #player guessed correctly
        print(f"Correct! there is {guess} more letters in the secret word.")
    else:
        losecount -= 1
        print(f"incorrect. there are no{guess} in the secert word. you have {losecount} tries left.")
