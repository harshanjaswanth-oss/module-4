try:
    age = int(input("Enter your age: "))
    if 0 < age < 150:
        print("Your age is recorded as:", age)
    else:
        print("Age must be between 1 and 149.")
except ValueError:
    print("Invalid input. Please enter a whole number.")