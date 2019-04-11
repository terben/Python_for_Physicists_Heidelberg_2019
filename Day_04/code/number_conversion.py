# sample solutions for dec2binary and binary2dec

def dec2binary(n):
    """ return a positive int in binary representation (a string) """

    # We do not need any checking for a correct input!

    # We need to treat the special case n=0 separately!
    if n == 0:
        b = "0"
    else:
        b = ""
        while n != 0:
            n, r = divmod(n, 2)
            b = str(r) + b

    return b

def binary2dec(b):
    """ return the decimal value (an int) of a binary number
        (represented as a string)
    """

    # The conversion from binary to decimal is done
    # with the defining equation:
    #
    # n = \sum_{i=0}^k b_i 2**i
    #
    # where k can be obtained from the 'length' of the
    # binary number

    n = 0
    i = len(b) - 1
    for d in b:
        n = n + int(d) * 2**i 
        i = i - 1

    return n

# run a test case; we convert an integer twice and should
# get back the original number.
n = 123456789

s = dec2binary(n)
print(s)

n_new = binary2dec(s)
print(n_new)

print(n_new == n)
