import random
from random import randint, choice
import os


def get_user_name():
    """
    A function to ask for the users name
    """
    print("Welcome to Battleship! \n")
    user_name = input("Please enter your name: \n")
    print(f"Hello {user_name}, enjoy the game!!\n")


class Board:
    
    """ A class to represent the game board for Battleship-
        Initialises default board sizes of 8 with 5 ships, has lists to store guesses and ships.
        Boards are initialized with '~', lists to store user and computer ship positions.

    """

    def __init__(self):
        self.board_size= 8
        self.user_board= [['~' for _ in range(8)] for _ in range(8)]
        self.computer_board= [['~' for _ in range(8)] for _ in range(8)]
        self.num_ships= 5
        self.user_positions=[]
        self.user_guesses=[]
        self.computer_positions=[]
        self.computer_guesses=[]
        self.user_selected_sizes = []
        self.computer_selected_sizes=[]

    def display_board(self,board, is_computer=False) :
        """ Display board format, 
            Iterate over each row and column in the board print (1-8)
            Hides ships if it is the computers board"""
        
        print('   A B C D E F G H ')
        print( '   ***************')

        for row_num in range(self.board_size):
            print(f"{row_num + 1}|", end=' ')

            for col_num in range(self.board_size):
                cell_value= board[row_num][col_num] 

                if is_computer and cell_value == 'S':
                    print('~', end=' ')  # Display water symbol #This will hide ships with '~'
                else: 
                    print(cell_value, end=' ')
            print()
        print()


def place_user_ship(game_board, available_sizes):
    """
    Ask user what size ship, what orientation, and what coordinates they want.
    Input validation implemented.
    """
    while True:
        try:
            # Display available ship sizes for user selection
            print(f"Available ship sizes: {available_sizes}")
              # Prompt user to select ship size (1 to 5)
            ship_size = int(input("What size do you want your ship? (1 to 5): "))
            if ship_size in available_sizes:
                print(f"Great choice, your ship size is {ship_size}!")
                # Add chosen ship size to user's selected sizes and remove it from available sizes
                game_board.user_selected_sizes.append(ship_size)
                available_sizes.remove(ship_size)

                # Set orientation automatically if ship size is 1 (no orientation needed)
                if ship_size == 1:
                    orientation = 'H'
                    print("Since your ship size is 1, orientation is not necessary")
                else:
                    while True:
                        orientation = input("Do you want to place your ship horizontally or vertically? (H/V): ").upper()
                        # Validate orientation input
                        if orientation in ['H', 'V']:
                            print(f"Your ship will be placed {orientation}.")
                            break
                        else:
                            print("Invalid input. Please enter 'H' for horizontal or 'V' for vertical.")

                while True:
                    coordinates = input("Enter desired coordinates (e.g., A1, B5): ").upper()
                    # Validate that coordinates follow correct format and fall within board limits
                    if len(coordinates) == 2 and coordinates[0] in 'ABCDEFGH' and coordinates[1] in '12345678':
                        col = ord(coordinates[0]) - ord('A')
                        row = int(coordinates[1]) - 1 
                        
                        # Check if the chosen location can accommodate the ship
                        if can_place_ship(game_board.user_board, ship_size, orientation, row, col):
                            place_ship(game_board.user_board, ship_size, orientation, row, col)
                            print(f"Your ship has been placed at {coordinates}.")
                            game_board.user_positions.append((ship_size, orientation, row, col))
                            # Return the details of the placed ship
                            return ship_size, orientation, coordinates
                        else:
                            print("Cannot place ship here. It goes out of bounds or overlaps another ship.")
                    else:
                        print("Invalid input. Please enter coordinates in the format 'Letter (A-H) followed by Number (1-8)'.")
            else:
                print('You have already chosen this size. Please enter an available ship size.')
        except ValueError:
            print("Invalid input. Please enter a valid integer.")




def place_ship(board, ship_size, orientation, start_row, start_col):
    """ Place a ship on the board based on what the user chooses. """
    if orientation == 'H':
        for i in range(ship_size):
            board[start_row][start_col + i] = 'S'
    elif orientation == "V":
        for i in range(ship_size):
            board[start_row + i][start_col] = 'S'
    return (ship_size, orientation, start_row, start_col)


def can_place_ship(board, ship_size, orientation, start_row, start_col):
    """ Checks if ship can be placed without overlapping """
    if orientation == 'H':
        if start_col + ship_size > len(board[0]):
            return False
        for i in range(ship_size):
            if board[start_row][start_col + i] != '~':
                return False
    elif orientation == "V":
        if start_row + ship_size > len(board):
            return False
        for i in range(ship_size):
            if board[start_row + i][start_col] != '~':
                return False
    return True



