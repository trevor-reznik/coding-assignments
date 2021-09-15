def count_characters(target_phrase, character_1, character_2):
    appearance_n = str(target_phrase.count(character_1) + target_phrase.count(character_2))
    print("'" + character_1 + "' and '" + character_2 + "' appeared " + appearance_n +\
            " times in the string '" + target_phrase + "'")
