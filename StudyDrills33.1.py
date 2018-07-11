#LPTHW Study Drill from Ex33

def while_loop(start_value, end_value, increase):
    i = start_value
    numbers = []
    while i < end_value:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print("Numbers now: ",numbers)
        print(f"At the bottom i is {i}")

while_loop(0,20,2)