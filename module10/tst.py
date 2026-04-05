class Animal: pass
class Dog(Animal): pass
class Cat(Animal): pass

@singledispatch
def speak(animal):
    print("Unknown sound")

@speak.register(Dog)
def _(dog):
    print("Haw!")

@speak.register(Cat)
def _(cat):
    print("Meow!")

speak(Dog())  # Woof!
speak(Cat())  # Meow!
speak(Animal())  # Unknown sound