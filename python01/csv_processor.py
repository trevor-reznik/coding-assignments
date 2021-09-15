###
### Course: CSc 110
### Author: Christian Byrne
### Description: Program that reads in a CSV file with no column labels, and can
###              compute a maximum, minimumim, and average of a specified column.
###              Asks user for file path/name, the column number to perform 
###              an operation on, and the desired operation. Prints resutls to
###              stdout.
###


def to_columns(line_list):
    """
    Program that separates list of lines with comma separator and turns to 2D array.
    Then rotates 2D list 90 degrees such that the rows become columns
    and the columns become rows. Returns the rotated comma-separated 2D array.
    line_list: list. file.readlines() result of a CSV file object
    """
    twod_list = []
    for line in line_list:
        comma_split = line.strip().split(",")
        twod_list.append(comma_split)
    ret_list = []
    for index, _ in enumerate(twod_list[0]):
        current_line = []  
        for row in twod_list:
            current_line.append(row[index])
        ret_list.append(current_line)
    return ret_list


def min_num(column, column_num):
    """
    Takes a list of numbers and calculates the min value.
    Returns a string that indicates which value is lowest in the list, as well as
    the column number of the numbers in the CSV file object. 
    column: a list of numbers in str,float, or int data type. 
    column_num: an integer representing the index value of column's elements in 
    the original readlines() result
    """
    first_value = float(column[0])
    for number in column:
        if float(number) < first_value:
            first_value = float(number)
    return "The minimum value in column " + str(column_num+1) + " is: " + str(first_value)


def max_num(column, column_num):
    """
    Takes a list of numbers and calculates the max value.
    Returns a string that indicates which value is largest in the list, as well as
    the column number of the numbers in the CSV file object. 
    column: a list of numbers in str,float, or int data type. 
    column_num: an integer representing the index value of column's elements in 
    the original readlines() result
    """
    first_value = float(column[0])
    for number in column:
        if float(number) > first_value:
            first_value = float(number)
    return "The maximum value in column " + str(column_num+1) + " is: " + str(first_value)


def avg_num(column, column_num):
    """
    Takes a list of numbers and calculates the avg value.
    Returns a string that indicates the average value, as well as
    the column number of the numbers in the CSV file object. 
    column: a list of numbers in str,float, or int data type. 
    column_num: an integer representing the index value of column's elements in 
    the original readlines() result
    """
    sum_n = 0
    for number in column:
        sum_n += float(number)
    return "The average for column " + str(column_num+1) + " is: " + str(sum_n/float(len(column)))


def main():
    csv_file = open(input("Enter CSV file name:\n"), "r")
    line_list = to_columns(csv_file.readlines())
    column_num = int(input("Enter column number:\n")) - 1
    column = line_list[column_num]
    print({"min": min_num(column,column_num), "max": max_num(column,column_num),\
        "avg": avg_num(column,column_num)}[input("Enter column operation:\n")])
    

main()