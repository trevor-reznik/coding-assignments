usr_stdin = [input().split() for _ in range(2)]
combination = usr_stdin[0] + usr_stdin[1] 

print(
    "The first line was:",
    usr_stdin[0],
    "\nThe second line was:",
    usr_stdin[1],
    "\n\nThe combination of both lines had {} words.".format(
        sum([len(_) for _ in usr_stdin])
    ),
    "\nThe combined set of words was:",
    combination    
)

combination.sort()
print(
    "\nAfter sorting, the words were:",
    combination,
    "\n\nPairs:"
)

for index, (list1_elem, list2_elem) in enumerate(zip(*usr_stdin)):
    print(
        "{}: {},{}".format(
            index,
            list1_elem,
            list2_elem
        )
    )

