#LPTHW Study Drill from Ex33

#Initially I want to let the user decide where to begin and where to end.
#But I meet a bug. If the user let the starting number be 0, the program will never stop running and go crazy.
#SO, I gave up on this.

end_number = int(input("Plz give the end number."))
increasement = int(input("Plz give the increasement."))

def while_loop(end_value, increase):
    i = 0 
    numbers = []
    while i < end_value:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increase
        print("Numbers now: ",numbers)
        print(f"At the bottom i is {i}")

    return numbers

numbers = while_loop(end_number, increasement)


print("The numbers: ")

for num in numbers:
    print(num)

