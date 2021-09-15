#! /usr/bin/env python3


import simple_classes



(a,b,c) = ("xyz", "hello", "world")

print("Inputs:")
print("  a = "+str(a))
print("  b = "+str(b))
print("  c = "+str(c))
print()

print("First Object:")
obj1 = simple_classes.Rotate(a,b,c)

print("  obj1.get_first()  = "+str(obj1.get_first()))
print("  obj1.get_second() = "+str(obj1.get_second()))
print("  obj1.get_third()  = "+str(obj1.get_third()))
print()

print("Second Object: (doubled strings)")
obj2 = simple_classes.Rotate(a*2, b*2, c*2)

print("  obj2.get_first()  = "+str(obj2.get_first()))
print("  obj2.get_second() = "+str(obj2.get_second()))
print("  obj2.get_third()  = "+str(obj2.get_third()))
print()

print("Rotating the first object a few times...")

obj1.rotate()

print("  obj1.get_first()  = "+str(obj1.get_first()))
print("  obj1.get_second() = "+str(obj1.get_second()))
print("  obj1.get_third()  = "+str(obj1.get_third()))
print()

obj1.rotate()

print("  obj1.get_first()  = "+str(obj1.get_first()))
print("  obj1.get_second() = "+str(obj1.get_second()))
print("  obj1.get_third()  = "+str(obj1.get_third()))
print()

obj1.rotate()

print("  obj1.get_first()  = "+str(obj1.get_first()))
print("  obj1.get_second() = "+str(obj1.get_second()))
print("  obj1.get_third()  = "+str(obj1.get_third()))
print()

obj1.rotate()

print("  obj1.get_first()  = "+str(obj1.get_first()))
print("  obj1.get_second() = "+str(obj1.get_second()))
print("  obj1.get_third()  = "+str(obj1.get_third()))
print()

print("Checking to see that the second object is unchanged...")

print("  obj2.get_first()  = "+str(obj2.get_first()))
print("  obj2.get_second() = "+str(obj2.get_second()))
print("  obj2.get_third()  = "+str(obj2.get_third()))
print()

print("Rotating the second object a couple times...")

obj2.rotate()

print("  obj2.get_first()  = "+str(obj2.get_first()))
print("  obj2.get_second() = "+str(obj2.get_second()))
print("  obj2.get_third()  = "+str(obj2.get_third()))
print()

obj2.rotate()

print("  obj2.get_first()  = "+str(obj2.get_first()))
print("  obj2.get_second() = "+str(obj2.get_second()))
print("  obj2.get_third()  = "+str(obj2.get_third()))
print()



print("TESTCASE COMPLETED")

