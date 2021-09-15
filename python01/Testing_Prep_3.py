width = int(input("Rectangle width:\n"))
height = int(input("Rectangle height:\n"))

print()
for _ in range(height):
    for _ in range(width):
        print("#", end="")
    print()

##
## Program Requirement: "After getting the two inputs,
## the program should print out a blank line"
##
## 
## for _ in range(height):  < 
##  print()                 < Failure on input range
##  for _ in range(width):  < (_, 0)
##      print("#", end="")  < 
##
