#!/usr/bin/python3
for firstDigit in range(0, 10):
    sperator = "\n"
    if firstDigit < 8:
        sperator = ", "
    for secondDigit in range(firstDigit + 1, 10):
        print("{:d}{:d}".format(firstDigit, secondDigit), end=sperator)
