first = int(input("Enter the first number:\n"))
second = int(input("Enter the second number:\n"))
res = first * second

print(f"{first} x {second} = {res}")

if res > 0:
    print("The result is positive.")
elif res < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
