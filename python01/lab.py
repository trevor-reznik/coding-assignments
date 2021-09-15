###
### Author: Christian Byrne
### Course: CSc 110
### Description: Program accepts a string of digits. Validates that the
###              input is digits. Then prints a bar of hashtags for each
###              digit in the string. The number of hashtags is determined 
###              by the associated digit. Bars printed sinde a neat box.
###

digit_string_input = input("Enter bar string:\n")

if digit_string_input.isnumeric() == False:
    exit()

index = 0
print("+---------+")
while index < len(digit_string_input):
    digit_value = int(digit_string_input[index])
    print("|" + "#"*digit_value, end="")
    print(" "*(9-digit_value) + "|")
    index += 1
print("+---------+")