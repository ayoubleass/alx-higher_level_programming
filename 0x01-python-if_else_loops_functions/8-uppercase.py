#!/usr/bin/python3
def uppercase(str):
    endchar = ""
    i = 0
    for c in str:
        if len(str) - 1 == i:
            endchar = "\n"
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            print("{}".format(chr(ord(c) - 32)), end=endchar)
        else:
            print("{}".format(c), end=endchar)
        i = i + 1
