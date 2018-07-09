#LPTHW Study Drill from Ex20
from sys import argv

script, input_file = argv

#Define the first function to print all content in a file.
def print_all(f):
    print(f.read())

#Define the second function to "move" to a specific position, in this case
#we moved to the beginning of the file.(because the parameter is 0)
def rewind(f):
    f.seek(0)

#Define the last function to print the specific line of the file.
#The "line_count" means the line python is reading.
def print_a_line(line_count, f):
    print(line_count, f.readline())

#Denoting that the current_file is the "input file"
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

#Giving the variable current_line a value of 1
current_line = 1
print_a_line(current_line, current_file)

#"+=" means add a number to the variable.
#Actually, it add the right-side number(or variable) to the left-side number(or variable).
#"a = a + b" is equal to "a +=b"
#It has the same meaning in cpp11.
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)