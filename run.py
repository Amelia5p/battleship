import random
from random import randint, choice
import os


def landing_page():
    """Landing page contents."""
    # Copied straight from https://fsymbols.com/text-art/
    print(
        """
██████╗░░█████╗░████████╗████████╗██╗░░░░░███████╗░██████╗██╗░░██╗██╗██████╗░
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝██╔════╝██║░░██║██║██╔══██╗
██████╦╝███████║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░╚█████╗░███████║██║██████╔╝
██╔══██╗██╔══██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░░╚═══██╗██╔══██║██║██╔═══╝░
██████╦╝██║░░██║░░░██║░░░░░░██║░░░███████╗███████╗██████╔╝██║░░██║██║██║░░░░░
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░
"""
    )


def display_instructions():
    """
    Function to display simplified instructions for the Battleship game.
    """
    # Multi-line string containing the instructions for the game
    instructions = """Battleship Game Instructions 

1. Objective:
   - Sink all of your opponent's ships before they sink yours.

2. Game Setup:
   - Place 5 ships on your 8x8 grid.
   - Choose ship sizes (1 to 5) and their orientation (H or V).

3. Placing Your Ships:
   - Enter starting coordinates (e.g., A1) for your ship placement.
   - Ensure ships do not overlap or go out of bounds.

4. Taking Turns:
   - Guess the location of your opponent's ships by entering coordinates.
   - Hits are marked as 'X', misses as 'O'.

5. Winning the Game:
   - The game ends when one player sinks all of the opponent's ships.

Good luck and enjoy Battleship!"""
    print(instructions)


def get_user_name():
    """ Get's username and validates it """
    while True:
        user_name = input("Please enter your name: \n").strip()
        if user_name and user_name.replace(" ", "").isalpha():
            print(f"Hello {user_name}, enjoy the game!!\n")
            return user_name
        else:
            print(
                "Invalid name. Please enter a valid name "
                "(only letters and spaces allowed).")


class Board:
    """A class to represent the game board for Battleship.

    Initializes default board sizes of 8 with 5 ships and has lists to store
    guesses and ships. Boards are initialized with '~', and lists store user
    and computer ship positions.
    """

    def __init__(self):
        self.board_size = 8
        self.user_board = [["~" for _ in range(8)] for _ in range(8)]
        self.computer_board = [["~" for _ in range(8)] for _ in range(8)]
        self.num_ships = 5
        self.user_positions = []
        self.user_guesses = []
        self.computer_positions = []
        self.computer_guesses = []
        self.user_selected_sizes = []
        self.computer_selected_sizes = []

    def display_board(self, board, is_computer=False):
        """Display board format.

        Iterate over each row and column in the board and print (1-8).
        Hides ships if it is the computer's board.
        """
        print("   A B C D E F G H")
        print("   ***************")

        # Loop through each row of the board
        for row_num in range(self.board_size):
            print(f"{row_num + 1}|", end=" ")

            for col_num in range(self.board_size):
                # Get the value of the current cell (either '~', 'S', 'X','O')
                cell_value = board[row_num][col_num]
                # If it's the computer's board and the cell contains a ship
                # hide it with '~'
                if is_computer and cell_value == "S":
                    print("~", end=" ")
                # Otherwise, display the actual value of the cell
                else:
                    print(cell_value, end=" ")
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
            ship_size = int(
                input("What size do you want your ship? (1 to 5):\n ")
            )
            if ship_size in available_sizes:
                print(f"Great choice, your ship size is {ship_size}!")
                # Add chosen ship size to user's selected sizes
                # Remove it from available sizes
                game_board.user_selected_sizes.append(ship_size)
                available_sizes.remove(ship_size)

                # Set orientation automatically if ship size is 1
                if ship_size == 1:
                    orientation = "H"
                    print(
                        "Your ship size is 1, orientation is not necessary"
                    )
                else:
                    while True:
                        orientation = input(
                            "Do you want to place your ship horizontally"
                            "or vertically? (H/V):\n "
                        ).upper()
                        # Validate orientation input
                        if orientation in ["H", "V"]:
                            print(f"Your ship will be placed {orientation}.")
                            break
                        else:
                            print(
                                "Invalid input. Please enter 'H' for"
                                "horizontalor 'V' for vertical."
                            )

                while True:
                    coordinates = input(
                        "Enter desired coordinates (e.g., A1, B5):\n "
                    ).upper()
                    # Validate that coordinates follow correct format
                    # and fall within board limits
                    if (
                        len(coordinates) == 2
                        and coordinates[0] in "ABCDEFGH"
                        and coordinates[1] in "12345678"
                    ):
                        col = ord(coordinates[0]) - ord("A")
                        row = int(coordinates[1]) - 1

                        # Check if the chosen location can accommodate the ship
                        if can_place_ship(
                            game_board.user_board,
                            ship_size,
                            orientation,
                            row,
                            col,
                        ):
                            place_ship(
                                game_board.user_board,
                                ship_size,
                                orientation,
                                row,
                                col,
                            )
                            print(
                                f"Your ship has been placed at {coordinates}."
                            )
                            game_board.user_positions.append(
                                (ship_size, orientation, row, col)
                            )
                            # Return the details of the placed ship
                            return ship_size, orientation, coordinates
                        else:
                            print(
                                "Cannot place ship here. It goes out of bounds"
                                "or overlaps another ship."
                            )
                    else:
                        print(
                            "Invalid input. Please enter coordinates in the"
                            "format 'Letter (A-H) followed by Number (1-8)'."
                        )
            else:
                print(
                    "You have already chosen this size or this ship size is not available." 
                    "Please enter an available ship size."
                )
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def place_ship(board, ship_size, orientation, start_row, start_col):
    """Place a ship on the board based on what the user chooses."""
    if orientation == "H":
        for i in range(ship_size):
            # Place ship horizontally
            board[start_row][start_col + i] = "S"
    elif orientation == "V":
        for i in range(ship_size):
            # Place ship vertically
            board[start_row + i][start_col] = "S"
    return (ship_size, orientation, start_row, start_col)


