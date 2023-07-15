# # Example 3: Guess the secret number
# secret_number = 5
# while True:
#     guess = int(input("Guess the number (number is an integer between 0 - 15): "))
#     if guess == secret_number:
#         print("Congratulations, you have guesses the right number")
#         break
#     else:
#         print("Sorry, wrong guess. Try it again")

def factorial(n):
    result = 1
    num = 1
    while num <= n:
        result *= num
        num += 1
    return result

n = 7
result = factorial(n)
print(f'Factorial of {n} is: {result}')