#Task_!
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
print(assert_m.filter_leaps(b))