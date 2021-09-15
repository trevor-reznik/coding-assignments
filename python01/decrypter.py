###
### Course: CSc 110
### Author: Christian Byrne
### Description: Decryption programs that accepts a text file that has had its line shuffled
###              on the basis of line number as well as an encryption key that indicates the
###              original line number of each corresponding line in the encrypted file.
###              Reorders the line numbers in the provided file based on the key then writes
###              the reordered lines to a new file named "decrypted.txt" which will be stored
###              in the directory of the script and will represented the decrypted original file.
###


def reorder(line_list, index_list):
    """
    Function that reorders the lines with reference to the key file.
    First declares a list with the same number of elements as lines in the encrypted file--each
    element will be a placeholder.
    Then iterates through the key list and line list simultaneously and assigns the
    placeholder list element with the index of the current iteration of the key list with
    the corresponding string value from the line_list.
    Returns the list of lines after it has been reordered.
    line_list: a list of lines from a file. a file object readlines method result
    index_list: list strings or integers indicating the original line number of each corresponding value
    in the line_list array
    """
    reordered_lines = [""] * len(index_list)
    for index, line in zip(index_list, line_list):
        reordered_lines[int(index)-1] = line
    return reordered_lines


def write_decrypted(lines):
    """
    Void function that writes each element in the paramter to a line in an output
    file named decrypted.txt.
    lines: a list of lines whose elements' data types will be converted to string before
    being writ to the output file
    """
    output_file = open("decrypted.txt", "w")
    for line in lines:
        output_file.write(str(line))
    output_file.close()

    
def main():
    encrypted_file = open(input("Enter the name of an encrypted text file:\n"), "r")
    index_file = open(input("Enter the name of the encryption index file:\n"), "r")
    decrypted_lines = reorder(encrypted_file.readlines(), index_file.readlines())
    write_decrypted(decrypted_lines)


main()
