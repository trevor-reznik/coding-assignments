usr_stdin = input("input string: ")
print(
    len(usr_stdin),
    usr_stdin[1],
    usr_stdin[:10],
    usr_stdin[-5:],
    usr_stdin.upper(),
    sep="\n"
)

print(
    "QWERTY" if usr_stdin[0].lower() in "qwerty"
    else "UIOP" if usr_stdin[0] in "uiop"
    else "LETTER" if usr_stdin[0].isalpha()
    else "DIGIT" if usr_stdin[0].isnumeric()
    else "OTHER"
)

print(int(input()) * int(input()))