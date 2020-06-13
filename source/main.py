# coding: utf-8
"""import this"""
import os 
#import fall
#import fire
import exceptions
from rational import Rational
from rational import RationalException
from .exceptions import Fall_2
from .exceptions import Fall_3
from .exceptions import Fall_4
from random import random

def setup(argmn):
    """
    
    """

def hello(name="World"):
  return "Hello %s!" % name

def Q(name='q'):
  """
  Question manager
  """
  q = input("Question ?, Enter a number: ")
  fire.Fire(R(q))
  fire.Fire(hello)    


def R(name='r'):
  """
  Response manager
  """
  r = fall.define(fall.define(r))
  print("Results ! here it is:", r)
  fire.Fire(menu)
  fire.Fire(Q(r))
  fire.Fire(hello)    


def menu(name="Menu"):
  """
  Menu, first level
  """
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

if __name__ == '__main__':
    main()

    