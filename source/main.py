# coding: utf-8
"""import this"""
import os
import site
import sys 
from source.define import Define
from source.rational import Rational
from source.rational import RationalException
#from source.fall import *
from appdirs import site_config_dir
from pip._internal.utils.appdirs import site_config_dirs
from _vendor.appdirs import site_data_dir
from source.fall import define
from random import Random
import random

#from ...docs.source import latex2p


site.addsitedir('.')  # Always appends to end
#sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../..'))
#sys.path.insert(2, os.path.abspath('../../source'))
sys.setrecursionlimit(1500)

def printConf():
    print('--------- sys path --------------')
    for elt in sys.path:
        print('_____elt in sys path_____')
        print(elt)
        print('_____________________end elt')
    print('----- end sys.pach --------')
    print('--------site_config_dir-------------')
    print(site_config_dir)
    print('site_config_dir')
    print('************************')    
    print('--------site_config_dirs-------------')
    print(site_config_dirs)
    print('site_config_dirs')
    print('************************')  
    print('--------site_data_dir-------------')
    print(site_data_dir)
    print('---------site_data_dir')
    print('************************')
    print('--------site.getusersitepackages------------')
    print(site.getusersitepackages())
    print('site.getusersitepackages')
    print('************site.getusersitepackages************')
    print('************************')
    print('--------site.getuserbase-----------')
    print(site.getuserbase())
    print('')
    print('************site.getuserbase************')

def ObjectDebug():
    print(" ________________ ")
    var = input("enter an integer: ")
    print(var)
    try :
        define_instance = Define()
        define_instance = Define(int(var), 1, "NotEmpty")
        print("---define_init---------------")
        print(define_instance.__define_init)
        print("---define_return---------------")
        print(define_instance.__define_return)
        print("---define_string---------------")
        print(define_instance.__define_string)
        print("__________________end")
    except:
        pass
    try :
        define_obj1 = Define()
        define_obj1 = Define(var)
        print("---define_init---------------")
        print(define_obj1.__define_init)
        print("---define_return---------------")
        print(define_obj1.__define_return)
        print("---define_string---------------")
        print(define_obj1.__define_string)
        print("__________________end")
    except:
        pass    #define_instance.define(var)
    #define_instance.__init__(int(var), 1, "NotEmpty")
def rationnalDebug(newNum, newDen):
    o1 = Rational()
    o1.denominator(newDen)
    o1.numerator(newNum)
    o1.simplify()
    
def rationnalDebugLoop(n):
    for i in range(1, n):
        rand1 = random.randint
        rand2 = random.randint
        rationnalDebug(rand1, rand2)    
        i += 1
    
#     for i in range(0,1000):
#         var_define = Define()
#         var_define.define(i)
#         print(var_define.__define_return)
#     for i in range(0,10000):
#         fall_v = Define(i)
#         fall_v.define(fall_v)
#         other_fall = fall_v.__define_return
#         encorene = fall_v.__define_string
#         print(object.__str__(fall_v))        

def setup(*argm):
    """
    TO DO    
    """

def main():
    printConf()
    #rationnalDebugLoop(15)

if __name__ == '__main__':
    main()
