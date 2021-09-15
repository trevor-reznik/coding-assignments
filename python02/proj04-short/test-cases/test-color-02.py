#! /usr/bin/env python3


import sys

import simple_classes



def dump(color, msg):
    print(msg)
    print("  __str__()        returns: "+str(color))
    print("  html_hex_color() returns: "+color.html_hex_color())
    print("  get_rgb()        returns: {}".format(color.get_rgb()))
    print()



r,g,b = (127,127,127)

print("Creating a new Color object.  r,g,b: {},{},{}".format(r,g,b))
some_color = simple_classes.Color(r,g,b)
dump(some_color, "Initial Color:")



color2 = "BLACK"
print(f"--- Setting the color: '{color2}'")
some_color.set_standard_color(color2)
dump(some_color, "Color, after setting the color")



color3 = "white"
print(f"--- Setting the color: '{color3}'")
some_color.set_standard_color(color3)
dump(some_color, "Color, after setting the color")



print("--- Clearing the red component ---")
some_color.remove_red()
dump(some_color, "Color, after removing the red")



color4 = "black"
print(f"--- Setting the color: '{color4}'")
some_color.set_standard_color(color4)
dump(some_color, "Color, after setting the color")



color5 = "WHITE"
print(f"--- Setting the color: '{color5}'")
some_color.set_standard_color(color5)
dump(some_color, "Color, after setting the color")



print("--- Clearing the red component ---")
some_color.remove_red()
dump(some_color, "Color, after removing the red")



color6 = "yellow"
print(f"--- Setting the color: '{color6}'")
some_color.set_standard_color(color6)
dump(some_color, "Color, after setting the color")



print("TESTCASE COMPLETED")

