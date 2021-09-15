###
### Author: Christian Byrne
### Course: CSc 110
### Description: Reversi (also known as Othello) is a two-player board
###              game played on a 2-dimensional grid. This program allows 2 users 
###              to play a game of Reversi on a board with 1 row and 12 columns.
###              First player is black and uses the X character. Second player is
###              White and uses the O character. Players alternate placing their
###              character on their chosen position which they choose through stdin.
###              If a player sandwhiches another player's characters with their own,
###              the sandwhiched characters are captured and flipped to the capturor's
###              character. At end of each turn, the current board state is printed
###              to stdout and written to a graphics canvas in a Tkinter window.
###              Game continues until the board is full at which point the winner
###              is inidicated on the printed boards and main passes.
###


from graphics import graphics

WHITE = 'O'
BLACK = 'X'
EMPTY = ' '

def is_move_acceptable(board, turn, pos):
    """
    Validates that the player's input is a legal play given the current board state.
    If player's position input is outside the range of the board or the position is
    already occupied, returns False; otherwise, returns True.
    board: list with 12 elements representing the characters on each position of the current board
    turn: string indicating whose turn it is. should be BLACK or WHITE variable value
    pos: integer representing 1-based position of the current player's move
    """
    if int(pos) < 0 or int(pos) > 12:
        return False
    if board[pos-1] != " ":
        return False
    return True


def move(board,turn,pos):
    """
    Accepts current board state and current move then returns an updated board list.
    Splits the board list at the index of pos into first_half and second_half sub-lists.
    Then iterates through both sub-lists away from the pos in the original board list.
    Continues iteration while elements in sub-list equal the other player's character.
    If the element at the end of that iteration = current player's character, then
    the elements in between start of sub-list and the end of the iteration are 'flipped'
    such that they are assigned as turn variable (representing current player's character).
    board: list with 12 elements representing the characters on each position of the current board
    turn: string indicating whose turn it is. should be BLACK or WHITE variable value
    pos: integer representing 1-based position of the current player's move
    """
    flipped_index = 0
    first_half = board[:pos-1]
    first_half.reverse()
    if pos != 1:
        while first_half[flipped_index] != " " and first_half[flipped_index] != turn\
              and flipped_index < len(first_half)-1:
            flipped_index += 1
        if first_half[flipped_index] == turn:
            for _ in range(flipped_index):
                first_half[_] = turn
        flipped_index = 0
    second_half = board[pos:]
    if pos != 12:
        while second_half[flipped_index] != " " and second_half[flipped_index] != turn\
              and flipped_index < len(second_half)-1:
            flipped_index += 1
        if second_half[flipped_index] == turn:
            for _ in range(flipped_index):
                second_half[_] = turn
    first_half.reverse()
    first_half.append(turn)
    return first_half + second_half
    

def get_move(turn):
    """
    Accepts current player's character then calls input() to get current player's move.
    Converts current player's move to an integer then returns it.
    turn: string indicating whose turn it is. should be BLACK or WHITE variable value
    """
    position_choice = input(turn + " choose your move:\n")
    return int(position_choice)


def is_over(board):
    """
    Called at end of each turn to check if game is over. Accepts current board state list then
    iterates through list. If any position is vacant, returns False, indicating game is not over.
    If iteration completes, indicating no elements = EMPTY variable value, returns True.
    board: list with 12 elements representing the characters on each position of the current board
    """
    for position in board:
        if position == EMPTY:
            return False
    return True


def get_opposite_turn(turn):
    """
    Called at end of each turn to update 'turn'property of main() object.
    Accepts current player's character and returns the the opposite
    player's character.
    turn: string indicating whose turn it is. should be BLACK or WHITE variable value
    """
    if turn == BLACK:
        return WHITE
    return BLACK


def print_board(board):
    """
    Void function that accepts current board state as list then prints visual
    representation of that board to stdout. Iterates through board list and 
    prints each element in between | characters.
    Adds decorative bars on top and bottom of 1 by 12 board.
    board: list with 12 elements representing the characters on each position of the current board
    """
    print("+-----------------------+")
    for position_character in board:
        print("|" + position_character, end="")
    print("|\n+-----------------------+")
    

def draw_board(board, gui):
    """
    Void function that writes the current board state to a canvas object from the graphics
    module to be displayed in a Tkinter window. Writes a decorative title and a 1by12 board.
    Iterates through board list and 1by12 board on canvas and writes the list's string elements
    to each corresponding box in the canvas's board.
    Then calls is_over() to check if game is over and if result is True, writes
    the who_is_winner() result to the canvas object at the bottom of the canvas
    board: list with 12 elements representing the characters on each position of the current board
    gui = initialized graphics canvas object on which to write the board graphics. Canvas should
    be at least 700x200 pixels
    """
    gui.rectangle(0,0,700,200,gui.get_color_string(18,18,18))
    gui.text(235,20,"REVERSI",gui.get_color_string(179,179,179),40)
    x_position = 50
    for _ in range(11):
        gui.rectangle(x_position,110,50,50,gui.get_color_string(64,64,64))
        gui.rectangle(x_position+3,113,47,44,gui.get_color_string(40,40,40))
        x_position += 50
    gui.rectangle(x_position,110,50,50,gui.get_color_string(64,64,64))
    gui.rectangle(x_position+3,113,44,44,gui.get_color_string(40,40,40))
    x_position = 63
    for position_character in board:
        character_color = "white"
        size_adjust = 2
        if position_character == BLACK:
            character_color = "aquamarine"
            size_adjust = 0
        gui.text(x_position-size_adjust,113,position_character,character_color,30)
        x_position += 50
    if is_over(board) == True:
        gui.text(265,160,who_is_winner(board),"IndianRed1",25)
    gui.update_frame(60)


def who_is_winner(board):
    """
    Accepts current board state as board list and returns the player with more points.
    Assumes that every position is occupied.
    First checks if there are 6 elements of BLACK--necessitating 6 of WHITE--and returns
    draw result if True.
    If not a draw, compares the count of each player's characters in the board list then
    returns a string indicating that the higher score player won the game.
    board: list with 12 elements representing the characters on each position of the current board
    """
    if board.count(BLACK) == 6:
        return "THERE WAS A TIE"
    if board.count(BLACK) > board.count(WHITE):
        return "BLACK WINS"
    return "WHITE WINS"


def main():
    print('WELCOME TO REVERSI')

    gui = graphics(700, 200, 'reversi')

    # Initialize an empty list with 12 slots
    board = [EMPTY] * 12
    # State of whether or not the game is over
    over = False
    # Starting turn (should alternate as gome goes on)
    turn = BLACK

    # Print out the initial board
    print_board(board)
    draw_board(board, gui)

    # Repeatedly process turns until the game should end (every slot filled)
    while not over:
        place_to_move = get_move(turn)
        while not is_move_acceptable(board, turn, place_to_move):
            place_to_move = get_move(turn)
        board = move(board, turn, place_to_move)

        print_board(board)
        draw_board(board, gui)

        over = is_over(board)
        turn = get_opposite_turn(turn)
    print('GAME OVER')
    print(who_is_winner(board))


main()