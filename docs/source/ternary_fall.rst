Addendum to comment: ternary_fall
===========

Operator of fall. Fall of the Triangle: 2 enters, 2 new, 3 out 

Preamble counter: "2^2/3"
    readjust case mod 17+8
    show value before modification
    readjust case mod 10+n

*************

cpt = mod(n, 10) + 1    # readjust case mod 17+8n
print(cpt)              # show value before modification)
if cpt == 11: cpt -= 1  # readjust case mod 10+n

*************
