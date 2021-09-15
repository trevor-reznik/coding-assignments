#! /usr/bin/env python3


import simple_classes



(a,b,c) = ("___", "asdflakjsdf", "33u0asdv")

print("Inputs:")
print("  a = "+str(a))
print("  b = "+str(b))
print("  c = "+str(c))
print()

print("First Object:")
obj = simple_classes.Simplest(a,b,c)

print("  obj.a = "+str(obj.a))
print("  obj.b = "+str(obj.b))
print("  obj.c = "+str(obj.c))
print()

print("After making some changes...")
obj.a = 123
obj.b = ["foo","bar","baz"]
obj.c = (obj.b, obj.b)
print("  obj.a = "+str(obj.a))
print("  obj.b = "+str(obj.b))
print("  obj.c = "+str(obj.c))
print()

print("Creating a new object, using multiples of the inputs:")
obj = simple_classes.Simplest(a*2, b*3, c*4)
print("  obj.a = "+str(obj.a))
print("  obj.b = "+str(obj.b))
print("  obj.c = "+str(obj.c))


