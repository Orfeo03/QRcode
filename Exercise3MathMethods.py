import math

#Exercise number 3

#Find the hypotenuse of a right triangle
# The formula is

a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))

c = math.sqrt(pow(a,2)+ pow(b,2))

print(f"The hypotenuse of the triangle is: {round(c,2)} cm")