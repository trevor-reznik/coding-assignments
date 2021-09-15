###
### Course: CSc 110
### Author: Christian Byrne
### Description: Accepts width parameter as input.
###              Prints TIE Fighter from Stars Wars as ASCII Art
###              with width of wings adjusted to width input.
###

width = int(input("Enter TIE width:\n"))

# Top - Wings
print("\n|[" + 9*" " + width*2*" " + "]|")
print("|[" + 9*" " + width*2*" " + "]|")
print("|[" + 9*" " + width*2*" " + "]|")

# Middle - Body
print("|[" + 1*" " + width*" " + "/=---=\\" + width*" " + 1*" " +  "]|")
print("|[" + width*" " + "/==---==\\" + width*" " +  "]|")
print("|[" + width*"/" + "|== X ==|" + width*"\\" + "]|")
print("|[" + width*" " + "\\==---==/" + width*" " +  "]|")
print("|[" + 1*" " + width*" " + "\\=---=/" + width*" " + 1*" " +  "]|")

# Bottom - Wings
print("|[" + 9*" " + width*2*" " + "]|")
print("|[" + 9*" " + width*2*" " + "]|")
print("|[" + 9*" " + width*2*" " + "]|")