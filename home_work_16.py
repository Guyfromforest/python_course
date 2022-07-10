#Task_1
class Person:
    def __init__(self, name, surname, age, hobby, religion, gender):
        self.religion = religion
        self.hobby = hobby
        self.age = age
        self.surname = surname
        self.name = name



class Student(Person):
    def __init__(self, graduet_program, everage_score, attending, optional_clasees, course, subjects, discount_for_study ):
        self.discount_for_study = bool(discount_for_study)
        self.subjects = []
        self.course = int(course)
        self.optional_clasees = bool(optional_clasees)
        self.attending = int(attending)
        self.everage_score = everage_score
        self.graduet_program = graduet_program


class Teacher(Person):
    def __init__(self, scientific_degree, years_of_experience, sci, subject,alma_mater):
        super().__init__(self, name, surname, age, hobby, religion)
        self.alma_mater = alma_mater
        self.subject = subject
        self.sci = int(sci)
        self.years_of_experience = int(years_of_experience)
        self.scientific_degree = scientific_degree

#
# Task2
import random
a = [random.randint(-20, 30) for i in range(10)]
b = [1985, 1985, 1992, 1778, 2010, 2010, 2019]
class Mathematical:
    pass
    def square_nums(self, lst: list):
        return [i**2 for i in lst]
    def remove_positives(self, lst: list):
        return [i for i in lst if i < 0]
    def filter_leaps(self, date: list):
        return sorted(list(set((date))))

assert_m = Mathematical()
print(assert_m.square_nums(a))
print(assert_m.remove_positives(a))
pдlrint(assert_m.filter_leaps(b))

#Task 3 Не розумію як прив'язати методи класи ProductStore до об'єкту класу Product хоча я його заносив і в список і в dict, але я не зупиняюсь

class Product:
    def __init__(self, type, name, price, amount):
        self.type = type
        self.name = name
        self.price = price
        self.amount = amount

class ProductStore:
    def __init__(self):
        self.id = 0
        self.store = []


    def add(self,product1:Product, amonunt:int):
        self.store.append(product1)
        for i in self.store:
            product1.price= product1.price*1.3
            product1.amount += amonunt
            self.id =+1
        print(self.store)
    def set_discount(self, indetifier, percent: int, indetifier_type:str):
        if indetifier_type == "name":
            for product in self.store:
                if indetifier == product.name:
                    product.price -= product.price*(percent/100)
        elif indetifier_type == "type":
            for product in self.store:
                if indetifier == product,type:
                    product.price -= product.price*(percent/100)
    def sell_product(self, product_name:str, amount):



p1 = Product('Sport', 'Football T-Shirt', 100)
b1 =ProductStore()
b1.add(p1,25)
print(b1)


#Task4 Create your custom exception named `CustomException`, you can inherit from base Exception class, but extend its functionality to log every error message to a file named `logs.txt`. Tips: Use __init__ method to extend functionality for saving messages to file
я створив клас,але не зрозумів як обгорнути його для логування,у мене була спроба,але воно не записувалося у смс
class CustomException(Exception):
    def __init__(self, msg):
        if msg:
            self.message = msg
        else:
            self.message=None

    def __str__(self):
        if self.message:
            return "CustomError".format(self.message)
        else:
            return "MyCustomError has been raised"



raise CustomException("We have a problem")












