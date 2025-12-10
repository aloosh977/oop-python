class Animal:
    def sound(self):
        pass
    
class Dog(Animal):
    def sound(self):
        return "woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

dog=Dog()
print(dog.sound())
cat=Cat()
print(cat.sound())