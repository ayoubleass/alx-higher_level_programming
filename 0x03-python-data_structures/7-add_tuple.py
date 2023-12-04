#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 2 and len(tuple_b) == 2:
        return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)
    return (tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1])
