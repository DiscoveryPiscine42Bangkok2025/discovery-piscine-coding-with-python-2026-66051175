i = int(input("Enter a number less than 25\n"))

if i >= 25:
    print("Error")
for i in range(i, 26):
    print("Inside the loop, my variable is", i)

# Enter a number less than 25
# 45
# Error
# ?> ./to25.py
# Enter a number less than 25
# 20
# Inside the loop, my variable is 20
# Inside the loop, my variable is 21
# Inside the loop, my variable is 22
# Inside the loop, my variable is 23
# Inside the loop, my variable is 24
# Inside the loop, my variable is 25