def can_place_ship(board, ship_size, orientation, start_row, start_col):
    """Checks if ship can be placed without overlapping"""
    if orientation == "H":
        # Check if the ship exceeds board width
        if start_col + ship_size > len(board[0]):
            return False
        # Check for overlap with existing ships
        for i in range(ship_size):
            if board[start_row][start_col + i] != "~":
                return False
    elif orientation == "V":
        # Check if the ship exceeds board height
        if start_row + ship_size > len(board):
            return False
        for i in range(ship_size):
            if board[start_row + i][start_col] != "~":
                return False
    return True


def place_computer_ship(game_board, computer_available_sizes):
    """
    Randomly selects ship size, orientation, and coordinates for the computer.
    Ensures that ships are placed within bounds and do not overlap. Random
    library used.
    """
    while True:
        # Randomly pick a ship size from available sizes
        ship_size = random.choice(computer_available_sizes)
        game_board.computer_selected_sizes.append(ship_size)
        computer_available_sizes.remove(ship_size)

        # Randomly decide orientation
        orientation = "H" if ship_size == 1 else random.choice(["H", "V"])
        # Generate random starting coordinates
        while True:
            row = random.randint(0, game_board.board_size - 1)
            col = random.randint(0, game_board.board_size - 1)

            # Check if ship can be placed at the selected coordinates
            if can_place_ship(
                game_board.computer_board, ship_size, orientation, row, col
            ):
                place_ship(
                    game_board.computer_board, ship_size, orientation, row, col
                )
                game_board.computer_positions.append(
                    (ship_size, orientation, row, col)
                )
                return ship_size, orientation, (row, col)


