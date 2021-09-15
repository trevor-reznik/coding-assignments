###
### Course: CSc 110
### Author: Christian Byrne
### Description: Accepts size parameters as inputs.
###              Prints Nebulon from Stars Wars as ASCII Art
###              with sizes of sections adjusted to
###              associated input values.
###     
                                                    
large_layers_number = int(input("Large Layers on bottom:\n"))
medium_layers_numbers = int(input("Medium Layers on bottom:\n"))
small_layers_number = int(input("Small Layers on bottom:\n"))
front_length = int(input("Front length:\n"))
middle_length = int(input("Middle length:\n"))
back_length = int(input("Back length:\n"))

# Top Section:
print("\n  /=" +  front_length*"-" + "\\" + (middle_length + 9)*" "\
     + "/" + back_length*"-" + "|")
print(" /==" + front_length*"/" + "==\\\\\\" + (middle_length + 4)*" "\
     + "|=" + back_length*"=" + "|")
print("|==-" + front_length*"\\" + "======\\--"\
     + (middle_length + back_length + 2)*"=" + "|")
print(" \\==" + front_length*"=" + "==-------"\
     + (middle_length + back_length + 2)*"-" + "|")
print("  \\=" + front_length*"-" + "=///     "\
     + middle_length*" " + "\\=" + back_length*"=" + "/")

# Bottom Section:

# Layer-count-inputs multiplied by the 2-line-strings that represents the layers 
print(large_layers_number*\
    ("   /" + (front_length - 3)*"-" + "|\n" + "   \\" + (front_length - 3)*"=" + "|\n"), end="")

# To make second and third layer right-justified with the first layer, 
# the difference between their lengths ((front_length - 3) - (front_length // [2 or 3])) is added as blank spaces
print(medium_layers_numbers*\
    (((front_length - 3) - (front_length // 2))*" " + "   /"\
        + (front_length // 2)*"+" + "|\n"\
             + ((front_length - 3) - (front_length // 2))*" " + "   \\"\
                  + (front_length // 2)*"-" + "|\n"), end="")
print(small_layers_number*\
    (((front_length - 3) - (front_length // 3))*" " + "  \\"\
         + (front_length // 3)*"<" + "|\n"\
              + ((front_length - 3) - (front_length // 3))*" " + "   "\
                   + (front_length // 3)*"<" + "|\n"), end="")
