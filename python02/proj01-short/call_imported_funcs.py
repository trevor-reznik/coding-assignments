import short1_thing


usr_stdin = input()

foo_ret = short1_thing.foo(usr_stdin)
print(foo_ret)

bar_ret = short1_thing.bar(
    *[usr_stdin] + [input() for _ in range(2)]
)
print(bar_ret)

print(
    short1_thing.baz(
        foo_ret, bar_ret
    )
)
