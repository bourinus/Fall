# coding: utf-8
##change
#import math
from source.exceptions.Fall_2 import *
from source.exceptions.Fall_3 import *
from source.exceptions.Fall_4 import *
#import numpy as np
#from exceptions import Fall_4
from builtins import str
from source import exceptions
#from pip._vendor.html5lib._ihatexml import charStringToList
#from pip._internal.utils.compat import str_to_display
#from builtins import str

class DefineException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class Define(object):    
    """
    Define Class
    """
    def __init__(self, define_init=0, define_return=1, define_string="DefineInstance" ):
        self.define_init = define_init
        self.define_return = define_return
        self.define_string = define_string
    
    @property
    def define_init(self):
        return self.__define_init
     
    @define_init.setter 
    def define_init(self, newNum, ):
        if isinstance(newNum, int) == False:
            raise DefineException("Define should be an integer")
        self.__define_init = newNum
        self.__define_string = "Definine initiate..."
         
    @property
    def define_return(self):
        return self.define_return
    
    @define_return.setter 
    def define_return(self, newDen):
        if isinstance(newDen, int) == False:
            raise DefineException("Define should be an integer")
        if newDen == 0:
            raise DefineException("define_return cannot be zero")
        self.__define_return = newDen

    @property
    def define_string(self):
        return self.define_return
    
    @define_string.setter 
    def define_string(self, define_string):
        if isinstance(define_string, str) == False:
            raise DefineException("define_string must be an string")
        if define_string == '':
            raise DefineException("define_string can't be empty")
        self.__define_string = define_string
          

    def define(self, define_init):
        """
        Define is a paradox & repetition based function & an interface to other paradoxical functions.
        1 entry, 3 equality, 2 paradigms.
        
        a gifted little liar, frequently interesting
        Always repeats it's entry, then print something else.
        Always has 3 consecutive values equals.
        Always hides an important information: the 6th value is never returned.
        """
        if isinstance(define_init, str):
                self.__define_return = "Some to write or do"
                self.__define_string = "Someting telse"
        if isinstance(define_init, list):
                self.__define_return = list #TO DO 
        
        if define_init == '':
                self.__define_return = 0
        s2 = define_init 
        for i in range(0, 3):
                self.__define_string =  self.__define_string +":"+str(i) 
                #print("-------")
                try:
                        s1 = define_init
                        self.__define_return = (s1 ** i)
                        # if i!=3: print("###########")
                except exceptions.Fall_4:
                        #(exceptions.Fall_4.A.__context__.__delete__(self))
                        break                        
                pass
        #print("returned:",)
        #In Classes, doin't return set an attribute like following
        self.__define_return = s2
    


def setup(argmn):
    """
    
    """         

