def count_vowels(string, A, B):
    ct = 0
    sub = string[A:B+1]
    vowels = ['a','e','i','o','u']
    for _ in vowels:
        ct += sub.count(_)
    return ct
