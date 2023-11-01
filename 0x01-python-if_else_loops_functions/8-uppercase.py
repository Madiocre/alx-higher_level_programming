#!/usr/bin/python3
def uppercase(s):
    result = ""
    for c in s:
        if 97 <= ord(c) <= 122:
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
