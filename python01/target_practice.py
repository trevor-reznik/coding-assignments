target_string = input("Hit string:\n")
while len(target_string) < 3 or (len(target_string) % 4) > 0:
    print("Please provide a valid hit string.")
    target_string = input("Hit string:\n")
marker = input("Marker:\n")
while len(marker) > 1:
    print("Please provide a valid marker.")
    marker = input("Marker:\n")
number_of_shots = len(target_string)/4
shots_index = 1
_ = 1
current_hit_x = int(target_string[_-1] + target_string[_])
current_hit_y = int(target_string[_+1] + target_string[_+2])
index_row = 5
while index_row >= -5:
    index_column = -7
    if index_row == 0 and current_hit_y != 0:
            print("-------|-------", end="")
    else:
        if index_row != current_hit_y:
            print("       |       ", end="")
        else:
            while index_column <= 7:
                if index_column == 0 and current_hit_x != 0:
                    print("|", end="")
                else:
                    if current_hit_x == index_column: 
                        print(marker, end="")
                    else:
                        if index_row == 0:
                            print("-", end="")
                        else:
                            print(" ", end="")
                index_column += 1
            if shots_index < number_of_shots: 
                _ += 4
                current_hit_x = int(target_string[_-1] + target_string[_])
                current_hit_y = int(target_string[_+1] + target_string[_+2])
                shots_index += 1
    index_row -= 1
    print("")

