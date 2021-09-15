###
### Course: CSc 110
### Author: Christian Byrne
### Description: Program that reads in a game log file.
###              Game log should be formated with each line being a space-separated
###              record with columns of team, player, points.
###              Program prints winner, final scores, first and last player to score
###              to stdout after accepting file_path to game log text file.
###


def get_log_file():
    """
    Calls input() to get file path to game log file from stdin.
    Then calls open() in read mode with the file path string as argument 1.
    Returns the file object initialized by open().
    """
    file_path = input("enter gamelog file name:\n")
    game_log = open(file_path, "r")
    return game_log


def split_to_array(game_log):
    """
    Accepts the game_log file object and splits the data into data cells.
    Assumes that each cell is separated by a space and that no single data point
    contains spaces. Uses split() on each line of the file obj then appends each
    element of the array returned by split() to the records array--which is returned
    after iterating through the whole file.
    game_log: the file object of the game_log file
    """
    records = []
    for line in game_log:
        separated_record = line.split(" ")
        for cell in separated_record:
            records.append(cell)
    return records


def team_names(cell_list):
    """
    Takes the array containing each data cell and returns the team names in an array.
    team1 will always be the first element in the cell_list. Then iterates until the
    next element in the team-column does not equal team1.
    cell_list: array containing each space-separated string data point in the log file
    """
    team1 = cell_list[0]
    i = 0
    while cell_list[i] == team1:
        i += 3
    team2 = cell_list[i]
    return [team1, team2]


def sum_scores(cell_list, teams):
    """
    Void function that prints the analysis of the log file.
    First iterates through cell_list array and adds up scores of each team then prints
    the higher of the two scores indicating the winner.
    Next, determines which team scored first then prints that team's final score followed
    by the other team's final score.
    cell_list: array containing each space-separated string data point in the log file
    teams: array containing team1 name and team2 name in that order as strings
    """
    team1, team2 = teams[0], teams[1]
    index = team2_score = team1_score = 0 
    for cell in cell_list:
        if cell == team1:
            team1_score += int(cell_list[index+2])
        if cell == team2:
            team2_score += int(cell_list[index+2])
        index += 1
    
    if team1_score > team2_score:
        print(team1 + " won!") 
    else:
        print(team2 + " won!")

    if cell_list[0] == team1:
        print(team1 + " scored " + str(team1_score) + " points.\n"\
              + team2 + " scored " + str(team2_score) + " points.")
    else:
        print(team2 + " scored " + str(team2_score) + " points.\n"\
              + team1 + " scored " + str(team1_score) + " points.")


def first_last_scores(cell_list):
    """
    Prints the first player to score and the last player to score.
    Uses first record for first player then finds the last record by referencing
    the length of the cell_list array acquired from len(cell_list) call. 
    cell_list: array containing each space-separated string data point in the log file
    """
    print(cell_list[1] + " scored first.")
    print(cell_list[len(cell_list) - 2] + " scored last.")
    

def main():
    game_log = get_log_file()
    cell_list = split_to_array(game_log)
    teams = team_names(cell_list)
    sum_scores(cell_list, teams)
    first_last_scores(cell_list)


main()
