###
### Course: CSc 110
### Author: Christian Byrne
### Description: Encryption programs that accepts a text file then writes
###              a new file with the lines of that file shuffled. Also writes another text
###              file containing the original line number of each corresponding line in the
###              encrypted output file. Text file with shuffled lines will be
###              named "encrypted.txt" and the file containing the original line
###              numbers of the encrypted lines will be named "index.txt" Output files stored
###              in directory of script.
###


import random
random.seed(125)

def shuffle_indices(lines):
    """
    Encryption function that accepts the list of lines from a file and shuffles
    the order of the lines. First creates an ordered list of the original line indexes.
    Then shuffles the lines by getting two random integers starting from zero and going
    up to the number of lines in the file minus 1 and swapping the content of the lines
    at these two indexes.
    Repeats shuffle swap (line count * 5) times.
    Returns array with two elements -- shuffled list of lines and corresponding list of
    indexes from original file.
    Before returning list of index values, increases each element by 1 to make it 1-based
    which more accurately describes line numbers rather than index numbers.
    lines: a list of lines from a file. a file object readlines method result
    """
    num_lines = len(lines)
    line_list = lines
    index_list = []
    i = 0
    for _ in lines:
        index_list.append(i)
        i += 1
    for _ in range(num_lines * 5):
        index_initial = random.randint(0, num_lines-1)
        index_replacement = random.randint(0, num_lines-1)
        
        temp = line_list[index_initial]
        line_list[index_initial] = line_list[index_replacement]
        line_list[index_replacement] = temp

        temp = index_list[index_initial]
        index_list[index_initial] = index_list[index_replacement]
        index_list[index_replacement] = temp
    for _ in range(0,num_lines):
        index_list[_] += 1
    return [line_list, index_list]        


def write_output(file_name, line_list):
    """
    Function that opens a file with specified file name in write mode then writes
    each element of second parameter list to a line in this file before closing the file.
    Called twice in main in order to create encrypted lines output file and index key file.
    file_name: the name of the file to be opened in write mode. if file does not exist in
    cd, it will be created
    line_list: a list of lines whose elements' data types will be converted to string before
    being writ to the output file
    """
    output_file = open(file_name, "w")
    for line in line_list:
        output_file.write(str(line).strip("\n") + "\n")
    output_file.close()

    
def main():
    file = open(input("Enter a name of a text file to encrypt:\n"), "r")
    keys = shuffle_indices(file.readlines())
    write_output("encrypted.txt", keys[0])
    write_output("index.txt", keys[1])


main()
