#A Person class

# class Person:
#     def __init__(self, age, name):
#         self.name = name
#         self.age = age
#
#     def talk(self):
#         return (f"Hello, my name is,{self.name}, and  I'm {self.age} years old ")
#
#
# p1 = Person(89, "Emaneul Kant")
# print(p1.talk())


# Doggy age
# Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age. Then create a method `human_age` which returns the dog’s age in human equivalent.
# class Dog:
#     different = 7
#     def __init__(self,age):
#         self.age = age
#
#
#     def human_age(self):
#         return self.age*Dog.different
#
#
# Jack = Dog(8)
# print("The human age of Jack is", Jack.human_age(), "years old")
# def using():
#     def wrapper():

CHANNELS = ["BBC", "Discovery", "TV1000"]
class TVcontroller:
    def __init__(self, channels):
        self.channels = CHANNELS
        self.current_channele = None

    def first_channel(self):
        self.current_channele = 1
        for i in CHANNELS:
            return print(CHANNELS[0])
    def last_channel(self):
        self.current_channele = 3
        for i in CHANNELS:
            return print(CHANNELS[-1])
    def turn_chanel(self, n: str):
        self.current_channele = n
        if n in range(1, 4):
            if n == 1:
              print(CHANNELS[0])
            elif n == 2:
              print(CHANNELS[1])
            elif n == 3:
               print(CHANNELS[-1])
        else:
             print("Sorry, but we have only 3 channels")
    def next_channel(self):
        if self.current_channele == 1:
            self.current_channele = 2
            print(CHANNELS[1])
        elif self.current_channele == 2:
            self.current_channele = 3
            print(CHANNELS[2])
        elif self.current_channele == 3:
            self.current_channele = 1
            print(CHANNELS[0])
        else:
            print(CHANNELS[1])
    def previous_channel(self):
        if self.current_channele == 1:
            print(CHANNELS[2])
            self.current_channele = 3
        elif self.current_channele == 2:
            print(CHANNELS[0])
            self.current_channele = 1
        elif self.current_channele == 3:
            print(CHANNELS[1])
            self.current_channele = 2
        else:
            print(CHANNELS[0])
    def current_channel(self):
        if self.current_channele == 1:
            print(CHANNELS[0])
        elif self.current_channele == 2:
            print(CHANNELS[1])
        elif self.current_channele == 3:
            print(CHANNELS[-1])
        elif self.channels == None:
            print(CHANNELS[0])
    def is_exit(self,name):
        if name in range(1,3):
            print("Yes")
        elif name in self.channels:
             print("Yes")
        else:
            print("No")


controller = TVcontroller(CHANNELS)
controller.first_channel()
controller.last_channel()
controller.previous_channel()
controller.next_channel()
controller.turn_chanel(2)
controller.current_channel()
controller.is_exit("SADD")
controller.is_exit(9)
controller.is_exit("BBC")
controller.is_exit(2)

        
            

        

        
        











