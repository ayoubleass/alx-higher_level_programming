#!/usr/bin/python3
def fizzbuzz():
    word = "fizzbuzz"
    for i in range(1, 101):
        if i % 15 == 0:
            print("{} ".format(word), end="")
        elif i % 5 == 0:
            print("{} ".format(word[4:]), end="")
        elif i % 3 == 0:
            print("{} ".format(word[:4]), end="")
        else:
            print("{:d} ".format(i),  end="")
