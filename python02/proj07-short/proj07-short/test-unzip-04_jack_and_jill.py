#! /usr/bin/python3

from unzip import *



def one_test(comp_data):
    print(f'INPUT STREAM: {comp_data}')
    raw_str = unzip(comp_data)
    print(f'OUTPUT DATA:  "{raw_str}"')
    print(f'Length comparisons: {len(comp_data)} -> {len(raw_str)}')
    print()



one_test( ["See Jack run. ", (11,9), "s up the hill", (24,8), "and Ji", (16,2), " ro", (5,3), "down."] )


print()
print("TESTCASE COMPLETED")


