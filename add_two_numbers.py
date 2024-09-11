def add_two_numbers(a, b):
    return a + b

while True:
 try:
     a = float(input("Enter the first number: "))
     b = float(input("Enter the second number: "))
     break
 except ValueError:
     print("Please enter valid numbers.")

print(add_two_numbers(a, b))

