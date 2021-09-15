"""Wordsearch Solver

Script to find instances of words from a word bank found in a 
word-search puzzle. Reads in puzzle and word bank from a text 
file whose name/location will be requested through stdin by a 
prompt after execution. Puzzle and word bank should be separated 
by a blank line.

Indicates results for each word in word bank by visually representing 
their locations in stdout.

Author: Christian P. Byrne
Course: CSC120 Summer 2021
"""


def direction_indexes(start_row, start_column, word_len):
    """Creates the sequential coordinate lists for the letter-positions 
    of words in all 8 directions from the starting coordinate.

    Args:
        start_row (int) : y-coordinate in the 2D puzzle array.
        start_column (int) : x-coordinate in the 2D puzzle array.
        word_len (int) : length of word being searched for.

    Returns:
        list : each direction is a sub-list of (x-coord, y-coord) tuples 
            in order.

    Examples:
        >>> print(direction_indexes(1, 0, 2))
        [[(1, 0), (2, 0)], [(1, 0), (2, -1)], [(1, 0), (2, 1)], 
        [(1, 0), (1, 1)], [(1, 0), (1, -1)], [(1, 0), (0, 0)], 
        [(1, 0), (0, 1)], [(1, 0), (0, -1)]]


    """

    # 0 = stay in place, 1 = up/right, -1 = down/left
    slopes = [
        (1, 0), (1, -1), (1, 1),
        (0, 1), (0, -1),
        (-1, 0), (-1, 1), (-1, -1) 
    ]
    
    directions = []
    for (row_slope, column_slope) in slopes:
        indexes = [
            (
                start_row + n*row_slope, start_column + n*column_slope
            ) for n in range(word_len)
        ]
        directions.append(indexes)

    return directions


def search_grid(grid, word):
    """Search puzzle grid in all 8 directions starting at each individual 
    letter in the grid, collecting coordinate-based locations of any 
    instances of found word.

    Args:
        grid (list) : string elements represent rows in the puzzle.
        word (str) : word to search for occurences of.

    Returns:
        list : each element is a sub-list of tuple coordinates representing 
            the position of the letters for that instance of the found word.


    """
    hits = []
    for start_x in range(len(grid[0])):
        for start_y in range(len(grid)):
            
            # Per instructions: The third nested loop checks each letter 
            #   location one by one for each of the 8 directions and 
            #   compares with wordbank word.
            for direction in direction_indexes(start_y, start_x, len(word)):
                # Skip directions that go outside of puzzle grid.
                not_looped = True
                for (x, y) in direction:
                    if x < 0 or y < 0:
                        not_looped = False
                if not_looped:
                    try:
                        # Build the word created by going in this direction.
                        string_at_location = (
                            "".join(
                                [grid[y][x] for (y, x) in direction]
                                )
                        )
                        # Append coordinates of matches to ret list.
                        if string_at_location == word:
                            hits.append(direction)
                    except IndexError:
                        continue

    return hits


def print_solved_grid(grid, word_hits, word):
    """Void function to print solved version of grid wherein everything 
    except the located instances of the wordbank word is a period.

    Args:
        grid (list) : string elements represent rows in the puzzle.
        word_hits (list) : 2D list. Each sub-list contains 
            (x-coord, y-coord) tuples in an order corresponding 
            to the letters in word.
        word (str) : word from word-bank.


    """
    
    # Create 2D grid of same dimensions as puzzle but all elements are periods
    solved_2D_grid = [
        ["."]*len(grid[0]) for _ in grid
    ]

    # Fill in located word's letters according to discovered coordinates
    for word_location in word_hits:
        for (row, column), letter in zip(word_location, list(word)):
            solved_2D_grid[row][column] = letter

    for row in solved_2D_grid:
        print(
            "".join(row)
        )


def read_puzzle():
    """Requests filename from stdin, parses and returns word bank 
    and puzzle based on blank-line seperator.

    Returns:
        list: [
            list : str elements represent rows in the puzzle,
            list : str elements represent word bank words
            ]

    """
    print("Please give the puzzle filename:")
    try:
        lines = open(input(), "r").readlines()
    except FileNotFoundError:
        print("Sorry, the file doesn't exist or cannot be opened.")
        quit()

    puzzle = []
    word_bank = []
    i = 0
    while lines[i] != "\n":
        puzzle.append(
            lines[i].strip("\n").strip()
        )
        i += 1
    while i < len(lines):
        if lines[i].strip() != "\n" and lines[i].strip():
            word_bank.append(
                lines[i].strip("\n").strip()
            )
        i += 1

    return [puzzle, word_bank]


def main():
    puzzle, word_bank = read_puzzle()
    for word in word_bank:
        word_locations = search_grid(puzzle, word)
        if word_locations:
            print_solved_grid(puzzle, word_locations, word)
        else:
            print(f"Word '{word}' not found")
        print() 


if __name__ == "__main__":
    main()