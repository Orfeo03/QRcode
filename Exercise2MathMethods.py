import math

#Exercise number 2 MathMethods

#Calculate the area of a circle

radius=float(input("Enter the radius of the circle:"))

area = math.pi * pow(radius,2)

print(f"The area of the circle is: {round(area,2)} cm²")