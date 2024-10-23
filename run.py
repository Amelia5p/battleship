from random import randint

def get_user_name():
    """
    A function to ask for the users name
    """
    print("Welcome to Battleship! \n")    
    user_name= input("Please enter your name: \n")
    print(f"Hello {user_name}, enjoy the game!!\n")

    
# Initialise scores
scores= {"user":0 , "computer":0}

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

    def display_board(self,board):
        """ Display board format, 
            Iterate over each row and column in the board print (1-8)
            Get value of cell"""
        
        print('   A B C D E F G H ')
        print( '   ***************')

        for row_num in range(self.board_size):
            print(f"{row_num + 1}|", end=' ')

            for col_num in range(self.board_size):
                cell_value= board[row_num][col_num] 
                print(cell_value, end=' ')
            print()
        print()


def place_user_ship(game_board):
    """
    Ask user what size ship, what orientation, and what coordinates they want.
    Input validation implemented.
    """
    while True:
        try:
            ship_size = int(input("What size do you want your ship? (1 to 5): "))
            if 1 <= ship_size <= 5:
                print(f"Great choice, your ship size is {ship_size}!")

                if ship_size == 1:
                    orientation = 'H'
                    print("Since your ship size is 1, orientation is not necessary")
                else:
                    while True:
                        orientation = input("Do you want to place your ship horizontally or vertically? (H/V): ").upper()
                        if orientation in ['H', 'V']:
                            print(f"Your ship will be placed {orientation}.")
                            break
                        else:
                            print("Invalid input. Please enter 'H' for horizontal or 'V' for vertical.")

                while True:
                    coordinates = input("Enter desired coordinates (e.g., A1, B5): ").upper()
                    if len(coordinates) == 2 and coordinates[0] in 'ABCDEFGH' and coordinates[1] in '12345678':
                        col = ord(coordinates[0]) - ord('A')
                        row = int(coordinates[1]) - 1 

                        if can_place_ship(game_board.user_board, ship_size, orientation, row, col):
                            place_ship(game_board.user_board, ship_size, orientation, row, col)
                            print(f"Your ship has been placed at {coordinates}.")
                            game_board.user_positions.append((ship_size, orientation, row, col))
                            return ship_size, orientation, coordinates
                        else:
                            print("Cannot place ship here. It goes out of bounds or overlaps another ship.")
                    else:
                        print("Invalid input. Please enter coordinates in the format 'Letter (A-H) followed by Number (1-8)'.")
            else:
                print("Please enter a number between 1 and 5.")
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


def place_computer_ship(game_board):
    """ Randomly place computer ships on board """
    for _ in range(game_board.num_ships):
        ship_size = randint(1, 5)
        orientation = choice(['H', 'V'])

        placed = False
        while not placed:
            row = randint(0, game_board.board_size - 1)
            col = randint(0, game_board.board_size - 1)

            if can_place_ship(game_board.computer_board, ship_size, orientation, row, col):
                place_ship(game_board.computer_board, ship_size, orientation, row, col)
                game_board.computer_positions.append((ship_size, orientation, row, col))
                placed = True






def start_game():  
    get_user_name()
    game_board = Board()
    print('___USER BOARD:')
    game_board.display_board(game_board.user_board)
    print('___COMPUTER BOARD:')
    game_board.display_board(game_board.computer_board)
    
    # loop allowing user to place ships only 5 times (num_ships)
    for _ in range(game_board.num_ships):
        place_user_ship(game_board)
        print('___USER BOARD AFTER PLACING SHIP:')
        game_board.display_board(game_board.user_board) 
    print("All ships have been placed!")
    place_computer_ship(game_board)
    print('___COMPUTER BOARD AFTER PLACING SHIPS:')
    game_board.display_board(game_board.computer_board)

start_game()