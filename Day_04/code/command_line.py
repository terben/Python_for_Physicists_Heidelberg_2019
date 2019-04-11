# short demonstration script on command line arguments

import sys

# command line arguments are stored as strings in the 'sys.argv' list

# The first argument contains the program name:
print("program name: {}".format(sys.argv[0]))

if len(sys.argv) > 1:
    print("You provided the following command line arguments:")

    for arg in sys.argv[1:]:
        print(arg)
