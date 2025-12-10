class Person:
    def __init__(self,name):
        self.name=name
    def greeting(self):
        print("hello",self.name)

p1=Person("ali")
p1.greeting()

