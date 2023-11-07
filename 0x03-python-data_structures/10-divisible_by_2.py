#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result_list = [False] * len(my_list)
    for i, num in enumerate(my_list):
        if num % 2 == 0:
            result_list[i] = True
    return result_list
