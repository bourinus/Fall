# coding: utf-8
"""import this"""
import os 
from source.define import Define
from source.fall import *
#from ...docs.source import latex2p

def setup(*argm):
    """
    
    """

def main():
    print(" ________________ ")
    var = input("enter an integer: ")
    print(var)
    define_instance = Define()
    define_instance.define(var)
    print("------------------")
    print(define_instance.__defineInit)
    print(define_instance.__defineReturn)
    print(define_instance.__defineString)
    print("__________________end")
        
    
#     for i in range(0,1000):
#         var_define = Define()
#         var_define.define(i)
#         print(var_define.__defineReturn)
#     for i in range(0,10000):
#         fall_v = Define(i)
#         fall_v.define(fall_v)
#         other_fall = fall_v.__defineReturn
#         encorene = fall_v.__defineString
#         print(object.__str__(fall_v))        
if __name__ == '__main__':
    main()
