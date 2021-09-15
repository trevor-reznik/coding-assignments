#! /usr/bin/python3

from unzip import *



def one_test(comp_data):
    print(f'INPUT STREAM: {comp_data}')
    raw_str = unzip(comp_data)
    print(f'OUTPUT DATA:  "{raw_str}"')
    print(f'Length comparisons: {len(comp_data)} -> {len(raw_str)}')
    print()



one_test( ["\n", "a\n", "b",(1,1),(3,1),(5,7), "c",(1,2),(4,1),(16,28) ] )



print()
print("TESTCASE COMPLETED")


