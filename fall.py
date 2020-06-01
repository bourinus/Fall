import fire
import numpy as np

from Exceptions import Fall_4 as class_Fall4
from Exceptions import Fall_3 as class_Fall3
from Exceptions import Fall_2 as class_Fall2

class Fall(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		self.arg = arg


def define(b):
	if isinstance(b, str): return b [::-1]
	if isinstance(b, list): return b [::-1]
	
	if b=='': return 0
	s2=b 
	for i in range(0,3):
		print(b) 
		print("-------")
		try:
			s1=b
			print(b**i)
			#if i!=3: print("###########")
		except ValueError:
			ValueError.class_Fall4(my_list(i)[i])
			break			
		pass
	print("returned:", )
	return b

def infinite_2loop(p): # only 0 
	if p==24: return 26
	if p!=0: # only 0 is stopped
		try:  		
			infinite_2loop(p-1)
			print(p)
			if infinite_2loop(p-1)==0: print("###########")
		except ValueError:
			ValueError.class_Fall2(D)
		pass

def infinite_3loop(p): # only 0 
	if p==23: return 27
	if p!=0: # only 0 is stopped
		try:  		
			infinite_3loop(p-1)
			print(p)
			if infinite_3loop(p-1)==0: print("###########")
		except ValueError:
			raise ValueError.class_Fall3(D)
		pass

def sh4d0w(a,b,c):
	r=b1^a*b2^b*b3^c
	#####################
	print("##########")
	r_10=factor(10*r)
	b=2
	e=ln(10*r)/ln(b)

	print("10*r:	", r_10)
	print("base: 	",b)
	print("exp: 	",e)
	print("##########")
	####################

	print("result:	", r)
	exp=(e-1)
	ratio=10*r*b
	print("base:",b,"exp:",e-1, "ratio", ratio)




def signature_25(n): # 1143 
	for p in range(0,25):
		x=mod(n,25-p)
		print(x)
		pass	

def signature_15(n): #19
	for p in range(0,15):
		x=mod(n,15-p)
		print(x)
		pass	

def signature_5(n): # 7
	for p in range(0,5):
		x=mod(n,5-p)
		print(x)
		pass	

def counter_56(n):
	if n==1: return 5/6
	if n==2: return 10/6
	if n==2: return 15/6
	if n==3: return 20/6
	if n==4: return 25/6
	if n==6: return 5/6
	if n==7: return 35/6
	if n==8: return 40/6
	if n==9: return 45/6
	if n==10: return 10/6
	pass
	print(n)
	counter_56(mod(2*n,100))

def counter_65(n):
	#if n==1: return 25/36
	#if n==2: return 100/36
	#if n==2: return 225/36
	#if n==3: return 20/36
	#if n==4: return 25/36
	#if n==6: return 36/36
	#if n==7: return 49/36
	#if n==8: return 64/36
	#if n==9: return 81/36
	#if n==10: return 25
	#pass
	#print(n)
	#counter_65(mod(2*n,100))


	if n==1: return 25/36
	if n==2: return 100/36
	if n==2: return 225/36
	if n==3: return 20/36
	if n==4: return 25/36
	if n==6: return 36/36
	if n==7: return 49/36
	if n==8: return 64/36
	if n==9: return 81/36
	if n==10: return 100/4
	print(n)
	counter_65(mod(4*n,100))
	if n==8: counter_65(n)
	pass


def spell(n):
	cpt1 = mod(n,11)
	cpt2 = mod(n,9)

	print(n,cpt1,cpt2)
	
	cpt3 = -mod(n,11)
	cpt4 = -mod(n,9)

	print(n,cpt3,cpt4)

	if cpt1==0:
		n+=1
		print ("2*n/3-1: ",2*n/3+1)
		return2Var(2*n/3+1)

	


##############################################
# Babylon in a nutshell: 2 1 2 5 12

def Tower(n):
	print(n, "#########")
	if mod(n,8)==0 : 
		while Tower(n/8)==mod(n,8):
			return n/8
		print("start :" ,n ,":", n-7*n/8, 7*n/8, 5*n/8, 3*n/8, n/4)
		cpt=n/8
	return n/8

	print("start :" ,n, n-7*n/8)

#	#################
#	#########################
#	if 	mod(n,8)==7: 
#		print(n, "!!!!!!!!")
#		Tower(mod(cpt)) 
#	if 	mod(n,6)==5: 
#		print("round 3:", cpt)
#		cpt=+1
#		Tower(mod(n,4*n+1))
#
#	if 	mod(n,2)==1: 
#		print("round 1:", cpt)
#		cpt=+1
#		Tower(mod(n,2*cpt+1))
#	if 	mod(n,4)==3: 
#		print("round 2:", cpt)
#		cpt=+1
#		Tower(mod(n,3*cpt+1))
#
#	pass
#	if 	mod(n,7)==5: Tower(mod(n,6*n+5))
#	if 	mod(n,5)==4: Tower(mod(n,7*n+1))
#	if 	mod(n,3)==3: Tower(mod(n,8*n+1))
#	if 	mod(n,3)==2: Tower(mod(n,9*n+1)) 




	# 0 : 5 win
	# 1 : 0 win fails
	# 0 : 5 fails


def Babel(n):
	if n!=4 or n!=2 or n!=1:
		print(n)
		Tour(n)
	else:
		Collatz(n)			
	return n
################################################

##############################################
# Colatz in a nutshell: 0 1 4 2 
# Babel in a nutshell: 2 1 2 5 12

def Tour(n):	
	#########
		# first case
	if 	mod(n,2)==0: return n/2
	if 	mod(n,2)==1: return 3*n+1
	if 	mod(n,4)==3: tour(n-1)
	if 	mod(n,4)==1: tour(n)

def Collatz(n):
	if n!=4 or n!=2 or n!=1:
		print(n)
		Tour(n)
	else:
		Collatz(n)			
	return n
################################################





### Check counter
# RSA2048 ?
#######
# rep ?)
# 92374854524656789567744752855350842546736021853497806217842186333020791425504181078568912504491547407349523284013957728710029199137924642528520539228730192737607545158535623836454551796389684665060
# ??
#
#RSA2048/92374854524656789567744752855350842546736021853497806217842186333020791425504181078568912504491547407349523284013957728710029199137924642528520539228730192737607545158535623836454551796389684665060

RSA2048=25195908475657893494027183240048398571429282126204032027777137836043662020707595556264018525880784406918290641249515082189298559149176184502808489120072844992687392807287776735971418347270261896375014971824691165077613379859095700097330459748808428401797429100642458691817195118746121515172654632282216869987549182422433637259085141865462043576798423387184774447920739934236584823824281198163815010674810451660377306056201619676256133844143603833904414952634432190114657544454178424020924616515723350778707749817125772467962926386356373289912154831438167899885040445364023527381951378636564391212010397122822120720357

def is_prime(n):
	x=mod(n,1000)
	y=mod(x,9)
	print(n, x)
	
	if x==439:x=mod(23*x,19)
	if x==23: x=mod(17*x,13)
	if x==19: x=mod(11*x,7)
	print(n, x)
	########################

	print(true	)
	x=mod(7*x,5)
	print(x)
	pass
	print(true	)
	y=mod(x,3)

		
	if x!=7 and x!=5 and x!=3:
		is_prime(x)
	
	
		
	pass


def cpt_boolean(a, b, c, x, y, z):
	#discriminate between two Pythagorean triplets
	# 3 4 5 vs 1 1 2
	#	cpt_boolean(a,b,a-b,1/cpt,y,cpt^2-y^2)
	#	x	13	169		
	#		12	144
	#			
	#	3	4	5	
	#	9	16	25 is 
	#
	# ( ( x-1 . x-2 )^2 + 1 )^2
	##### Not counting step, using parity	
	print(a,b,c,x,y,z )
	if a==8:cpt=3/4*a

	cpt=3*(a^2-(c^2-b^2))/4
	if z==-3287:
		if y!=-659:
			cpt_boolean(3,b,4*a+b,z,x-2,y)
			cpt=a
		############################			
		cpt=6*(4*b-4/3*z-y)/7
		print(a,b,c,x,mod(y,9),mod(z,9) )
		cpt_boolean(7, x-y, 5*a+c, 3,x,4*x+y)

	if a==3 and b==4 and c==5:
		print(true	)

	if a==0 and	b==0 and c==0 and x==0 and y==0 and z==0:
		cpt_boolean(8*a^2, 7*b, a+b+c, 6*x, 5*y, z-5*b)
	pass
	print(a,b,c,x,y,z )
	print("okokok", cpt)
	print("#################" )
	print("rappel :",	"	",	a,	"	",	b,	c)
	print("rappel :",	"	",	x,	"	",	y,	z)
	#
	# y=-3946 		mod(z+y,9)=5		3849 mod(z+y,11)=10  (x+y) 
	# z=-3287 		mod(z,9)=7 			3287 mod(z,11)=9     -z
	# x+y=-659  	mod(y,9)=7  		659  mod(y,11)=10    -y
	#			
	#		659  	mod(y,9)=5  		659  mod(y,11)=10
	#		3946 	mod(z+y,9)=7		3849 mod(z+y,11)=10
	#		3287 	mod(z,9)=2 		    3287 mod(z,11)=9
	#			
	#			 3949-6*659=-5 3949/5=3959
	#			 3287-5*659= 8 3284/8=5*659 	2*659 + 1 = 1319
	#			  659-6*569= 4*659   			659 = 3^6 - 70.
	#	 mod      	9 		 				 11 		  			18/10
	# U(n)=n*659: 	0 2 4 6 8 1 3 5 7 1 3 	: 0 10 9 8 7 6 .5 4 3 2 1
	# U(n)=n*3287: 	0 2 4 6 8 1 3 5 7 0 2	: 0 .9 7 5 3 1 10 8 6 4 2 
	# U(n)=n*3949: 	0 7 5 3 1 6 4 4 2 0 7	: 0 .0 0 0 0 0 .0 0 0 0 0 
	#		       8/7  					7                   	6/5
	# U(n)=n*659:	0 3 6 1 4 7 2 5 0 3 6 	: 0 1 2 3 4 5 6 0 1 2 3
	# U(n)=n*3287:	0 7 6 5 4 3 2 1 0 7 6	: 0 0 4 1 5 2 6 0 4 1 5
	# U(n)=n*3949:	0 5 2 7 4 1 6 3 0 5 2  	: 0 1 2 3 4 5 6 0 1 2 3
 	# 				9 						  7						16/9
	# U(n)=n*751:	0 4 8 3 7 2 6 1 5 0 4   : 0 3 6 9 1 .4 .7 10 2 5 8
	# U(n)=n*658:  	0 1 2 3 4 5 6 7 8 0 1 	: 0 9 7 5 3 .1 10 .8 6 4 2
	# U(n)=n*607:	0 4 8 3 7 2 6 1 5 0 4 	: 0 2 4 6 8 10 1. .3 5 7 9
	#	 mod      	9 		 				  11 		  	      		9/11
	# U(n)=n*569: 	0 2 4 6 8 1 3 5 7 1 3 	: 0 10 9 8 7 6 5 4 3 2 1
	################################################################
	#	659 & 661 form a twin prime pair.
	#		is a Sophie Germain prime: 2*659 + 1 = 1319 is also prime
	#		= 3^6 - 70 & is the 120th prime number 659 divides 12^7 - 1
	#	569 & 571 form a twin prime pair.
	#		= 13^2 + 20^2
	#		is in a primitive Pythagorean triple: 569^2 = 231^2 + 520^2
	#		has the representation 569 = 2^9 + 57.
	#		divides 86^4 - 1.
	##########################################################
	#			2,	3,	5,	7	ex
	#			3,	5,	7,	11	ex 
	# Quadruplet of primes beyond 10 000 :  (p, p+2, p+6, p+8).
	#			5, 	7, 	11, 13 
	#			11, 13, 17, 19
	#
	#(1)			5651, 5653, 5657, 5659
	#(2)			9431, 9433, 9437, 9439 <-- 439 is not prime exception aka the 13th pb 19*23
	#
	##Pythagorean triplets	
	#	Primitives:
	#	1:			3,	4,	5				9	16	25 			
	#	2:			5,	12,	13				25	144	169
	#	Test:		569 231 520 			569 13^2 20^2  Bases: 10,13,20
	#	Primality	*	*	*				*	*	 not   
	#
	#
	#								
	#(9 431, 9 433, 9 437, 9 439) : 431,433,437,439 : *	*	*  !!!  <-- 439 is not prime
	#(5 651, 5 653, 5 657, 5 659) : 651,653,657,659 : *	*	*	*
	#(56 51, 56 53, 56 57, 56 59) : 51,	53,	57,	59 : *	*	*	*	
	#(94 31, 94 33, 94 37, 94 39) : 31,	33,	37,	39 : *	not *   ok : 39 = 3 * 13 ok but contradiction no go further
	#							
	#							 	31,		33,		37,		39	 	Similiarity						
	#(9 431, 9 433, 9 437, 9 439):	431,	433,	437,	439  	Results
	#								831, 	833, 	837, 	839 	Hypothesis
	#							831=3×277	?		?		*
	#							*		833=3^2×43 	*
	#									*		837=3^3×31 			Check
	#
	#
	#(9 431, 9 433, 9 437, 9 444): 431, 433, 437, 444 : *	*	*	no
	#									*2	* 	^2
	#1031 1033 1137 1139
	#
	#
	#			31,	33, 56, 65	= 1089 3136 4225 : 	10 	31 	25
	#
	# 569^2 = 231^2 + 520^2
	#																									37 is prime		
	#																			   	0 5 6 7 	0	13  3		
	#			 																   	0 5 9 8 	4   17  7
	#																 			   	0 4 5 7     7   11  1
	#																				0 3 6 9 	0   18  8
	#
	#	Needed:
	# 		5 primitives Quadruplet of primes nor more & basis 10,13,20
	#		exception 





def cpt42_Square(n, lvl):
	if n==lvl^2:
		if lvl==7: lvl=lvl^2		
		if lvl==6: lvl=lvl^3		
		if lvl==5: 
			print(n,lvl)
			n+=1  
			lvl=lvl-5 	
		if lvl==4: 
			lvl=0
			print(n,lvl)
		if lvl==3: n+=2
		if lvl==2: 
			n^2
			n-=1
		print(n,lvl)
	lvl=lvl^2
	if n==lvl:
		if lvl==2: lvl=lvl^3		
		if lvl==1: lvl=lvl^2		
		if lvl==1: n+=1
	print(n,lvl)




def cpt13_Triangle(n,lvl):
	#001  100
	#112  011
	#345  110
	# count in level of primes
	# OUTPUTS
	#	1*  
	# 	2*
	# 	3*
	#################
	if 	3*lvl==lvl^3: # only 
		if lvl*lvl==lvl+lvl: 
			lvl=mod(lvl,10)
		lvl=10
	###############################
	if lvl==7: 	cpt13_Triangle(n,0)	
	if lvl==5: 	cpt13_Triangle(n,2)	
	if lvl==3: 	cpt13_Triangle(n,6)	
	#################
	#################
	if lvl==8: 	cpt13_Triangle(n,9)	
	if lvl==6: 	cpt13_Triangle(n,5)	
	if lvl==7: 	cpt13_Triangle(n,3)	
	###############################
	#	return n+lvl,lvl+1
	return n*lvl^2 

def  Interpreter(x):
	#	return n+lvl,lvl+1

	a=(x^2-1)
	b=(x^3-1)
	c=(x^4-1)
	d=(x^5-1)
	print(	"	",	a,	b,	c, d)
	n=		a-b+c
	lvl=	a+b+c
	print(n, lvl)

	if a+b+c+d+n+lvl==-8:
		recall=1
		n=-n
		print(	"toto", "	2",	"4",	"6",	"8",	"!"	)
		print(	n, lvl, "	2",	"3",	"5",	"7",)

	if recall==1:
		lvl=lvl^2
		print(lvl, "!")

	print(	"	", 	x,	n, lvl)
	if recall==1:
		n=	a-b+c
		lvl=a+b+c+d
		x=	a+b+c
	print(	"	", 	x,	n, lvl)

	#####################
	print("#################" )
	r0=mod(lvl,2)
	print("#################" )
	r1=mod(mod(lvl^2,11),20)
	print("#################" )
	r2=mod(mod(lvl^3,9),20)
	print("#################" )
	q1=r1+r2*r2*r0
	q2=r0+r1*r2*r1
	q3=r2+r1*r1*r2
	print("rappel :",	n, lvl,			"(",	mod(lvl,10), ")")
	print("check 1:", 	"	",	n/lvl, 	lvl)
	print("check 2:	", 	lvl^2, 	lvl^3)
	print("check 3:	", 	n^3, 	n^2)
	print("Results:	", 	r0,		r1,		r2 )
	print("Results:	", 	q1,		q2,		q3 )

	A="Interpreter"
	if r0==0: A=r1+r2
	if r1==1: A=r2+r0
	if r2==0: A=r2+r0
	B="Interpreter"
	if r0==1: B=r0+lvl
	if r1==2: B=r2+lvl
	if r2==3: B=r1+lvl
	C="Interpreter"
	c=mod(lvl,2)==1
	print("Answer A:", c)
	print("Answer B:", B)
	print("Answer C:", A)

	print("#################" )
	print(cpt13_Triangle(lvl+2,n+lvl^2)/9)
	print("#################" )
	

def cpt_Syracuse(n, lvl):
	#
	#0 1 4 2 5 6 5 3 2 1
	#7 1 2 3 1 4 1 5 6

	#################
	return n,lvl
	#################
	if lvl==5: 
		if n==0:
			if mod(n,2)==0: 	return n/2
			if mod(n,2)==1: 	return 3*n+1			
	if lvl==6:
		if n==1:
			if mod(n,3)==2: 	return n/3
			if mod(n,3)==4: 	return 4*n+2
	if lvl==7:
		if n==3:			
			if mod(n,5)==0: 	return n/4
			if mod(n,5)==1: 	return 5*n+3
	if n==4:			
		if mod(n,2)==0: 	return n/5
		if mod(n,2)==1: 	return 4*n+6
		cpt_Syracuse(lvl,n)
	pass
	print(n)






# Counter for a.b=c
#
def check(p,q,r):
############################## 1 2 3 4 (5)
# 3n^2 +25n+ 1 ?
# 3n^2 +19n+ 1 ?
	cpt=p+q+r	#cpt=mod(cpt,16)
	if cpt==0:
		if r/q==p:
			print('check 1')
			cpt+=1
		if r/p==q:
			print('check 2')
			cpt+=1
		if p*q==r:
			print('check 3')
			cpt+=1
	pass 
########################## 3 2 1 0
#	0 1 2 3	4
#	if cpt^2=9
#	if cpt^2=4
#	if cpt^2=25
#   if cpt^2=1/0 				"NFG" 			 
###############

	if cpt^2==16:
		if mod(cpt,18)==0:
			cpt+=10
			print('hello, check')
			print('true', r/q, r/p, p*q)
		check(p+1,q+2,r+3)
		check(r/q,r/p,r/3)
	cpt=cpt^2
	if cpt==25:	
		# second exit & collatz algorihtm
		if mod(cpt,18)==1:
			r=3*r
			print('false... testing', cpt)
			mod(r/q,9), mod(r/p,9), mod(p*q,9)
	cpt=(cpt+1)^2
	pass
	check(q,p,r)
##############################
	lvl=mod(p+q+r,9)
	if cpt==0:
		return(r,p,q)	
		lvl+=1
	if cpt==4:
		lvl==lvl^2
		lvl+=1
	if cpt==5:
		return(3,4,5)
		lvl+=1
	if cpt==3:
		return(q,p,100)
		lvl=-1 
		return(p,q,r)
	pass			
##############################
	if cpt==14:
		if cpt==15: 
			check(r,q,p) 
			print('test 1', mod(r,11), mod(q,11), mod(p,11))
		if cpt==16:
			cpt+=5	
			check(r,p,q) 
			print('test 2', mod(r,11), mod(p,11), mod(q,11))
			cpt+=6
		if cpt==15:
			check(p,q,r)
			print('test 3', mod(p*q,11), mod(r*p,11), mod(r*q,11))
			cpt+=4
		if cpt==17:
			check( mod(r,11), mod(q,11), mod(p,11) )
			print('checked')
	pass
	cpt+=2
#######################			
	if cpt==20:
		print(p, q, r)
		cpt+=1
	print('true')


###
def counter(n):
	print(n) 					# show value before modification)
	x=mod(n,9)
	y=mod(n,11)
	cpt=3*n+19+1				# 0 -> 20
	print(cpt) 					# show value before modification)
	u=mod(cpt,9)
	x=4*u+19*u-11*n
	# lenght max =5
	#####################################
	cpt+=5
	x=mod(u,10)
	counter(n)
	if x==n:
		print(u) 					# show value before modification)
		u+=1 	
		pass
	#################
	counter(x)
	




def Ternary_fall(n,x):	
	# 2 enters, 2 new, 3 out "2^2/3"
	## Fall of the Triangle

	cpt=mod(n,10)+1				# readjust case mod 17+8n
	print(cpt) 					# show value before modification)
	if cpt==11: cpt-=1 			# readjust case mod 10+n
	#############################	
	if n>25:	 				# limit
		## Fall of ternary
		y=mod(x,9)
		# intermingling y,x,n for 3 new variables.
		# circle  	(x-i)^2	+	(x+i)^2					 =1 
		# root 			i   &		-i  	  	S=-2i 	P=1 
		#
		#			i 		-i
		#	y 		x	 	n
		a=y^2+i*x*y-x^2 	
		Ternary_fall(n,a)
		b=y^2+i*x*y-x^2
		Ternary_fall(a,b)
		c=y^2+i*x*y-x^2
		Ternary_fall(x,c)
		d=x^2+i*x*n-n^2
		Ternary_fall(n-a*b*c,d)
		# new problems with 3 variables
	   # no x beyond this point
	   ###########################
	pass
	return a,b,c

def Quaternary_fall(a,b,c,d):	
# 4 enters, 1   out
## Fall of the Square 			2/2 out "2^2.2/3.5" "6/5"

	cpt=6						# readjust case mod 17+8n
	print(cpt) 					# show value before modification)
	if cpt==7: cpt-=1 			# readjust case mod 10+n
	#############################	
	if n>25:	 				# limit
		#enter only 12 or 24 ? many square not allowed here
		if d==5: 
			if a==4: Quaternary_fall(a,b,c,3) 
			if b==3: Quaternary_fall(a,b,c,2) 
		
			# 1 2 3 5
			if d==6: 
				if a==3: Quaternary_fall(a,b,c,4) 
				if b==2: Quaternary_fall(a,b,c,1) 
		
			# 2 4 6 8	 
			if d==16: 
				if b==3: Quaternary_fall(a,b,c,4) 
				if c==0: Quaternary_fall(a,b,c,14) 
		pass 
		### lvl 14	# a b c d: x
		if d>14: 
			if a^2+b^2==c^2:
				Quaternary_fall(a,b,c,14)
				Ternary_fall(-a,b,-c)			
			Quaternary_fall(a,b,c,12)
		## lvl 17 	# 1 2 3 4: y
		if d>17: 
			if Quaternary_fall(a^2+b^2-d^2) ==1: 
				Quaternary_fall(b,c,d,4)
			Quaternary_fall(a,b,c,19)			
		pass
		## lvl 7	# yes or no
		if Binary_fall(a^2+b^2-c^2) == 1:
			Quaternary_fall(-a,b,-c,14)
		if Binary_fall(a^2+b^2+c^2) == 0:
			Quaternary_fall(-a,d,-c,12)
	if d==19: 
		pass
	return a,b,c,d


def Quint(n):
	## Fall of 5 
	## poney

	cpt=mod(n,5)+1				# readjust case mod 17+8n
	print(cpt) 					# show value before modification)
	if cpt==7: cpt-=1 			# readjust case mod 10+n
	#############################	
	if n>5:		 				# limit
	##
	## Fall of illusion
	# fall of fairy 3 6 9	
		if n==4:
			if d==1: 	Quint(x^2+y^2)	
			if d==2: 	Quint(d/10)
			if d==3: 	Quint(120)	 
			# Fall of many  3 4 7
			if d==5: 	Quint(81)
			if d==4: 	Quint(25*x^2+20*x^2)
			if n==3: 	return 120 
			# 0 1 1 2 3 4 5 120
			if n==d: return 7
			if n==3: return 3
			pass	# Final remembrance of d
			Quint(3*4*6)
		pass
	print(n)
	return n	


def Binary_fall(n):
	# 1 number in, 1 out 
	## Fall of 2 

	cpt=mod(n,8)+1				# readjust case mod 17+8n
	print(cpt) 					# show value before modification)
	if cpt==8: cpt-=1 			# readjust case mod 8
	#############################
	# disappearance of variable x: save & forget
	# hunting mod 64 & the usage of variable 'x'
	if n>20:	 				# limit
		# 0 4  
		if n==0: 
			if cpt==4: 	Binary_fall(2)
			else: 		Binary_fall(8)	
			cpt-=4
		# 3 6
		if n==3: 
			if cpt==6: 	Binary_fall(9)
			else: 		Binary_fall(3)	
			cpt-=3
		# 5 7 
		if n==5: 
			if cpt==5: 	Binary_fall(7)
			else: 		Binary_fall(6)	
			cpt-=2
		# 1 9 
		if n==7: 
			if cpt==6: 	Binary_fall(14)
			else: 		Binary_fall(21)			
			cpt-=1

		if cpt==7: 		cpt+=1 &  Binary_fall(20)
		if cpt==8: 		cpt+=2 &  Binary_fall(15)
		if cpt==9: 		cpt+=3 &  Binary_fall(10)
		if cpt==10: 	cpt+=4 &  Binary_fall(5)
	pass
	





def transcendant_fall(a,b,c):
	cpt=mod(a+b+c,5)+1		# initiate at 000 & 111
	print(cpt) 				# show value before modification)
	if cpt==4: cpt-=1		# readjustment if 100 & 011
	#########################
	if a+b+c>=3:			# limit
		#3='phi' 2='pi'
		cpt=-1
		if a==0: 	transcendant_fall(3*a,b,c) 
		if b==1: 	transcendant_fall(a,2*b,c) 
		if c==1: 	transcendant_fall(a,b,2*c) 
		cpt-=2
		if a==1:  	transcendant_fall(2*a,b,c) 
		if b==0: 	transcendant_fall(a,3*b,c) 
		if c==1: 	transcendant_fall(a,b,2*c) 	 
		cpt-=3
		if a==1:  	transcendant_fall(2*a,b,c) 	
		if b==1:  	transcendant_fall(a,2*b,c) 	
		if c==0:  	transcendant_fall(a,b,3*c) 	
		cpt-=4
		if a==1:  	transcendant_fall(3*a,b,c) 	
		if b==0:  	transcendant_fall(a,2*b,c) 	
		if c==1:  	transcendant_fall(a,b,2*c)
	pass
	return a,b,c,cpt
	
			


# Stable operator of fall
def Operator_fall(n):
#  Fall of numbers
## Fall of 2
	# declaration of variable cpt
	Binary_fall(n)
## Fall of 3	
	# declaration of variable 'y' & a,b,c
	# disappearance of a,b,c

	Ternary_fall()
	print(n, cpt)
	#last round 2 digit vs 1
	#	cpt 21 vs 6 
	r=mod(cpt,0)				# r=2
	# basis equation		   {0} radius	
	f=mod(cpt,1)   				# f=1	
	# basis equation		   {1} factor
	p1=cpt/(r*f)				#3	# d distance 
	p2=cpt/(r+f) 				#2
	p0=1
	c=cpt-p0 #5
	#(c+p0)(c-p2)	(5+1)(5-2) = 6 * 3
	#(c+p2)(c-p2) 	(5+2)(5-2) = 7 * 3
	print(c, c+p0, c-p2, c+p2 )
	# disappearance of variable 'n' no parity after this line
	return c, c+p0, c-p2, c+p2 




# definition of fraction by level
def Operator_Phi(n): 
	if n==1: 	Operator_Phi(0)
	if n==2: 	Operator_Phi(3)
	if n==6: 	Operator_Phi(2)
	if n==4: 	Operator_Phi(3)
	if n==3: 	Operator_Phi(4)
	if n==5: 	Operator_Lambda(3)	
	print("Incorrect input.") 
#

def Operator_Pi(n): 					 		
	if Operator_Phi(n==3):		Operator_Pi(n)									
	if Operator_Phi(n==3):		Operator_fall(5)
	if Operator_Phi(n==4):		Operator_fall(4)
	print("Incorrect input !") 

#
def Operator_Lambda(n): 
	if Operator_Phi(n)==1: 		Operator_Lambda(n) 		
	if Operator_fall(n)==3:		Operator_fall(n)
	if Operator_fall(n)==4: 	Operator_Phi(n)
	if Operator_fall(n)==3:		Operator_Pi(n)
	if Operator_fall(n)==16: 	Operator_Phi(n)
	if Operator_fall(n)==25:   	Operator_Pi(n)
	print("Incorrect input ?") 		
	n=n*phi 
	Operator_Lambda(n)

#def Op_Pythagoras(a,b,c):
#	r=Operator_Pi(a,b,c) 	print(r 		q=Operator_Phi(R)		print(q)
#	Q=Operator_Phi(q)  		print(Q 		R=Operator_Phi(a,b,c) 	print(R)
#	S=Operator_Phi(R)		print(S 		T=Operator_fall(a,b,c)  print(T)
#	x=Operator_Phi(r,s,t)   print(x 		return x)
	
#Op_Pythagoras(1,1,1)
#Op_Pythagoras(1,1,2)





def main():
  fire.Fire(name='fall')

if __name__ == '__main__':
  main()