"""
"""


import sympy
from sympy import *
from sympy import simplify_logic
from sympy import evaluate


def s(logic, display=False):
    if display:
        print(simplify_logic(logic))
    return simplify_logic(logic)


def combine_props(props):
    combined = " & ".join(true_props)
    return combined


def simplify_each(props):
    for prop in props:
        print(
            f"Original: {prop}",
            "\n"
            f"Simplified: {s(prop)}",
            "\n"
        )
    
    print(
        "\nCombined and Simplified:\n",
        f"{s(combine_props(props))}"
        )



true_props = [
    # If I takethe bus or subway, then I will be late for my appointment
    "(b | s) >> l",
    # If I take a cab, then I will not be late but I will be broke
    "c >> (~l & r)",
    # I will be on time
    "~l"
]


def eval_scenario(props, truth_values):
    expression = sympify(combine_props(props))
    applied_truth = expression.subs(truth_values)
    return sympify(applied_truth)



# y= eval_scenario(true_props, scenario)
# print(y)

expr = combine_props(true_props)


# ────────────────────────────────────────────────────────────────────────────────




x, y, z, b, s, l, c, r = symbols("x, y, z, b, s, l, c, r")

expr = x & y & z

print(sympify(expr))


expr = expr.xreplace({x : (b | s) >> l})
expr = expr.xreplace({y :  c >> (~l & r)})
expr = expr.xreplace({z : ~l})

expr = expr.subs({x: true, y: true, z: true})

print(simplify_logic(expr))



