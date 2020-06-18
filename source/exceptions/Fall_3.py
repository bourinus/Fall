# coding: utf-8
# -1    1
# j     1/j 
# j^2   1/j^2     
#
# 'j'  'J barre'


# from https://docs.python.org/fr/3.5/tutorial/errors.html
class B(Exception):         
    #
    # level 0
    print("contradiction:   -1=1            ... lvl 3")
    pass


class C(B):
    #
    # level 1
    print("Oops!            j=1/j           Trying again...")
    pass


class D(C):
    #
    # level 3
    print("Oops!            j^2=-1/j^2.     Trying again...")
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("check A+")
    except C:
        print("check C++")
    except B:
        print("Result check B:                  3/4 Green")
        print("-----")
