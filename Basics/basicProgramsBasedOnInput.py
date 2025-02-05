# To find sum of two numbers
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
sum = num1 + num2
print("sum of num1 and num2 is:",sum)

# :To find square root
num = int(input("enter the number you want: "))
sr = num ** 0.5
print(sr)

# 2nd method To find Square Root--
import math
num = int(input("enter the number you want: "))
sr = math.sqrt(num)
print(sr)

# To swap the variables
num1 = int(input("enter first variable:"))
num2 = int(input("enter second variable:"))
temp = num1
num1 = num2
num2 = temp
print("first variable: ",num1)
print("second variable: ",num2)

# To convert kilometers into miles
kilometers = float(input("enter value in kilometer: "))
miles = kilometers * 0.621371
print("Now value in miles: ", miles)