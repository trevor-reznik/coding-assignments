def average_numbers(n_numbers):
    number_list = []
    for _ in range(n_numbers):
        user_number = int(input("Number:\n"))
        number_list.append(user_number)
    print("Average = " + str(sum(number_list)/n_numbers))