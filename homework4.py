#Task1 tring manipulation

# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.
#
# Sample String: 'helloworld'
#
# Expected Result : 'held'
#
# Sample String: 'my'
#
# Expected Result : 'mymy'
#
# Sample String: ' x'
#
# Expected Result: Empty String
#
# Tips:
#
#     Use built-in function len() on an input string
#     Use positive indexing to get the first characters of a string and negative indexing to get the last characters
# a = "Junkyfood"
# b = 0
# for i in a:
#     b = b+1
# d = a[0:2]+a[-2:b]
# print(d)
#2nd part
# word1="itq"
# if len(word1) <= 2:
#     print(word1*2)
# else:
#     print("More than2")
#3th part
# word2="i"
# if len(word2) > 2:
#     print(word2*2)
# else:
#   print("Empty string")

#Make a program that checks if a string is in the right format for a phone number.\
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation
#number = input("Give me your number, please:\n")
# if number.isdigit() and len(number) == 10:
#     print("Thank for you number, have a good day")
# else:
#     print("Please, check you phone, it must be 10 numbers")

#The name check.

#Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
# The program should check if your input is equal to the stored name even if the given name has another case, e.g., i
# f your input is “Anton” and the stored name is “anton”, it should return True.
namehause=["Oleksii Borodin", "Gregory Skovoroda"]
name = input("What is you full name?\n")
if name in namehause:
    print(name)
else:
    print("You aren't my friend")

