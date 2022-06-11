#Write a Python program to detect the number of local variables declared in a function.
# from math import pi
# def devide ():
#     a = [1, 2, 3, 4, 5, 6]
#     return b/pi
# print(devide.__code__.co_nlocals)

# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

# def make_divide(x):
#     def divide(a):
#         return x/a
#     return divide
# div_3 = make_divide(3)
# print(div_3(4))
#     #
# # Task3
# def choose_func(nums: list, func1, func2):
#     for i in nums:
#         if i >0:
#             return func2
#         else:
#             return func1
#
# def list_check(nums):
#     return [i**2 for i in nums if i >= 0]
# def list_check2(nums):
#     return [i**2 for i in nums if i >= 0]
#
# a = [1,2,3,4,5,8,-6]
# b = [2,3,-4,2,5,6,1111111111111111110,0.2]
# def choose_func(nums: list, func1, func2):
#     for i in nums:
#         if i >0:
#             return func2
#         else:
#             return func1
#
# def list_check(nums):
#     return [i**2 for i in nums]
# def list_check2(nums):
#     return [i**2 for i in nums if i>0]
#
# a = [1,2,3,4,5,8,-6]
# b = [2,3,-4,2,5,6,0]
# print(choose_func(a, list_check(a), list_check2(a)))
# print(choose_func(b, list_check(b), list_check2(b)))









