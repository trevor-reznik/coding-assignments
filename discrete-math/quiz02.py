"""

T(x, y, z)


"""



# def T(x, y, z):
#     x, y, z = float(x), float(y), float(z)
#     prop1 = (x + y)**2
#     prop2 = z

#     equal = prop1 == prop2

#     return equal



# for i in range(2000):
#     for z in range(299):
#         for r in range(299):
#             ret = T(i, z, r)



from sympy import *



p, q, x, y, z = symbols("p, q, x, y, z")


expr = x & y & z

expr = expr.xreplace({x: p >> q })
expr = expr.xreplace({y: q >> p })
expr = expr.xreplace({z: ~(p | q) })


expr = expr.subs({x: true, y: true, z: true})

print(simplify_logic(expr))