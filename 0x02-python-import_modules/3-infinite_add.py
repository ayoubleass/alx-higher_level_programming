#!/usr/bin/python3
from sys import argv
sum = 0

for i in range(len(argv)):
    if i > 0:
        sum = sum + int(argv[i])

if __name__ == "__main__":
    print(sum)