def place_computer_ship(game_board, computer_available_sizes):
    """
    Randomly selects ship size, orientation, and coordinates for the computer.
    Ensures that ships are placed within bounds and do not overlap.
    """
    while True:
        # Randomly pick a ship size from available sizes
        ship_size = random.choice(computer_available_sizes)
        game_board.computer_selected_sizes.append(ship_size)
        computer_available_sizes.remove(ship_size)
        
        # Randomly decide orientation
        orientation = 'H' if ship_size == 1 else random.choice(['H', 'V'])
        
        # Generate random starting coordinates
        while True:
            row = random.randint(0, game_board.board_size - 1)
            col = random.randint(0, game_board.board_size - 1)
            
            # Check if ship can be placed at the selected coordinates
            if can_place_ship(game_board.computer_board, ship_size, orientation, row, col):
                place_ship(game_board.computer_board, ship_size, orientation, row, col)
                game_board.computer_positions.append((ship_size, orientation, row, col))
                print(f"Computer placed ship of size {ship_size} at ({row}, {col}) with orientation {orientation}.")
                return ship_size, orientation, (row, col)


                


def user_guess(game_board):
    """Allows user to guess a position on the computer's board"""
    while True:
        guess = input("Enter your guess (e.g., A1, B5): ").upper()

        if len(guess) == 2 and guess[0] in 'ABCDEFGH' and guess[1] in '12345678':
            col = ord(guess[0]) - ord('A')
            row = int(guess[1]) - 1

            if (row, col) in game_board.user_guesses:
                print("You already guessed this location. Try again.")
            else:
                game_board.user_guesses.append((row, col))

                if game_board.computer_board[row][col] == 'S':
                    print("It's a hit!")
                    game_board.computer_board[row][col] = 'X' 
                else:
                    print("You missed!")
                    game_board.computer_board[row][col] = 'O'  
                break
        else:
            print("Invalid input. Please enter coordinates in the format 'Letter (A-H) followed by Number (1-8)'.")



def computer_guess(game_board):
    """ Allows computer to guess a random position on the computer's board """
    while True:
        row= randint(0, game_board.board_size -1)
        col= randint(0, game_board.board_size -1)

        if (row,col) not in game_board.computer_guesses:
            game_board.computer_guesses.append((row, col))

            if game_board.user_board[row][col] == 'S':
                print("The computer has hit your ship")
                game_board.user_board[row][col] = 'X'
            
            else: 
                print('The computer has missed')
                game_board.user_board[row][col] = 'O'
            break
        


def check_winner(game_board):
    """ Checks if either player has lost all of their ships """
    user_ships_remaining = sum(row.count('S') for row in game_board.user_board)
    computer_ships_remaining = sum(row.count('S') for row in game_board.computer_board)


    if user_ships_remaining == 0:
        return "The computer has sunk all of your ships."
    elif computer_ships_remaining == 0:
        return "Congratulations! You have sunk all of the computer's ships."
    return None

def clear_console():
    """ Clears console """
    os.system('cls' if os.name == 'nt' else 'clear')


def start_game():  
    get_user_name()
    game_board = Board()
    
    available_sizes = [1, 2, 3, 4, 5]
    computer_available_sizes= [1, 2, 3, 4, 5]

    print('___USER BOARD:')
    game_board.display_board(game_board.user_board)
    print('___COMPUTER BOARD:')
    
    for _ in range(len(available_sizes)):
        place_user_ship(game_board, available_sizes)
        print('___USER BOARD AFTER PLACING SHIP:')
        game_board.display_board(game_board.user_board) 
    print("All ships have been placed!")
    
    for _ in range(len(computer_available_sizes)):
        place_computer_ship(game_board, computer_available_sizes)
    print("All computer ships have been placed!")
    print('___COMPUTER BOARD (SHIPS ARE HIDDEN):')
    game_board.display_board(game_board.computer_board, is_computer=True)
    
    while True:
        user_guess(game_board)
        print('___COMPUTER BOARD AFTER USER GUESS:')
        game_board.display_board(game_board.computer_board, is_computer=True)
        
        if check_winner(game_board):
            print(check_winner(game_board))
            break
        
        computer_guess(game_board)
        print('___USER BOARD AFTER COMPUTER GUESS:')
        game_board.display_board(game_board.user_board)

        if check_winner(game_board):
            print(check_winner(game_board))
            break

start_game()