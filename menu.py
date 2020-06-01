import fall
import fire

class Menu(object):
  """docstring for ClassName"""
  def __init__(self, arg):
    self.arg = arg
    

def hello(name="World"):
  return "Hello %s!" % name

def menu(name="Menu"):
  c = input("Menu. Enter a choice: ")
  if c==0: hello(c)
  if c==1: help(c)
  if c==2: Q(c)
  if c==3: R(c)
  
def callFall():
  b = input("chitchat ?, Enter a string: ")
  Fall_Object = Fall(self)
  Fall_Object.define(b)





def Q(name='q'):
  q = input("Question ?, Enter a number: ")
  fire.Fire(R(q))
  fire.Fire(hello)	

def R(name='r'):
  r=fall.define(fall.define(r))
  print("Results ! here it is:",r)
  fire.Fire(menu)
  fire.Fire(Q(r))
  fire.Fire(hello)	


def chitchat():
  print("hey !")
  b = input("chitchat ?, Enter a string: ")
  if b=='': chitchat()
  if isinstance(b, str): return 'none'
  if isinstance(b, str)!=0: fire.Fire(Q(q))	
  fire.Fire(hello)	



  
def main():
  fire.Fire(name='menu')

if __name__ == '__main__':
  main()
