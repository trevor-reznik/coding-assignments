"""Rhyme Generator

Maps rhymes from dictionary text file, then prints perfect rhymes
entered by user at stdin.

How this program defines a rhyme:
    1. Rhymes revolve around the phenomes connected to a primary stress
        a. DIRECTLY BEFORE:     different phenomes.
        b. AT:                  identical.
        c. ALL AFTER:           identical.  
    2. There can be no rhymes if:
        a. NO primary stress.
        b. NO phenomes BEFORE primary stress.

Filename:
    rhymes.py

Author: 
    Christian P. Byrne

Course:
    CSC120 | Summer 2021
"""


class Pronunciation:
    """Pronounciation object for a word.

    Args:
        phenomes (list) : List of phenome units of the word.

    Attributes:
        primary (str) : Primary stress phenome.
        before (str) : Phenome before the primary.
        after (list) : List of phenomes proceeding the primary stress.
        rhyme_possible (bool) : Whether a perfect rhyme is possbile
            with this word.


    """
    def __init__(self, phenomes):
        primary_index = self._find_primary(phenomes)

        # Map attributes if a rhyme is possible.
        if primary_index:
            self.primary = self._strip(
                phenomes[primary_index]
            )
            self.before = self._strip(
                phenomes[primary_index-1]
            )
            self.after = self._strip(
                phenomes[primary_index + 1:]
            )        
    
    def _find_primary(self, phenomes):
        """Parse the primary stress phenome.

        Returns:
            int | null : Index of primary stress in phenomes list.


        """
        primary_indices = []
        for index, sound in enumerate(phenomes):
            if "1" in sound:
                primary_indices.append(index)

        # Check if no rhymes possible.
        if (
            not primary_indices 
            or len(primary_indices) == 1 
            and primary_indices[0] == 0
        ):
            self.rhyme_possible = False 
        else:
            self.rhyme_possible = True
            return min(primary_indices)

    def _exclude(self, phrase):
        """Replace the stress-number suffix from the
        phenomes."""
        for exclude in ["1", "2", "0"]:
            phrase = phrase.replace(exclude, "")
        return phrase

    def _strip(self, phenomes):
        """Format the phenomes by removing stress-number
        suffixes."""
        return (
            self._exclude(phenomes) if type(phenomes) == str
            else [self._exclude(phenome) for phenome in phenomes]
        )
    
    def rhyme(self, word):
        """Checks if passed word rhymes with self.

        Args:
            word (obj) : Another Pronunciation object to cross-
                reference with.

        Returns:
            bool : Whether the two words rhyme.
        """
        # Three conditions by which a rhyme is defined here.
        if (
            word.primary == self.primary
            and word.before != self.before
            and word.after == self.after
        ):
            return True
        return False


def map_pronunciations(file):
    """Parses the input pronunciations dictionary file and maps
    reference dictionary.

    Args:
        file (list) : List of lines in input txt file.
    
    Returns:
        (
            {
                [word: str]: Pronunciation[],
            },
            list: Words with no rhymes possible.
        )


    """
    no_rhymes = []
    pronunciations = {}

    for line in file:
        parsed = line.strip("\n").strip().split()
        word = parsed[0].upper()

        # Word's value is a list of Pronunciation objects.
        if word not in pronunciations.keys():
            pronunciations[word.upper()] = []

        mapped = Pronunciation(parsed[1:])
        if mapped.rhyme_possible:
            pronunciations[word].append(mapped)
        else:
            no_rhymes.append(word)

    return pronunciations, no_rhymes


def validate_input(stdin, no_rhymes, words):
    """Validates stdin input.
    
    If an error condition is met or the word does
    not exist in the mapped dictionaries, associated 
    error message is printed.
    
    Args:
        stdin (str): Result from input() call.
        no_rhymes (list) : List of words with no possible rhymes.
        words (list) : List of all words with possible rhymes.

    Returns:
        bool: False if error condition, else True.


    """
    user_word = stdin.strip("\n").strip()
    if not user_word:
        print("No word given\n")
        return False
 
    if len(user_word.split()) > 1:
        print(
            "Multiple words entered, please enter "
            + "only one word at a time.\n"
        )
        return False
    
    if (
        user_word.upper in no_rhymes 
        or user_word.upper() not in words
    ):
        print(
            f"Rhymes for: {user_word.upper()}\n"
            + " -- none found --\n"
        )
        return False

    return user_word.upper()


def print_results(matches):
    """Print the matches from dictionary lookups.
    
    Handles duplicates by not printing. Handles empty
    list by printing special error message.
    
    Args:
        matches (list) : List of matches.


    """
    if not matches:
        print(" -- none found --")
    else:
        # Prevent printing duplicates.
        log = []
        for word in matches:
            if word not in log:
                print(word)
                log.append(word)
    print()


def main():
    file = open(input(), "r").readlines()
    pronunciations, no_rhymes = map_pronunciations(file)

    while True:
        try:
            user_word = validate_input(
                input(),
                no_rhymes,
                pronunciations.keys()
            )
        except EOFError:
            return
        # Skip if error condition or word not found.
        if not user_word:
            continue
        
        print(
            f"Rhymes for: {user_word.upper()}"
        )
        matches = []
        # For each pronunciation of user's word.
        for user_pronunciation in pronunciations[user_word]:
            # For each word in dictionary.
            for word, variants in pronunciations.items():
                # For each different pronunciation of word in dict.
                for pronunciation in variants:
                    # Call pronunciation object's rhyme method.
                    if pronunciation.rhyme(user_pronunciation):
                        matches.append(
                            word.upper()
                            )
                            
        print_results(matches)


if __name__ == "__main__":
    main()