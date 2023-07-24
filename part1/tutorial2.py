## program to check if the number is positive, negative or 0
# number = int(input("Enter a number: "))
# if number > 0:
#     print("The number is positive")
# elif number < 0:
#     print("The number is negative")
# else:
#     print("The number is zero")

# # check if the number is even or odd
# if number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# # guess the secret number
# secret_number = 7
# guess = int(input("Guess the number (number is between 1-9): "))

# if guess == secret_number:
#     print("Congratulations, you have guessed the correct number")
# else:
#     print("Sorry, that's not the right number")

# - Exercise 1: Write a program that checks if a year is a leap year or not.
# - Exercise 2: Write a program that determines the type of a triangle based on its side lengths.
# - Exercise 3: Write a program that asks the user for their age and prints whether they are a child, teenager, or adult.

# Exercise 3
# age = int(input("Enter your age: "))

# if age < 13:
#     print("You are a child.")
# elif age < 20:
#     print("You are a teenager.")
# else:
#     print("You are an adult.")

# # - Exercise 2:
# side1 = float(input("Enter the length of side 1: "))
# side2 = float(input("Enter the length of side 2: "))
# side3 = float(input("Enter the length of side 3: "))

# if side1 == side2 == side3:
#     print("Equilateral triangle")
# elif side1 == side2 or side1 == side3 or side2 == side3:
#     print("Isosceles triangle")
# else:
#     print("Scalene triangle")

year = int(input("Enter a year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(year, "is a leap year.")
#         else:
#             print(year, "is not a leap year.")
#     else:
#         print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap year')
        else:
            print(f'{year} is not a leap year')
    else:
        print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

