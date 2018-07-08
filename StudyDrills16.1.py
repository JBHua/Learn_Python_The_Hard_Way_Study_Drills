#LPTHW Study Drill from Ex16

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C.")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")

target = open(filename, 'w')

print("Truncating the file. Goodbye!")

#According to the documentation for open function,
#if you open the file with "w", you do not need an extra "truncate()"
#because python will truncate it if the file already exists.
#So we don't need line 23
#target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

#The key of this drill is the "Formatting Strings".
#As you can see, I use "%s"to insert the sting to achieve the goal.
#I also use the escape character "\n" to change lines.

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

#Code from line 40-45 is the original code in the book.
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("And finally, we close it.")
target.close()