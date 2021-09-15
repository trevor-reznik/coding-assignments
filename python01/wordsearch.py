###
### Course: CSc 110
### Author: Christian Byrne
### Description: Wordsearch program that searches for substrings in 2D array of strings.
###              Searches for substrings that are in the array. Substrings can be 
###              vertically or horizontally oriented and can be backwards or forwards, up  
###              or down as with a crossword puzzle. However, can only search either vertically or  
###              horizontally per instance. Program asks for path to two files. The first
###              file is the list of key words and the second file is the crossword puzzle 
###              itself. Then asks if user wants to search for vertical or horiozontal instances
###              of the key words in the puzzle. After runniing, program prints locations of
###              all substrings to stdout.
###


def rotate_grid(puzzle_grid):
    """
    Program that rotates the board 90 degrees such that the rows become columns
    and the columns become rows. Called if user indicates that they want to search
    vertically. Accepts the grid array and returns the rotated version.
    The puzzle grid is re-defined with the result of this function in main, so
    the rest of the program can run normally and search the rotated board horizontally.
    puzzle_grid: 2D array in which each element[][] should be a single character representing a
    letter in the crossword puzzle
    """
    rotated_lines = []
    index = 0
    for column in puzzle_grid[0]:
        current_line = []  
        for row in puzzle_grid:
            current_line.append(row[index])  # make new row list with each element of same index
        rotated_lines.append(current_line)
        index += 1
    return rotated_lines


def search_grid(puzzle_grid, search_words, puzzle_mode):
    """
    Iterates through each row in the puzzle-grid array and calls check_line()
    on each element. If check_line() returns a hit, the result is appended to
    local word_locations array after appending the index of the current row. Returns
    the word_locations array representing lists of each disocvered word and their
    respective locations.
    puzzle_grid: 2D array in which each element[][] should be a single character representing a
    letter in the crossword puzzle
    search_words: a dictionary -- keys are string to be searched for in the puzzle and values are
    the reversed versions of paired keys
    puzzle_mode: "v" or "h" strings indicating vertical or horizontal search mode respectively
    """
    word_locations = []
    for row in puzzle_grid:
        found_word = check_line(row, search_words)
        if found_word != False:
            found_word.append(puzzle_grid.index(row)+1)  # add row index to result before appending
            word_locations.append(found_word)
            
    for hit in word_locations:
        if puzzle_mode == "v":
            print(hit[0] + " found at " + "[" + str(hit[1]) + ", " + str(hit[2]) + "]")
        else:
            print(hit[0] + " found at " + "[" + str(hit[2]) + ", " + str(hit[1]) + "]")


def check_line(line, search_words):
    """
    Called for every line in the puzzle grid. Iterates through line and checks if
    any of the keys or values in the search_words dictionary is in the 1st arg. Returns
    string of any found word and the column index. If substring is a key in the dict, column
    index is the start of the world. If substring is value in dict,, returns the end
    of the substring as column start. If no search_words are found in the line, returns False.
    line: a list of single-character strings representing a row in the crossword puzzle
    search_words: a dictionary -- keys are string to be searched for in the puzzle and values are
    the reversed version of paired keys
    """
    line_string = ""
    for character in line:
        line_string += str(character).lower()
    for word in search_words.keys():
        if word in line_string or search_words[word] in line_string:
            index = 0
            while word in line_string[index:] or search_words[word] in line_string[index:]:
                index += 1
            if search_words[word] in line_string:
                return [word, index+len(search_words[word])-1]
            return [word, index]
    return False


def map_search_words(words_file):
    """
    The txt file with the search_words is passed to this function to map the text in
    the file to a dictionary. Splits each line then appends a key:value pair with each
    element of the split() result. Returns the dictionary after iterating through whole txt file.
    words_file: a file object with lines formatted like 'word: reversed_word'
    """
    search_words = {} 
    for line in words_file:
        split_line = line.split(": ")
        search_words[split_line[0].strip()] = split_line[1].strip("\n")
    return search_words


def make_grid(puzzle_file):
    """
    The txt file with the crossword puzzle is passed to this function to map the text in
    the file to a 2D array. Splits each line with ' ' separator. Creates list of the split() result
    for each line of the file. Appends each of those lists to the 2D array which is returned after
    the whole txt file has been iterated through.
    puzzle_file: a file object with lines of space-separated characters representing rows in the puzzle
    """
    grid = []
    for line in puzzle_file:
        grid.append(line.strip("\n").split(" "))
    return grid


def main():
    words_file = open(input("Enter word file:\n"), "r")
    puzzle_file = open(input("Enter puzzle file:\n"), "r")
    puzzle_mode = input("Enter puzzle mode:\n")

    search_words = map_search_words(words_file)
    puzzle_grid = make_grid(puzzle_file)
    if puzzle_mode == "v":
        puzzle_grid = rotate_grid(puzzle_grid)
    search_grid(puzzle_grid, search_words, puzzle_mode)


main()
