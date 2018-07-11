#LPTHW Study Drill from Ex29

people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cat! The world is doomed!")

if people > cats:
    print("Not many cat! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

#Let's use some combination

if (people+dogs) > cats:
    print("Dogs are the best!")

if (cats >= people) and (dogs >= people):
    print("Oh no, there are so many animals")

if (people > cats) or (people > dogs):
    print("That' good.")