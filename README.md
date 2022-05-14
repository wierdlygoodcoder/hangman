# HANGMAN The Word Guessing Game 
The hangman game is a python terminal game that is running the code institute mock terminal on Heroku.

This game allows users to guess words from a dictionary of a preset word for 3 difficulties easy, normal and hard. The game also
has lived and you can try to play up to 6 times before the game will say that you fail. 


![Screenshot 2022-05-14 013151](https://user-images.githubusercontent.com/95313496/168403970-28846ddd-3c03-477b-967b-48bce6f5424b.jpg)


## How To Play
The rules for hangman are simple you can only use letters and nothing else and only guess one letter at a time.

This game also has the extra rule that all letters must be the lower case when guessed and the game will turn the first letter in the word into a capital.

The way this game plays it will tell you how many tries you have and how many letters you have to guess. 

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
  - The game tbeinga hen tell the player what the word was. 

![Screenshot 2022-05-14 031409](https://user-images.githubusercontent.com/95313496/168407080-fbba0c97-08f8-41f4-9f75-7b94a42eff22.jpg)


### future features

## data model

## testing

## bugs

#### solved bugs
serect number arugements was in the wrongorder to be called by the funtion so it gave them a number inbstead of a word 

was runnuing 1 .5 was ending after guess so linked the last two functions

lose count called in globally  and was being called before it was beening reduced 
print display needed aN EMPTY print statement to print on new line
#### remaining bugs
#### validator testing

## deployment

## credits

