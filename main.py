import fire
import fall

def hello(name="World"):
  return "Hello %s!" % name


def main():
  fire.Fire(hello)
  fire.Fire(fall)
  


if __name__ == '__main__':
  main()