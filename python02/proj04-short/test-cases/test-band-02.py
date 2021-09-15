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



init_singer = "Kurt Cobain"

print(f"Creating a new Band object.  Initial Singer: {init_singer}")
flaming_rabbits = simple_classes.Band(init_singer)
dump(flaming_rabbits, "Initial Band:")



new_drummer = "Russ"
print(f"--- Adding a drummer: {new_drummer}")
flaming_rabbits.set_drummer(new_drummer)
dump(flaming_rabbits, "After adding the drummer:")



singer2 = "Frank Sinatra"
print(f"--- Changing the singer: {singer2}")
flaming_rabbits.set_singer(singer2)
dump(flaming_rabbits, "After changing the singer:")



guitar1 = "Kermit"
print(f"--- Adding a guitar player: {guitar1}")
flaming_rabbits.add_guitar_player(guitar1)
dump(flaming_rabbits, "After adding the guitar player")



singer3 = "Garth Brooks"
print(f"--- Changing the singer: {singer3}")
flaming_rabbits.set_singer(singer3)
dump(flaming_rabbits, "After changing the singer:")



print("TESTCASE COMPLETED")

