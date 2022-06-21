#!/usr/bin/python3
from decimal import DivisionByZero


def safe_print_division(a, b):
    r = 0
    try:
        r = a / b
    except ZeroDivisionError:
        r = None
    finally:
        print("Inside result: {}".format(r))
        return r
