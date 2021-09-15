def affordability(price):
    if float(price) > 20:
        return "expensive."
    return "affordable."

print("That", input("Enter food:\n")\
      , "is", affordability(input("Enter price:\n")))
