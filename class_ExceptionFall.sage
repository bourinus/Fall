class (Exception):
    pass
class A(Exception):
    print("Oops!  i^2=-1.  Try again...")
    pass
class C(B):
    print("Oops!  i^3=-i.  Try again...")
    pass
class D(C):
    print("Oops!  i^4=1.  Try again...")
    pass

for cls in [B, C, D]:
    try:
        print("############")
        raise cls()
    except D:
        print("D")
        print("  i^4=1.  ")
    except C:
        print("C")
    except B:
        print("B")
        print("base: b2=",b^5)  # CLASS CHECK
    except A:
        print("base: b=",b^4)
    
    print("############")