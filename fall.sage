import *.*
def define(b):
	while True:
		print("base: b1=",b)     # CLASS PRINT
		print("############")
		try:
			print("base: b3=",b^2) 
			break
		except ValueError:
			print("Oops!  i^2=-1.  Try again...")
			print("base: b=",b^3)
			break



def xor(n):
	cpt=floor(ln(n)/ln(10))+1
	print(cpt)

	if n<=0: xor(100-1/n^2)
