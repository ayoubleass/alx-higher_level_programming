#!/usr/bin/python3

lastChar = ", "

for i in range(0, 100):
    if i < 10:
        print("0{:d}".format(i), end=lastChar)
    elif i > 9:
        if i == 99:
            lastChar = "\n"
        print("{:d}".format(i), end=lastChar)
