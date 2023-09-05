#!/usr/bin/env python

"""Count word occurence

USAGE: count_word_occurence.py [--options] input_file

Reports the occurence of each word, as lower-case, in an input file.
"""

import sys

__version__ = "0.1"
__author__  = "hien.le@vlimagrain.com"

class WordCounter:
    def __init__(self, description=None):
        self.description = "This is the word occurence counter"
        self.counter = {}

    def add(self, word=""):
        lc = word.lower()
        if lc in self.counter:
            self.counter[lc] += 1
        else:
            self.counter[lc] = 0

    def sort(self):
        pass

    def lookup(self, word):
        try:
            return self.counter[word.lower()]
        except KeyError:
            return 0

    def report(self):
        pass

#=== The real stuff ============================================================

def main():
    counter = WordCounter()
    with open (args.infile, "rb")as infile:
        for line in infile:
            words = line.split()
            for word in words:
                counter.add(word)
    competitors = ["bayer", "nunhems", "syngenta", "basf", "dow", "monsanto", "dupont", "pioneer", "seminis", "sakata", "kws", "rijk", "zwaan", "enza", "bejo", "takii", "limagrain"]
    for competitor in competitors:
        print(f"{competitor}, {counter.lookup(competitor)}")
    counter.report()

if __name__ == "__main__":
    main()
