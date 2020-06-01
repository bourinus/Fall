# Fall

No rhythm in arithmetic.
Fall: a stable operator of fall.

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
 * [Fire](https://github.com/google/python-fire)
 * Mock

 ```
 $ sudo apt install -y python3-pip
 $ sudo pip3 install fire mock
 ```


## Loading with SageMaths:
Open a terminal at the location of the the file fall.py and load sage:

```
$ sage
```
this gives acces to the sage console:
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

 Define is a paradoxe & repetition based function.

 * default test command: by analogy to the definition of the complex number i.
 ```
 sage: define(i)                            
 I
 -------
 1
 ###########
 I
 -------
 I
 ###########
 I
 -------
 -1
 ###########
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


### Literature

 * [The redemption game](https://github.com/bourinus/Fall/blob/master/doc/txt%20in%20progress/work_david.txt) - New type of proof & Prime number structure & Proof of God's Existence. On causes & consequences, values & judgment. 

 * [On hell](https://github.com/bourinus/Fall/blob/master/doc/txt%20in%20progress/On%20hell.txt) and paradise aka corruption & perfection are twin concepts: 'if one get the part undoubtedly it will get the  whole'. 

 * [On repetition & sorting](https://github.com/bourinus/Fall/blob/master/doc/txt%20in%20progress/structure.txt) How repetition can hide schemes and how to leverage them to achieve to see the scheme instead of his echoes.

 * [On the Euler’s theorem on polyhedrons](https://github.com/bourinus/Fall/blob/master/doc/txt%20in%20progress/On%20Euler%20%26%20polyhedrons.txt) - Maths are too corrupted folks.

### License :

 [GNU-GPL-V3](https://www.gnu.org/licenses/gpl-3.0.fr.html) 

 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 

  
