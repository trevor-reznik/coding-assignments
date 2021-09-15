#! /usr/bin/python3

from unzip import *



def one_test(comp_data):
    print(f'INPUT STREAM: {comp_data}')
    raw_str = unzip(comp_data)
    print(f'OUTPUT DATA:  "{raw_str}"')
    print(f'Length comparisons: {len(comp_data)} -> {len(raw_str)}')
    print()



one_test( list('abc') + [(2,3)] )
one_test( list('jkl') + [(3,10)] )



print()
print("TESTCASE COMPLETED")


