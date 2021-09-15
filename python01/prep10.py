formula = (input("Enter string:\n"))
open_count = closed_count = 0
result = "balanced"
for _ in range(len(str(formula))):
    if formula[_] == "(":
        open_count += 1
    if formula[_] == ")":
        closed_count += 1
        if closed_count > open_count:
            result = "unbalanced"      
if closed_count != open_count:
    result = "unbalanced" 
print("Parentheses", result)
