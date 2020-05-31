# 
class A(Exception):         
    #
    # level 0
    print("print  i=i.")
    pass
class B(Exception):
    #
    # level 1
    print("Oops!  i^2=-1.  Try again...")
    pass
class C(Exception):
    #
    # level 3
    print("Oops!  i^3=-i.  Try again...")
    pass
class D(Exception):
    #
    # level 4
    print("Oops!  i^4=1.  Try again...")
    pass

for cls in [B, C, D,A]:
    print("############")
    try:
        raise cls()
    except D:
        print("check A")
    except C:
        print("check B")
    except B:
        print("check C")
        print("############")
    except A:
        print("Green")
