"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Find random words from dictionary."""

    def __init__(self,path="words.txt"):
        """Reads path and prints # of items read."""

        dict_file = open(path)

        self.words = self.word_list(dict_file)

        print(f"{len(self.words)} words read")

    def word_list(self,dict_file):
        """Creates a list of words from dict_file"""

        return [w.strip() for w in dict_file]

    def random(self):
        """Returns random word"""

        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Special WordFinder that excludes blank lines and comments"""

    def word_list(self,dict_file):
        """Creates a list of words from dict_file, skipping blanks and comments"""

        return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]