def user_guess(game_board):
    """Allows user to guess a position on the computer's board"""
    # Infinite loop to keep asking for user input until a valid guess is made
    while True:
        guess = input("Enter your guess (e.g., A1, B5):\n ").upper()
        # Validate the guess format (should be a letter and a number)
        if (
            len(guess) == 2
            and guess[0] in "ABCDEFGH"
            and guess[1] in "12345678"
        ):
            # Convert the letter (column) to an index (0-7)
            col = ord(guess[0]) - ord("A")
            # Convert the number (row) to a zero-based index (0-7)
            row = int(guess[1]) - 1

            if (row, col) in game_board.user_guesses:
                print("You already guessed this location. Try again.")
            else:
                game_board.user_guesses.append((row, col))

                if game_board.computer_board[row][col] == "S":
                    print("It's a hit!")
                    game_board.computer_board[row][col] = "X"
                else:
                    print("You missed!")
                    game_board.computer_board[row][col] = "O"
                break
        else:
            print(
                "Invalid input. Please enter coordinates in the format"
                "'Letter (A-H) followed by Number (1-8)'."
            )


def computer_guess(game_board):
    """Allows computer to guess a random position on the computer's board"""
    while True:
        # Randomly choose a row index
        row = randint(0, game_board.board_size - 1)
        # Randomly choose a column index
        col = randint(0, game_board.board_size - 1)

        if (row, col) not in game_board.computer_guesses:
            game_board.computer_guesses.append((row, col))

            if game_board.user_board[row][col] == "S":
                print("The computer has hit your ship")
                game_board.user_board[row][col] = "X"

            else:
                print("The computer has missed")
                game_board.user_board[row][col] = "O"
            break


def check_winner(game_board):
    """Checks if either player has lost all of their ships"""
    # Count the number of user's ships remaining on their board
    user_ships_remaining = sum(row.count("S") for row in game_board.user_board)
    # Count the number of computer's ships remaining on their board
    computer_ships_remaining = sum(
        row.count("S") for row in game_board.computer_board
    )

    if user_ships_remaining == 0:
        return "The computer has sunk all of your ships."
    elif computer_ships_remaining == 0:
        return "Congratulations! You have sunk all of the computer's ships."
    return None


def clear_console():
    """Clears console"""
    os.system("cls" if os.name == "nt" else "clear")


def play_again():
    """Ask user if they want to play again"""
    while True:
        user_input = (
            input("Would you like to play again? (y/n):\n").strip().lower()
        )

        if user_input == "y":
            clear_console()
            start_game()
            break
        elif user_input == "n":
            clear_console()
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def take_turns(game_board):
    """Main game loop for taking turns until there's a winner."""

    while True:
        # User's turn
        print("Your turn:")
        user_guess(game_board)
        print("___COMPUTER BOARD AFTER USER TURN:")
        game_board.display_board(game_board.computer_board, is_computer=True)
        # Check for winner after user's turn
        winner = check_winner(game_board)
        if winner:
            print(winner)
            break
        input("Press Enter to see the next board...")
        # Computer's turn
        print("\nComputer's turn:")
        computer_guess(game_board)
        print("___USER BOARD AFTER COMPUTER TURN:")
        game_board.display_board(game_board.user_board)
        # Check for winner after computer's turn
        winner = check_winner(game_board)
        if winner:
            print(winner)
            break


def start_game():
    """ Main game function """
    landing_page()
    print("\n\n")
    # Ask user if they would like to view instructions
    while True:
        view_instructions = input("Would you like to see the instructions?"
                                  "(y/n):\n ").strip().lower()
        if view_instructions in ['y', 'n']:
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    if view_instructions == 'y':
        display_instructions()
        input("Press Enter once you are ready...")

    get_user_name()
    game_board = Board()

    available_sizes = [1, 2, 3, 4, 5]
    computer_available_sizes = [1, 2, 3, 4, 5]

    print('___USER BOARD:')
    game_board.display_board(game_board.user_board)

    # Loop to allow user to place their ships
    for _ in range(len(available_sizes)):
        place_user_ship(game_board, available_sizes)
        print('___USER BOARD AFTER PLACING SHIP(S):')
        game_board.display_board(game_board.user_board)
    print("All ships have been placed!")

    # Loop to allow computer to place its ships
    for _ in range(len(computer_available_sizes)):
        place_computer_ship(game_board, computer_available_sizes)
    print("All computer ships have been placed!")

    # Main game loop to take turns
    take_turns(game_board)
    # Ask's user if they would like to play again
    play_again()


start_game()
