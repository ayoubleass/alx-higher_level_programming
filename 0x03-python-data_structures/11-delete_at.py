#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    for i in range(0, len(my_list)):
        if idx == i:
            del my_list[i]
    return my_list