#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for letter in range(len(my_string)):
        if(my_string[letter] != 'c' and my_string[letter] != 'C'):
            new_string += my_string[letter]
    return new_string
