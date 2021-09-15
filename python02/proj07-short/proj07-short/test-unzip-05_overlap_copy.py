#! /usr/bin/python3

from unzip import *



def one_test(comp_data):
    print(f'INPUT STREAM: {comp_data}')
    raw_str = unzip(comp_data)
    print(f'OUTPUT DATA:  "{raw_str}"')
    print(f'Length comparisons: {len(comp_data)} -> {len(raw_str)}')
    print()



one_test( ["a", (1,20)] )
one_test( ["a ", (2,1), "b ", (5,4), "c ", (11,10), "d ", (23,22), "e"] )



print()
print("TESTCASE COMPLETED")


