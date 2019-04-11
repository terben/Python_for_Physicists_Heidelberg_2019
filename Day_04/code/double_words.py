#!/usr/bin/env python3

# The script reports word direct repetitions in ASCII text files.
# We also treat repetitions including punctuation marks and
# such separated by line feeds.

# The file that should be examined is read as a command line argument
# to the script

# An example call of the script is:
# python3 double_words.py double_words_test.txt

import sys
import string
import re   # for regular expressions (see below)

if len(sys.argv) != 2:
    print("Synopsis: %s file" % (sys.argv[0]), file=sys.stderr)
    sys.exit(1)

txtfile = open(sys.argv[1], 'r')

line_number = 1
last_word = ""  # see below for an explanation of that variable

for line in txtfile:
    # Idea: We split the lines at spaces, tabs and punctuation marks;
    # see exercise sheet
    words = re.split('\W+', line.rstrip())
    words = [ word for word in words if word != "" ]

    # we do not need to do anything for completely empty lines:
    if len(words) > 0:
        # test for word repetitions within a line:
        for i in range(1, len(words)):
            if words[i] == words[i - 1]:
                print("Repetition in line %d. Word \"%s\" at position %d!" % \
                      (line_number, words[i -1], i))

        # test for a word repetition with the end of the line of the
        # previous line. We do not need to do this for the very first line
        # (last_word was not yet set):
        if last_word != "":
            if words[0] == last_word:
                print("Repetition of the first word \"%s\" on line %d." % \
                      (last_word, line_number), end=' ')
                print("It occured at the end of the previous (non-empty) line!")

        # We store the last word for comparison with the first word of the
        # next line:
        last_word = words[-1]

    line_number = line_number + 1

txtfile.close()
