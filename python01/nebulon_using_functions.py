### 
### Author: Christian Byrne
### Description: Describe your program with one
###              or more sentences of text.
###

layers_l = int(input("Large layers on bottom:\n"))
layer_m = int(input("Medium Layers on bottom:\n"))
layers_s = int(input("Small Layers on bottom:\n"))
len_f = int(input("Front length:\n"))
len_m = int(input("Middle length:\n"))
len_b = int(input("Back length:\n"))

def extender(scale, material):
    extension = ""
    for _ in range(scale):
        extension += material
    return extension

def repeater(scale, layer1, layer2):
    stack = ""
    for _ in range(scale):
        stack += layer1 + "\n" + layer2 + "\n"
    return stack

print("  /=" +  extender(len_f, "-") + "\\" + extender((len_m + 9), " ") + "/" + extender(len_b, "-") + "|")
print(" /==" + extender(len_f, "/") + "==\\\\\\" + extender((len_m + 4), " ") + "|=" + extender(len_b, "=") + "|")
print("|==-" + extender(len_f, "\\") + "======\--" + extender((len_m + len_b + 2), "=") + "|")
print(" \==" + extender(len_f, "=") + "==-------" + extender((len_m + len_b + 2), "-") + "|")
print("  \=" + extender(len_f, "-") + "=///     " + extender(len_m, " ") + "\\=" + extender(len_b, "=") + "|")
print(repeater(layers_l, ("   /" + extender((len_f - 3), "-") + "|"), ("   \\" + extender((len_f - 3), "=") + "|")), end="")
print(repeater(layer_m, (extender(((len_f - 3) - (len_f // 2)), " ") + "   /" + extender((len_f // 2), "+") + "|"), (extender(((len_f - 3) - (len_f // 2)), " ") + "   \\" + extender((len_f // 2), "-") + "|")), end="")
print(repeater(layers_s, (extender(((len_f - 3) - (len_f // 3)), " ") + "  \\" + extender((len_f // 3), "<") + "|"), (extender(((len_f - 3) - (len_f // 3)), " ") + "   " + extender((len_f // 3), "<") + "|")), end="")