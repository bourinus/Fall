import fire


def main():
    return "hello"

def hello(name="World"):
    return "Hello %s!" % name
def launch():
    return "launch"

if __name__ == '__main__':
    fire.Fire(hello)
	fire.Fire(%s)

if __name__ == '__launch__':    
    fire.Fire(launch)
    fire.Fire("launch")

