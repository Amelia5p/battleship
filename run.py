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
        self.guesses=[]
        self.ships=[]
        self.user_position=[]
        self.computer_position=[]

    def display_board(self,board):
        """ Display board format"""
        
        print('   A B C D E F G H ')
        print( '   ***************')

        for row_num in range(self.board_size):
            print(f"{row_num + 1}|", end=' ')

            for col_num in range(self.board_size):
                cell_value= board[row_num][col_num] 
                print(cell_value, end=' ')
            print()
        print()
  

