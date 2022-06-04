# Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it. Then write another script that opens myfile.txt, and reads and prints its contents. Run your two scripts from the system command line.

# Does the new file show up in the directory where you ran your scripts?
#
# What if you add a different directory path to the filename passed to open?
#

# Note: file write methods do not add newline characters to your strings; add an explicit ‘\n’ at the end of the string if you want to fully terminate the line in the file.
#If file is in a same directory with function
# def new_file():
#     with open("Hello word.txt", "w") as f:
#         a = f.write("Hello file world")
#
# new_file()
#
# def print_file():
#     with open("Hello word.txt", "r") as f_1:
#         line_1 = f_1.read()
#         print(line_1)
#
# print_file()

#different directory
# def new_file():
#     with open("../../Game/Hello word.txt", "w") as f:
#         a = f.write("Hello file world")
#
# new_file()
#
# def print_file():
#     with open("../../Game/Hello word.txt", "r") as f_1:
#         line_1 = f_1.read()
#         print(line_1)

