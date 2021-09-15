#! /usr/bin/python3

from unzip import *



def one_test_expect_assert(comp_data):
    print("--- Testing an input stream, which we expect will result in an assertion failure. ---")
    print(f"INPUT STREAM: {comp_data}")

    try:
        raw_str = unzip(comp_data)

    except AssertionError:
        print("SUCCESS!")
        print()
        return

    except:
        print("ERROR: The function throw an exception, but it was not an assertion failure")
        print()
        return

    print("ERROR: The function did not throw any sort of exception!")
    print()
    return



one_test_expect_assert( ["abc"  , 123,456, "xyz"] )
one_test_expect_assert( ["abc"*4, (1,)] )                      # NOTE: (123,) declares a 1-element tuple
one_test_expect_assert( ["abc"  , (1,2,3), "baz"])
one_test_expect_assert( ["abc"  , ('x',2), "baz"])
one_test_expect_assert( ["abc"  , (1,'y'), "baz"])
one_test_expect_assert( [(1,1)] )
one_test_expect_assert( ["abc", (4,1)] )
one_test_expect_assert( ["abc", (0,1)] )
one_test_expect_assert( ["abc", (-1,1)] )
one_test_expect_assert( ["abc", (3,0)] )
one_test_expect_assert( ["abc", (3,-1)] )


print()
print("TESTCASE COMPLETED")


