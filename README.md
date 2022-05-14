# HANGMAN The Word Guessing Game 
The hangman game is a python terminal game that is running the code institute mock terminal on Heroku.

This game allows users to guess words from a dictionary of a preset word for 3 difficulties easy, normal, and hard. The game also
has lived and you can try to play up to 6 times before the game will say that you fail. 


![Screenshot 2022-05-14 013151](https://user-images.githubusercontent.com/95313496/168403970-28846ddd-3c03-477b-967b-48bce6f5424b.jpg)


## How To Play
The rules for hangman are simple you can only use letters and nothing else and only guess one letter at a time.

This game also has the extra rule that all letters must be the lower case when guessed and the game will turn the first letter in the word into a capital.

The way this game plays will tell you how many tries you have and how many letters you have to guess. 

You win by guessing the word that the computer has chosen for you in that game.

## Features
### Existing Features
- Choose your difficulty:
  - The player is asked to choose from the three difficulties.

![Screenshot 2022-05-14 014950](https://user-images.githubusercontent.com/95313496/168404861-b0a69885-c842-477a-9ce9-b0f89314f3ba.jpg)

- Once the difficulty is chosen the player is then asked to put in a letter.
  - If the player puts in anything but a letter the game will ask for a letter.

![Screenshot 2022-05-14 020123](https://user-images.githubusercontent.com/95313496/168404985-66994e45-78fc-4303-b2aa-6bf871b2ab0a.jpg)

- The player makes a correct guess the console returns their guess on the board.
  - The console then says they guessed correctly.
  - The game then asks them to guess again.

![Screenshot 2022-05-14 020852](https://user-images.githubusercontent.com/95313496/168405225-c130eec4-47cc-415a-a51e-61c334b82d82.jpg)

- If the player gets the guess wrong they are told that it was wrong
   - That they have tried counting down from 6.
   - The game then asks for the player to retry.

![Screenshot 2022-05-14 024512](https://user-images.githubusercontent.com/95313496/168406347-6dcbd9a3-64a8-4188-99f6-81bd3f992ed9.jpg)

- When the player wins they have to guess each and every letter in the word one at a time.
  - When they do this the game says well done and the restarts letting them go again

![Screenshot 2022-05-14 030156](https://user-images.githubusercontent.com/95313496/168406901-2ed0840b-bd04-45cb-8dfc-1ecbe5fe01d1.jpg)

- When the player guesses wrong the game will give them 6 tries
  - After the 6th try the game will say that you lost
  - The game then tells the player what the word was. 

![Screenshot 2022-05-14 031409](https://user-images.githubusercontent.com/95313496/168407080-fbba0c97-08f8-41f4-9f75-7b94a42eff22.jpg)


### Future Features

- To have a visual hangman when the player goes through their lives.
- Allow players to add words to the category.
- Have topes within the difficulties.

## Data Model

I have used functions to make this game by naming them so they can interact with each other. 

I used the **choose function**to allow the user to have the choice and then that passes the user's answers through. from there the choice the user made gives that choice 
a variable of secret_word.

From there the next function gives the user the ability to interact with the game allowing them to put in a letter. it also validates the user's choice and then if they use the alphabet the choice they make is passed on to the to see if it's in the secret word if it is the guess was correct if not then they get that answer. the function returns the next function until the player has completed the loop.;

The next function checks to see if the player has won or lost and if they have not then they return to the previous function.

## Testing
- passed the code through a pep8 tester there were no issues
- invalid inputs do not work and ask for the user to put in a letter
- tested my code in the code institute Heroku terminal

## Bugs

### Solved bugs
- Corrected an issue that the serect_number arguments were in the wrong order to be called by the function so it gave them a number instead of a word 
- the game was only running 1 .5 was ending after guess so linked the last two functions and it now repeats until the correct answer or wrong answer is given.
- lose count called in globally as was not being called. 
- loss count was not reduced before it was being printed 


### Remaining bugs
- I would like to reset the tries after the program restarts as it continues with the number of tries you had from the previous game.

### Validator testing
The application was put through pep 8 online check. 

![Screenshot 2022-05-14 035856](https://user-images.githubusercontent.com/95313496/168408324-23092d87-e343-4512-9c69-53566bd110f6.jpg)

## Deployment

To deploy this project I had to use Heroku to deploy. this was difficult to understand to start off but by the end I understand it. the steps I took to deploy the project were:

1. used the console to log on to Heroku using the command: 'Heroku login -i'.
2. still in the console I had to choose the correct Heroku app using the following command: 'Heroku apps'.
3. after that I used the following command to select that app so that I could commit to it: Heroku git: 'remote -a hangmans'.
4. this is where I put the commit message to both git and heruko:'git add. && git commit -m "_input message here_"'.
5. here is where I push to both git and Heroku: 'git push origin main', 'git push Heroku main'.

## Credits
- Code institute for the deployment terminal 
- My mentor 


