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
        Initialises default board sizes of 8 and 5 ships, has lists to store guesses and ships.
        Boards are initialized with '~'.

    """

    def __init__(self):
        self.board_size= 8
        self.user_board= [['~' for _ in range(8)] for _ in range(8)]
        self.computer_board= [['~' for _ in range(8)] for _ in range(8)]
        self.num_ships= 5
        self.guesses=[]
        self.ships=[]
        
