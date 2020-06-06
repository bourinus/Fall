# coding: utf-8
"""import this"""
import os 
import fall
import fire
import exceptions
from rational import Rational
from rational import RationalException
from exceptions import Fall_2
from exceptions import Fall_3
from exceptions import Fall_4
from random import random
from _ast import Try


def hello(name="World"):
  return "Hello %s!" % name


def Q(name='q'):
  q = input("Question ?, Enter a number: ")
  fire.Fire(R(q))
  fire.Fire(hello)    


def R(name='r'):
  r = fall.define(fall.define(r))
  print("Results ! here it is:", r)
  fire.Fire(menu)
  fire.Fire(Q(r))
  fire.Fire(hello)    


def menu(name="Menu"):
  c = input("Menu. Enter a choice: ")
  if c == 0: hello(c)
  if c == 1: help(c)
  if c == 2: Q(c)
  if c == 3: R(c)


def main():
  hello('')    
  c = input("Main. Enter a choice: 0 1 2 3")
  if c == 0: fire.hello(c)
  if c == 1: fire.help(c)
  if c == 2: fire.Q(c)
  if c == 3: fire.R(c)
  fire.Fire(menu)

"""
if __name__ == '__main__':
    m = True
    while m == True:
        try:
            raise Exception
        except Exception as err:
            print(err)
            break
"""
            
if __name__ == '__main__':
    
    for i in range(0, 10000):
        fall.define(i)
    
    try:
        print("____________________________")
        r5 = int(random())
        for i in range(0, r5):
            fall.define(r5)
        print("____________________________")            
    except Exception as e:
        print("An error occured", str(e))
        
    try: 
        rBad = Rational(0, 0)  # raise Denominator cannot be zero
    except RationalException as e:
        print("An error is raised", e)

    r1 = Rational(1, 2)
    print("r1 == " + str(r1))
    
    r2 = Rational(4, 1)
    print("r2 == " + str(r2))
    
    r = r1 + r2
    print("%s + %s == %s" % (r1, r2, r))
    
    rToSimplify = Rational(100, 50)
    print("[100,50] == %s" % (rToSimplify))

    r3 = Rational(1, 1)
    r3.numerator = 33
    r3.denominator = 44
    r4 = Rational(r3.numerator, r3.denominator)
    print("Prop r3: %s " % str(r3))
    print("Prop r3: %s simplify " % str(r4))
    
    try:
        menu(name)()
    except BaseException as err:
        print("Menu Error: ",str(err))
    finally:
        print("Exit menu...")
    
    try:
        main()
    except IOError as err:
        print("Main Error: ",str(err))
    finally:
        print("Exit Fall...")
        exit()
        

