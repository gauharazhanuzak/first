#1
import math

degree = float(input("Input degree: "))
radian = math.radians(degree)
print("Output radian:", radian)

#2
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = 0.5 * (base1 + base2) * height
print("Expected Output:", area)

#3
sides = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))

area = int((sides * length**2) / (4 * math.tan(math.pi / sides)))
print("The area of the polygon is:", area)

#4
length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = length * height
print("Expected Output:", area)