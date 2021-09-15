usr_stdin = input("Please give a string to swap:").strip()
input_len = len(usr_stdin)
print(
    usr_stdin[input_len // 2 + input_len % 2 : ] 
    + ( usr_stdin[input_len // 2] if input_len % 2 else "" )
    + usr_stdin[ : input_len // 2]
)