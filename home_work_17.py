#Task1
class Animal:
    def talk(self):
         raise NotImplementedError ("Animal cann't speak")

class Dog(Animal):
    def __init__(self, name, year, sound):
        self.year = year
        self.name = name
        self.sound = sound

    def talk(self):
        return (f"This dog has name:{self.name}. he has {self.year} years old and can say:{self.sound}")

class Cat(Animal):
    def __init__(self, name, year, sound):
        self.year = year
        self.name = name
        self.sound = sound

    def talk(self):
        return (f"Cat has name:{self.name}, he has {self.year} year oldand can say:{self.sound}")

a1= Animal()
b1 = Dog("Kant",12,"Wow")
c1 = Cat("Puh", 1,"Meow")
print(a1.talk())
print(c1.talk())
print(b1.talk())

#Task2 Я його декілька раз перероблював і виходив жах,то він у мен елише драфтом є.
# Write a class structure that implements a library. Classes
# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books=[]
#         self.authors=[]
#
#