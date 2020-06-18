# coding: utf-8
##change
#import math

from exceptions import Fall_2
from exceptions import Fall_3
from exceptions import Fall_4
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
    def __init__(self, defineInit=0, defineReturn=1, defineString="DefineInstance" ):
        self.defineInit = defineInit
        self.defineReturn = defineReturn
        self.defineString = defineString
    
    @property
    def defineInit(self):
        return self.__defineInit
     
    @defineInit.setter 
    def defineInit(self, newNum, ):
        if isinstance(newNum, int) == False:
            raise DefineException("Numerator must be an integer")
        self.__defineInit = newNum
         
    @property
    def defineReturn(self):
        return self.defineReturn
    
    @defineReturn.setter 
    def defineReturn(self, newDen):
        if isinstance(newDen, int) == False:
            raise DefineException("defineReturn must be an integer")
        if newDen == 0:
            raise DefineException("defineReturn cannot be zero")
        self.__defineReturn = newDen

    @property
    def defineString(self):
        return self.defineReturn
    
    @defineString.setter 
    def defineString(self, defineString):
        if isinstance(defineString, str) == False:
            raise DefineException("defineString must be an string")
        if defineString == '':
            raise DefineException("defineString can't be empty")
        self.__defineString = defineString
          

    def define(self, defineInit):
        """
        Define is a paradox & repetition based function & an interface to other paradoxical functions.
        1 entry, 3 equality, 2 paradigms.
        
        a gifted little liar, frequently interesting
        Always repeats it's entry, then print something else.
        Always has 3 consecutive values equals.
        Always hides an important information: the 6th value is never returned.
        """
        if isinstance(defineInit, str):
                self.__defineReturn = "Some to write or do"
                self.__defineString = "Someting telse"
        if isinstance(defineInit, list):
                self.__defineReturn = list #TO DO 
        
        if defineInit == '':
                self.__defineReturn = 0
        s2 = defineInit 
        for i in range(0, 3):
                print(defineInit) 
                print("-------")
                try:
                        s1 = defineInit
                        self.__defineReturn = (s1 ** i)
                        # if i!=3: print("###########")
                except Fall_4 as e:
                        Fall_4(e)
                        break                        
                pass
        #print("returned:",)
        #In Classes, doin't return set an attribute like following
        self.__defineReturn = s2
    


def setup(argmn):
    """
    
    """         

