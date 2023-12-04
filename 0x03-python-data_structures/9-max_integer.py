#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    large_num = my_list[0]
    for num in my_list:
        if large_num < num:
            large_num = num
    return large_num
