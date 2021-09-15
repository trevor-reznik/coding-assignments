while True:
    usr_stdin = input()
    if usr_stdin.strip() == "quit":
        break
    i = 0
    if usr_stdin:
        while usr_stdin[i] == " ":
            i += 1
    print(i)