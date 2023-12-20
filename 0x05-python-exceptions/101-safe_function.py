#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        if not isinstance(args, list):
            a, b = args
        else:
            a = sum(args)
        return fct(a, b)
    except ZeroDivisionError as e:
        print("Exception: {:}".format(e))
    except IndexError as e:
        print("Exception: {:}".format(e))
