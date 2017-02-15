#!/usr/bin/env python

"""Count word occurence

USAGE: count_word_occurence.py [--options] input_file

Reports the occurence of each word, as lower-case, in an input file.
"""

import sys, argparse

__version__ = "0.1"
__author__  = "hien.le@vlimagrain.com"

def parse_arguments():
    """
    Get the command-line options
    """
    parser = argparse.ArgumentParser(description="Parse and count words")
    parser.add_argument('infile', nargs = '?', help = "Input file. REQUIRED")
    parser.add_argument("-v", "--version", action="store_true", help = "Prints the version")
    args  = parser.parse_args()

    if args.version:
        print "{} version {}".format(__file__, __version__)
        sys.exit()
    elif args.infile == None:
        parser.print_help()
        sys.exit()
    else:
        return args

class WordCounter:
    def __init__(self, description=None):
        self.description = "This is the word occurence counter"
        self.counter = dict()

    def add(self, word=""):
        lc = word.lower()
        if lc in self.counter:
            self.counter[lc] += 1
        else:
            self.counter[lc] = 0

    def sort(self):
        pass

    def lookup(self, word):
        return self.counter[word.lower()]

    def report(self):
        pass

#=== The real stuff ============================================================

def main():
    args = parse_arguments()
    #all_words = {}
    counter = WordCounter()
    with open (args.infile, "rb")as infile:
        for line in infile.readlines():
            words = line.split()
            for word in words:
                counter.add(word)
    counter.report()

if __name__ == "__main__":
    main()
