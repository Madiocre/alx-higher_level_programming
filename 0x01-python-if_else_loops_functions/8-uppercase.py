#!/usr/bin/python3
def uppercase(s):
    for c in s:
        if 97 <= ord(c) <= 122:
            print(chr(ord(c) - 32), end="")
        else:
            print("{}".format(c), end="")
    print()
