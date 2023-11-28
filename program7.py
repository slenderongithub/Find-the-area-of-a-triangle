#WAP to find the area of any triangle 

import math

A=int(input("Enter side A: "))
B=int(input("Enter side B: "))
C=int(input("Enter side C: "))

s=(A+B+C)/2
ar=s*(s-A)*(s-B)*(s-C)
Area=math.sqrt(ar)

print("The area of the triangle is", Area)