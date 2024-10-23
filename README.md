![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

credits: YT video for formating board used some ideas > https://www.youtube.com/watch?v=cwpS_ac8uk0


BUGS:
The code board[start_row][start_col + 'i'] has an issue because 'i' should not be in quotes. It is a variable, so simply write start_col + i.

after user chooses ship places it wasnt placing 'S' on board to show where ships are >> fixed this by mofifyng  start game function = game_board.display_board(game_board.user_board)

the game was asking if user wanted h/v when user picked 1 which is unnecessary, fixed this by: 