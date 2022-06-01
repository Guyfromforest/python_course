def find_exp():
 try:
     from oops_1 import oops
     oops()
 except IndexError as  e:
     print("I did that")

find_exp()

