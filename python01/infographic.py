###
### Author: Christian Byrne
### Course: CSc 110
### Description: This program reads in a text file (perhaps containing the contents of a 
###              book, poem, article, etc) and produces an infographic based on the text. 
###              Asks for path to text file in stdin. Displays infographic in tkinter window.
###              Infographic visualizes results of analysis. Those results includes the features:
###              name of file, total number of unique words, The most used small, medium, and 
###              large words in the file. s/m/l defined by character counts <5/5-7/>7.
###              And lastly, the proportions of capitalized vs. non-capitalized words and
###              proportions of punctuated vs. non-punctuated words. 
###

# %%
from graphics import graphics

def make_dict(lines):
    """
    Accepts list of lines from text file and maps each word to a dictionary which
    follows the key:value pattern of word:word_occurence_number. Returns that dictionary.
    lines: a readlines() result called on a text file. List of strings corresponding to
    lines in the target text file
    """    
    word_counts = {}
    for line in lines:
        for word in line.strip().split():
            word_counts[word] = 1 if word not in word_counts else word_counts[word] + 1
    return word_counts


def punctuation_ratios(word_counts):
    """
    Counts the fraction of unique words that are capitalized and fraction that are puncuated. 
    Calls isupper() str method on first character for capitalize check. If last chracter is 
    in list of puncuation marks for latter. Returns list of 2 floats following structure of 
    [capitalized/total, puncuated/total].
    word_counts: dict of unique words. key:value pattern of {word(str):word_occurence_number(int)}
    """
    ratios = [0,0]
    for word in word_counts.keys():
        if word[:1].isupper():
            ratios[0] += 1
        if word[-1:] in [".",",","!","?"]:
            ratios[1] += 1
    return [ratios[0]/(len(word_counts)),ratios[1]/(len(word_counts))]


def analyze_by_size(word_counts):
    """
    Itearates through dict of unique words and counts occurences of each size s/m/l
    (<5/5-7/>7 characters). Makes three dictionares which follow same format as word_counts,
    but each dictionary corresponds to a size s/m/l. After those dicts are defined, a fourth
    dict is made by finding the keys in each of the first three with the highest value 
    (representing words with highest occurence for each size). Then creates list with number
    of unique words in each size category. Returns list containing the dictionary of 
    most common words per size and the list containing # of words in each category.  
    word_counts: dict of unique words. key:value pattern of {word(str):word_occurence_number(int)}
    """
    text_features = [{},{},{},{},[]]
    for word in word_counts.keys():
        i = 0 if len(word) < 5 else 2 if len(word) > 7 else 1
        text_features[i][word] = word_counts[word]
    for size_dic in text_features[:3]:
        keys, values = list(size_dic.keys()), list(size_dic.values())
        text_features[3][keys[values.index(max(values))]] = max(values)
        text_features[4].append(len(values))
    return text_features[3:]


def display_lengths(gui, colors, length_counts):
    """
    Writes bar chart representing the proportion of each different word length
    in the text.
    gui: graphics object from graphics module
    colors: a list of gui's get_color_string() method results
    length_counts: list with two elements. first is dict with size:# of words,
    second is list containing the # of words of each size as fraction of all 
    unique words
    """
    gui.text(38,170, "Word lengths", colors[4], 20)
    gui.rectangle(40, 210, 180, length_counts[1][0], colors[0])
    gui.text(50,215, "small words", "black", 10)
    gui.rectangle(40, 210+length_counts[1][0], 180, length_counts[1][1], colors[1])
    gui.text(50,215+length_counts[1][0], "medium words", "black", 10)
    gui.rectangle(40, 210+450-length_counts[1][2], 180, length_counts[1][2], colors[2])
    gui.text(50,215+450-length_counts[1][2], "large words", "black", 10)


def display_punct(gui, colors, percentages):
    """
    Writes bar charts representing the proportion of capitalized words and proportion
    of puncuated words relative to the total # of unique words.
    gui: graphics object from graphics module
    colors: a list of gui's get_color_string() method results
    percentages: list with two float elements [capitalized/total, puncuated/total]
    """
    # Cap/Non-Cap
    gui.text(238,170, "Cap/Non-Cap", colors[4], 20)
    gui.rectangle(240, 210, 180, percentages[0]*450, colors[0])
    gui.text(250,215, "Capitalized", "black", 10)
    gui.rectangle(240, 210+percentages[0]*450, 180, (1-percentages[0])*450, colors[1])
    gui.text(250,215+percentages[0]*450, "Non Capitalized", "black", 10)
    # Punct/Non-Punct
    gui.text(438,170, "Punct/Non-Punct", colors[4], 20)
    gui.rectangle(440, 210, 180, percentages[1]*450, colors[0])
    gui.text(450,215, "Puncuated", "black", 10)
    gui.rectangle(440, 210+percentages[1]*450, 180, (1-percentages[1])*450, colors[2])
    gui.text(450,215+percentages[1]*450, "Non Puncuated", "black", 10)


def main():
    file_name = input("Enter rel path and name of file:\n")
    word_counts = make_dict((open(file_name,"r")).readlines())
    total_unique, length_counts = len(word_counts), analyze_by_size(word_counts)
    most_used_str = "Most used words (s/m/l):   "
    for i in range(3):
        most_used_str += list(length_counts[0].keys())[i] + " "
        most_used_str += "(" + str(length_counts[0][list(length_counts[0].keys())[i]]) + "x) "
        length_counts[1][i] = length_counts[1][i]/total_unique*450
    gui = graphics(650, 700, 'Infographic')
    colors = [gui.get_color_string(255, 138, 128),gui.get_color_string(200, 90, 84),\
        gui.get_color_string(255, 188, 175),gui.get_color_string(179,179,179),\
            gui.get_color_string(225,226,225)]
    while True:
        gui.rectangle(0, 0, 650, 700, gui.get_color_string(18, 18, 18))
        gui.text(40,30, file_name, colors[0],22)
        gui.text(40,85, "Total Unique Words: " + str(total_unique), colors[3],20)
        gui.text(42,135, most_used_str, colors[0], 13)
        display_lengths(gui, colors, length_counts)
        display_punct(gui, colors, punctuation_ratios(word_counts))
        gui.update_frame(120)


if __name__ == "__main__":
    main()