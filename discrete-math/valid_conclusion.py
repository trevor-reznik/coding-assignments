from sympy import *

prop1, prop2, prop3, \
     bus, subway, late, cab, broke = \
         symbols("prop1, prop2, prop3, bus, subway, late, cab, broke")

# "Assume that the following three propositions are true"
hypothesis = prop1 & prop2 & prop3

# 1. "If I take the bus or subway, then I will be late for my appointment."
hypothesis = hypothesis.xreplace({prop1 : (bus | subway) >> late})
hypothesis = hypothesis.subs({prop1: true})

# 2. "If I take a cab, then I will not be late but I will be broke."
hypothesis = hypothesis.xreplace({prop2 :  cab >> (~late & broke)})
hypothesis = hypothesis.subs({prop2: true})

# 3. "I will be on time."
hypothesis = hypothesis.xreplace({prop3 : ~late})
hypothesis = hypothesis.subs({prop3: true})

simplied = simplify_logic(hypothesis)
# > simplified = ~bus & ~late & ~subway & (broke | ~cab)


# ────────────────────────────────────────────────────────────────────────────────


# Textbook 1.11: "The argument is valid whenever the proposition
#   ( p1 ∧ p2 ∧ ... ∧ pn ) → conclusion is a tautology"
def is_conclusion_valid(conclusion):
    argument = hypothesis >> conclusion
    return simplify_logic(argument) == true


# "use symbolic logic to determine whether each of the following is a 
# ...valid conclusion or not"



# ────────────────────────────────────────────────────────────────────────────────

"""
FOOTNOTES

( hypothesis >> conclusion ) must be equivalent to True for the conclusion 
to be valid.

The results make sense given that the simplified conjunction of the hypothesis
is equivalent to:

~bus & ~late & ~subway & (broke | ~cab)

It's interesting because to find all the permutations where the hypotheses are
true we just find the permutations where the conjoined hypothesis is equivalent 
to true. 

~bus & ~late & ~subway & (broke | ~cab) = True when:
    - bus, late, and subway are False and 
    - cab is False or broke is True.

This is reflected in the truth table from ther problem.

It's also easy to test conclusions after simplifying the hypothesis, because we
just ask if "hypothesis >> conclusion"" is a tautology. For example, in part (d),

"~bus & ~late & ~subway & (broke | ~cab) >> ~subway" of course is a tautology.
"""

# ────────────────────────────────────────────────────────────────────────────────


"""
It seems that another way to look at it is:
    if the conclusion is a necessary condition for the conjoined hypothesis
    to be true, then the argument is valid. To filter the hypothesis such 
    that you only see necessary conditions, try to convert all logical operators
    to &.
    
    ~subway is a necessary condition of the hypothesis, so ~subway is a valid 
    conclusion.

Or:
    If the conclusion is true, can the conjoined hypothesis still be true.
    Find the necessary conditions for the conclusion to be true, then apply
    them to the conjoined hypothesis to see if it is still true


Converting all logical operators to &:

~bus & ~late & ~subway & ~(~broke & cab)


By this logic, ~bus, ~late, ~subway should all also be valid conclusions. The 
proposition ~(~broke & cab) to be true requires that "~broke & cab" is false,
which means that broke is True or cab is False. This provides at least 4 valid
conclusions: ~bus, ~late, ~subway, (broke | ~cab). 
"""

# Testing:

print(
    f"~bus: {is_conclusion_valid(~bus)}",
    f"~late: {is_conclusion_valid(~late)}",
    f"~subway: {is_conclusion_valid(~subway)}",
    f"(broke | ~cab): {is_conclusion_valid(broke | ~cab)}",
    sep="\n"
)

