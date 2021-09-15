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



init_singer = "Miss Piggy"

print(f"Creating a new Band object.  Initial Singer: {init_singer}")
flaming_rabbits = simple_classes.Band(init_singer)
dump(flaming_rabbits, "Initial Band:")



new_drummer = "Animal"
print(f"--- Adding a drummer: {new_drummer}")
flaming_rabbits.set_drummer(new_drummer)
dump(flaming_rabbits, "After adding the drummer:")



guitar1 = "Kermit"
guitar2 = "Swedish Chef"
guitar3 = "Rowlf"

print(f"--- Adding a guitar player: {guitar1}")
flaming_rabbits.add_guitar_player(guitar1)
dump(flaming_rabbits, "After adding the guitar player")

print(f"--- Adding a guitar player: {guitar2}")
flaming_rabbits.add_guitar_player(guitar2)
dump(flaming_rabbits, "After adding the guitar player")

print(f"--- Firing all guitar players ---")
flaming_rabbits.fire_all_guitar_players()
dump(flaming_rabbits, "After firing all guitar players")

print(f"--- Adding a guitar player: {guitar3}")
flaming_rabbits.add_guitar_player(guitar3)
dump(flaming_rabbits, "After adding the guitar player")



print("TESTCASE COMPLETED")

