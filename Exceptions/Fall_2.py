#'j'  'J barre'
#
#-1    1
#j     1/j 
#j^2   1/j^2     
#
#'j'  'J barre'

# from https://docs.python.org/fr/3.5/tutorial/errors.html
class B(Exception):         
    #
    # level 0
    print("print  -1=1")
    pass
class C(B):
    #
    # level 1
    print("Oops!  j=1/j   Try again...")
    pass

for cls in [B, C]:
    try:
        raise cls()
    except C:
        print("check C")
    except B:
        print("check B")

