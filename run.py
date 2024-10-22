def get_user_name():
    """
    Ask for the users name and return it
    """
print("Welcome to Battleship! \n")    
user_name= input("Please enter your name: \n")
print(f"Hello {user_name}, enjoy the game!!\n")
    

scores= {"user":0 , "computer":0}

class Board:
    
    """ A class to represent the game board for Battleship-
    The size of the board- initializes the boards with a fixed size of 8x8.
    """

    def __init__(self):
        self.board_size= board_size
        self.user_board= [['~' for _ in range(8)] for _ in range(8)]
        self.compuer_board= [['~' for _ in range(8)] for _ in range(8)]
        
        
