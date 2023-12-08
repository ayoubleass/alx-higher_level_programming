#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_new_list = []

    for num in my_list:
        if num not in unique_new_list:
            unique_new_list.append(num)
    return sum(unique_new_list)
