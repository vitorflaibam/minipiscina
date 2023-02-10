class Intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.name = name

    def __str__(self):
        return self.name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."
            
    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee()


if __name__ == '__main__':
    intern = Intern()        
    intern1 = Intern("Mark")
    print(intern)
    print("Come on, you must have a name!")
    print("My name is ", intern1)
    print("Can you make coffee for me, Mark?")
    print(intern1.make_coffee())
    try:
        print("It doesn't matter, just make it!")
        intern.work()
    except Exception as e:
        print(e)