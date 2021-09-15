#! /usr/bin/env python3


import sys

import simple_classes



def dump(band, msg):
    print(msg)
    print("  Singer:  "+band.get_singer())
    print("  Drummer: {}".format(band.get_drummer()))
    print("  Guitars: {}".format(band.get_guitar_players()))
    print("--- play_music() BEGIN ---")
    band.play_music()
    print("--- play_music() END ---")
    print()



print("TESTING TO SEE IF YOU PROPERLY DUPLICATE THE GUITAR LIST")
print()



init_singer = "Frank Sinatra's Favorite Cousin"

print(f"Creating a new Band object.  Initial Singer: {init_singer}")
flaming_rabbits = simple_classes.Band(init_singer)
dump(flaming_rabbits, "Initial Band:")



flaming_rabbits.add_guitar_player("Slash")
flaming_rabbits.add_guitar_player("Backslash")
flaming_rabbits.add_guitar_player("En")
dump(flaming_rabbits, "Band with 3 players")



players = flaming_rabbits.get_guitar_players()
print(f"The set of guitar players returned from the object: {players}")
print()

print("--- CHANGING THE PLAYER LIST WE WERE GIVEN ---")
players[1] = "asdf"
players.append("jkl")
print(f"  Updated player list: {players}")

players2 = flaming_rabbits.get_guitar_players()
print(f"  Band guitar list after changes were made to the array: {players2}")



print("TESTCASE COMPLETED")

