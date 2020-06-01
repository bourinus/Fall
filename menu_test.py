from fire import testutils
import fall
import menu

class MenuTest(testutils.BaseTestCase):

  def test_hello(self):
    print("hello: test", self)

	#python hello.py  # Hello World!
    print("	python hello.py  # Hello World!")
    self.assertEqual(menu.hello(''), 'Hello !')
    
	#python hello.py --name=David  # Hello David!
    print("	python hello.py --name=David  # Hello David!")    
    self.assertEqual(menu.hello('name'), 'Hello name!')
	
	#python hello.py --help  # Shows usage information.
    print("	python hello.py --help  # Shows usage information.")    
    self.assertEqual(menu.hello('help'), 'Hello help!')


  


if __name__ == '__main__':
  testutils.main()