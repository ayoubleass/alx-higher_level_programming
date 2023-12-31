#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = []
    while i < list_length:
        try:
            if isinstance(my_list_1[i], int) and isinstance(my_list_2[i], int):
                new_list.append(my_list_1[i] / my_list_2[i])
            else:
                print("wrong type")
                new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            i = i + 1
    return new_list
