def calorie_counter(size, type):
    base = 0
    if len(type) == 4:
        base += 100
    if len(type) == 7:
        base += 300
    if size == "small":
        return base // 2
    return base

print("\n" + str(calorie_counter\
                 (input("Drink Size:\n"), input("Drink type:\n")))\
      , "calories")
