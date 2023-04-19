#A program to demonstrate how to use a class and an object

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def bark(self):
        print("Wolf")
        
fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()