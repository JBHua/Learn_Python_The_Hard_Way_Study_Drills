#LPTHW Study Drill from Ex21

#Define and assign value to three different variables.
people = 40
cars = 40
trucks = 20

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

if people > trucks  and people > cars:
    print("Ok, there are too many people, let's go home")
elif people < trucks and people < cars:
    print("That's good! There are plenty of cars and trucks,so we can take both of them.")
else:
    print("We still cannot decide.")