###
### Course: CSc 110
### Author: Christian Byrne
### Description: Accepts size parameters as inputs.
###              Prints ATAT from Stars Wars as ASCII Art
###              with sizes of sections adjusted to
###              associated input values.
###

neck_length = int(input("Neck Length:\n"))
body_height = int(input("Body Height:\n"))
leg_height = int(input("Leg Height:\n"))

# Top/Shell
print("\n     _,.-Y  |  |  Y-._")
print(' .-~"   ||  |  |  |   "-.')
print(body_height*" |______________________|\n", end="")   

# Middle - Starting at Top of Head
print(" |______________________|", end="")
print(neck_length*" ", end="")
print("    _____")

print(" L______________________[---", end="")
print(neck_length*"-", end="")
print('I" .-{"-.')

print("I____________________ [__L]", end="")
print(neck_length*"_", end="")
print("[I_/r(=}=-P")

print("L________________________j~", end="")
print(neck_length*" ", end="")
print(' \'-=c_]/=-^')

# Bottom/Legs
print("\\________________________]")
print("  [___________________]")
print('     I--I"~~"""~~"I--I')
print(leg_height*("     |\\n|         |\\n|\n"), end="")
print("     ([])         ([])")
print("    /|..|\\       /|..|\\")
print("   |=}--{=|     |=}--{=|")
print("  .-^--e-^-.   .-^--e-^-.")