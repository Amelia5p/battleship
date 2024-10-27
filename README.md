# Battleship

## Site Overview
Battleship is a two-player game where players aim to sink each other's ships by guessing their locations on an 8x8 grid. This version of the classic game has you competing against the computer in a grid-based battle to be the last one standing!



Live site:

![Responsive Site]() 



<!-- TOC end -->

<br><br>

# User Experience

## Design


### Lucid Chart


![flowchart](images/flowchart.png)

## User Stories

### First time visitor goals
* As a first time user,

### Returning visitor goals
* As a returning user, 


# Features

## Landing Page
![Landing](images/Landing.png)

## Instructions
![Instructions](images/Instructions.png)

## Username
![Username](images/Name.png)
## Display Board
![Display](images/Display.png)

## 'Hit' mark on board
[!Hit](images/hit.png)

## 'Miss' mark on board
[!Miss](images/miss.png)

## Winner messages
[!Winner](images/winner_msg.png)
[!Winner](images/winner_msg_2.png)

## Play Again
[!Play](images/play_again.png)


### Accessibility
Aria-lables, alt text, color contrast and font selections were thoughtfully chosen to ensure an inclusive and accesible user experience.

### Future features
 I would like to implement the following features in the future to allow for an improved user experience:
 - Sign up and Login feature to allow users a personalised experience.
 - Choose board size
 - Leaderboard using google sheets API
 

# Testing

## Feature Testing 

| Feature | Action | Result |
| ---|---|:---:|
| Landing Page Display | Confirm that the ASCII art logo appears as expected. | PASS |
| Display Instructions | Check that the game instructions are displayed correctly.  | PASS |
| Get User Name |Verify user can input their name and that it is properly validated.| PASS |
| Display Board |Ensure the board displays accurately for both players- ships hidden on the computer’s board.| PASS |
| Place User Ship | Validate that ships can be placed by the user with appropriate size, orientation, and positioning. | PASS |
| User Guess| Verify that valid hits (X) and misses (O) are marked correctly on the computer’s board.| PASS |
| Computer Guess|Confirm the computer can randomly guess positions on the user’s board,record hits and misses correctly.| PASS |
| Check Winner| Verify that the game correctly identifies and announces the winner when all ships of one player are sunk.| PASS |
| Clear Console| Check that the console is cleared when prompted.| PASS |
| Play Again| Ensure that the user can choose to play again or exit after the game ends.| PASS |





## Browsers Compatibility
The site was tested using Dev Tools on Google Chrome, Safari, Firefox and Edge and functions and appears as it should across all major browsers. I also tested it on an Iphone 12 mini and a Samsung Galaxy S21 ultra.

## Lighthouse Testing
The lighthouse testing was successful with scores above 90 across all pages for all four ratings (Performance, Accessibility, Best Practices and SEO).

## Code Validation
### PYTHON
PEP8



# Bugs

Debugging and problem solving was done consistently throughout the development process.

List of some issues that arose:

BUGS:
The code board[start_row][start_col + 'i'] has an issue because 'i' should not be in quotes. It is a variable, so simply write start_col + i.

after user chooses ship places it wasnt placing 'S' on board to show where ships are >> fixed this by mofifyng  start game function = game_board.display_board(game_board.user_board)

the game was asking if user wanted h/v when user picked 1 which is unnecessary, fixed this by: setting orientation to H automatically if 1 is selected 

computer ships were marked as '~' but when supposed to be hidden there were no spaces between cells where the ships were so you could tell their locations, updated with space to hide properly.

I was not fully familiar with the game so initially players could choose ship size 1 five times, implemented code to fix this to only allow one of each ship size per player.

 winner check is being triggered prematurely >> fix by separating the computer and users available sizes as once i placed all of the users ships the program would call check winner.

 play agian fun> thanks for playing and ask play again was in loop, fix by using elif statement with break



# Deployment


# Credits

 
## Other


## Code / Educational Resources


# Acknowledgements 
This is project one, created for the Code Institutes Full Stack Web Developer (eCommerce) course. I would like to thank my cohort facilitator and the Code Institute team for their support.























Happy coding!

credits: YT video for formating board used some ideas > https://www.youtube.com/watch?v=cwpS_ac8uk0
code for random computer choice inspired by : https://discuss.codecademy.com/t/excellent-battleship-game-written-in-python/430605


BUGS:
The code board[start_row][start_col + 'i'] has an issue because 'i' should not be in quotes. It is a variable, so simply write start_col + i.

after user chooses ship places it wasnt placing 'S' on board to show where ships are >> fixed this by mofifyng  start game function = game_board.display_board(game_board.user_board)

the game was asking if user wanted h/v when user picked 1 which is unnecessary, fixed this by: setting orientation to H automatically if 1 is selected 

computer ships were marked as '~' but when supposed to be hidden there were no spaces between cells where the ships were so you could tell their locations, updated with space to hide properly.

I was not fully familiar with the game so initially players could choose ship size 1 five times, implemented code to fix this to only allow one of each ship size per player.

 winner check is being triggered prematurely >> fix by separating the computer and users available sizes as once i placed all of the users ships the program would call check winner.

 play agian fun> thanks for playing and ask play again was in loop, fix by using elif statement with break