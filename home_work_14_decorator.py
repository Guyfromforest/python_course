# Task1
from functools import wraps
# def logger(func):
#     @wraps(func)
#     def wrap(*args):
#         print(f"The function name is:\t{func.__name__}")
#         result = func()
#         return result
#     return wrap
#
# @logger
# def add(n=2, n1=9):
#     return n + n1
# print(add())
# Task2 Remake
# def stop_word(words:list):
#         def stop_word_dec(func):
#             @wraps(func)
#             def wrap(*args, **kwargs):
#                 result = func(*args, **kwargs)
#                 for i in words:
#                     result = result.replace(i, "*")
#                 return result
#             return wrap
#         return stop_word_dec
# #
# #
# #
# #
# @stop_word(["BMW","pepsi"])
# def create_slogan(name):
#     return f"{name} drinks pepsi in his brand new BMW"
# #
# print(create_slogan("Mykola"))
# #Task 3


# #
# def arg_rules(type_:type,max_length:int, contains:list):
#     def arg_rules_dec(func):
#         @wraps(func)
#         def wrap(*args, **kwargs):
#             result = func(*args, **kwargs)
#             if type_ != type(args[0]):
#                 print(f"You can use only {type_}, you have used - {type(args[0])}")
#                 return False
#             if max_length <= len(args[0]):
#                 print(f"You must use less words, normal is {max_length}, you have used:{len(args[0])}")
#                 return False
#             for i in contains:
#                 if i not in (args[0]):
#                     print(f"You missed symbol - {contains} ")
#                     return False
#             return result
#         return wrap
#     return arg_rules_dec
#
#
# @arg_rules(str,15,["@","5"])
# def create_slogan(name:str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW"
#
# print(create_slogan("oleksii05@.com"))












