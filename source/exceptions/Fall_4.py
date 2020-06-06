# -*- coding: utf-8 -*-

class A(Exception):         
    #
    # level 0
    print("contradiction:   i=i            ... lvl 1")
    pass


class B(Exception):
    #
    # level 1
    print("Oops!            i^2=-1         Trying again...")
    pass


class C(Exception):
    #
    # level 3
    print("Oops!            i^3=-i         Trying again...")
    pass


class D(Exception):
    #
    # level 4
    print("Oops!            i^4=1          Trying again...")
    pass


for cls in [A]:
    try:
        raise cls()
    except A:
        print("Result check A:                 1/2 Green")
        print("-----")

