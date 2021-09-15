def water_state(temp):
    if float(temp) > 32:
        if float(temp) < 212:
            return "Water"
        return "Steam"
    return "Ice"

print(water_state(input("Temperature in fahrenheit:\n")))
