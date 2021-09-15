#! /usr/bin/python3

from unzip import *



def one_test(comp_data):
    print(f'INPUT STREAM: {comp_data}')
    raw_str = unzip(comp_data)
    print(f'OUTPUT DATA:  "{raw_str}"')
    print(f'Length comparisons: {len(comp_data)} -> {len(raw_str)}')
    print()



one_test( [] )                             # empty string
one_test( ["abcd"] )                       # simple, 4-character string
one_test( ['a','b','c','d'] )              # same, but as individual characters
one_test( ['a','a','a','a','b','b','b'] )  # repeated characters, without duplication

# many individual characters, forming long strings
one_test( list("Hello world") )
one_test( list("she sells sea shells by the sea shore") )


print()
print("TESTCASE COMPLETED")


