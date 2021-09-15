###
### Author: Christian Byrne
### Course: CSc 110
### Description: Program accepts a string of digits. Validates that the
###              input is digits. Then prints bars of hastags inside a 20-
###              character-wide box. For every digit pair, the first digit
###              of the pair determines the number of right-alligned-with-
###              center hastags in the row and the second digit determines
###              the number of left-alligned hashtags in the second half of
###              the row.
###


digit_string_input = input("Enter bar string:\n")

# validate inputs
if digit_string_input.isnumeric() == False:
    exit()

# Append a "0" to string so programs works when input has odd # of characters
if int(len(digit_string_input)) % 2 != 0:
    digit_string_input += "0"

# 9 - number of digits = amount of whitespace in each half-row
i = 0
print("+------------------+")
while i < len(digit_string_input):
    first_digit_value = int(digit_string_input[i])
    second_digit_value = int(digit_string_input[i+1])
    print("|" + " "*(9-first_digit_value), end="")  
    print("#"*(first_digit_value+second_digit_value), end="")
    print(" "*(9-second_digit_value) + "|")  
    i +=2
print("+------------------+")