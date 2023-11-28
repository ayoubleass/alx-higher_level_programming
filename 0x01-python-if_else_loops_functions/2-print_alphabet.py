#!/usr/bin/python3

firstChar = 'a'
lastChar = 'z'

while firstChar <= lastChar:
    print(firstChar, end="")
    firstChar = chr(ord(firstChar) + 1)
