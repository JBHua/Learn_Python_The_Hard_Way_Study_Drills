#LPTHW Study Drill from Ex21
#StudyDrills4: Write a simple formula and use the functions in the same way to calculate it.

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("StudyDrills 4")

cars = add(32, 336)
bikes = subtract(5427, 123)
planes = multiply(313, 58)
boats = divide(500,2)

vehicle = add(boats, subtract(planes, multiply(bikes, divide(cars, 4))))

print("Ok, We have", vehicle, "vehicles")