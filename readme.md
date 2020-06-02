# Fall

Fall: stable operators of fall.
Exponentiation, paradox & repetition based functions in python.


Seeks & destroys paradoxes with new recursions, proofs, sequences, formalism. github.com/bourinus/Fall python programmer try

[Project address](https://github.com/bourinus/Fall) 

[Readme address](https://github.com/bourinus/Fall/blob/master/readme.md)

### Current State: 
1 stable function: define() only accessible from SageMath console.

## Getting Started

### Environment:

 Operating system: 
 * [ubuntu](https://ubuntu.com/download)

 Software:  
 * [Sagemaths](https://www.sagemath.org/)	 SageMath version 9.0, Release Date: 2020-01-01 

 ```
 $ sudo apt install -y sagemath
 ```

 * [Python](https://www.python.org/downloads/release/python-382/) 	Python 3.8.2
 ```
 $ sudo apt install software-properties-common
 $ sudo add-apt-repository ppa:deadsnakes/ppa
 $ sudo apt update
 $ sudo apt install python3.8
 ``` 

### Install Python modules used:
 * [Mock](https://pypi.org/project/mock/) test library, allows you to replaces parts of your system under test with objects.
 * [Fire](https://github.com/google/python-fire)  automatically generates command line interfaces (CLIs) from any Python object.

 ```
 $ sudo apt install -y python3-pip
 $ sudo pip3 install fire mock
 ```

## Loading with SageMaths:
Open a terminal at the location of the the file fall.py and load sage:

```
$ sage
```
this gives access to the sage console:
```
sage: load("fall.py")  
sage: define((6/5)*(4/3)) 
```
## Executing with terminal & python (not working)
```
$ python3.8 fall.py
```

# Testing

## testing: define()

First understanding:
define() is a paradox & repetition based function.
```
always repeats it's entry, then print something else.
always has 3 consecutive values equals.
always hides an important information: the 6th value is never returned.
```
* default test command n°1: 
```
sage: define(1)    sage: define(I)      sage: define(0)      sage: define(2)
1                  I                    0                    2
-------            -------              -------              -------
1                  1                    1                    1
1                  I                    0                    2
-------            -------              -------              -------
1                  I                    0                    2
1                  I                    0                    2
-------            -------              -------              -------
1                  -1                   0                    4
returned:          returned:            returned:            returned:
1                  I                    0                    2
```
* test command n°2: 
```
 sage: A = Matrix([[0,3,6],[1,4,7],[2,5,8]])
 sage: define(A)
 [0 3 6]
 [1 4 7]
 [2 5 8]
 -------
 [1 0 0]
 [0 1 0]
 [0 0 1]
 ###########
 [0 3 6]
 [1 4 7]
 [2 5 8]
 -------
 [0 3 6]
 [1 4 7]
 [2 5 8]
 ###########
 [0 3 6]
 [1 4 7]
 [2 5 8]
 -------
 [ 15  42  69]
 [ 18  54  90]
 [ 21  66 111]
 ###########
```


# Why this paradox based function is interesting:
 
 This gives access to other class of functions based on principles: counting/processing differently.
 And because this gives an error management based on the complex number j
 ```
 contradiction:   i=i            ... lvl 1
 Oops!            i^2=-1         Trying again...
 Oops!            i^3=-i         Trying again...
 Oops!            i^4=1          Trying again...
 Result check A:                 1/2 Green
 -----
 contradiction:   -1=1            ... lvl 3
 Oops!            j=1/j           Trying again...
 Oops!            j^2=-1/j^2.     Trying again...
 Result check B:                  3/4 Green
 -----
 check C++
 check A+
 contradiction:   -1=1            ... lvl 2
 Oops!            j=1/j           Trying again...
 Oops!            j^2=-1/j^2.     Trying again...
 Result check B:                  1/4 Green
 -----
 check C+
 check A++
 hello: test test_hello (__main__.MenuTest)
 	python hello.py  # Hello World!
 	python hello.py --name=David  # Hello David!
 	python hello.py --help  # Shows usage information.
 .
 ----------------------------------------------------------------------
 Ran 1 test in 0.000s
 
 OK
 ```

# How to deal with paradox based functions:
  Studying repetition and global behavior gives faster computation using principles.
   
 ```
 1/2   5/10  2/5     0.2  2/10  1/10     1/100   100/100  1/10   10/1   10    1/10
 1/3   5/3   30/5    6    6/10  3/10     9/100    90/100  9/10   10/9   10/9  9/10
 1/4   5/7   70/5    14   14/10 7/5      49/50    98/100  1/50   50/1   50    1/50
 ```


### Literature:
 * [The Glass Bead Game](https://en.wikipedia.org/wiki/The_Glass_Bead_Game) Hermann Hesse, 1941. A book about the arithmetic of God.

 * [The Redemption game](https://github.com/bourinus/Fall/blob/master/doc/txt%20in%20progress/work_david.txt) - New type of proof & Prime number structure & Proof of God's Existence. 
 On causes & consequences, value & judgment. 

 * [On hell](https://github.com/bourinus/Fall/blob/master/doc/txt%20in%20progress/On%20hell.txt) AND paradise aka corruption & perfection are twin concepts.
 'if one get the part undoubtedly it will get the  whole'. 

 * [On repetition & sorting](https://github.com/bourinus/Fall/blob/master/doc/txt%20in%20progress/structure.txt) - How repetition can hide schemes and how to leverage them to achieve to see the scheme instead of his echoes.

 * [On the Euler’s theorem on polyhedrons](https://github.com/bourinus/Fall/blob/master/doc/txt%20in%20progress/On%20Euler%20%26%20polyhedrons.txt) - Maths are too corrupted folks.

### License :

 [GNU-GPL-V3](https://www.gnu.org/licenses/gpl-3.0.fr.html) 

 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 

  
