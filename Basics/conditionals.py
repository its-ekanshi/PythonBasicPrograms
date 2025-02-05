# To check number is positive or negative or zero
num = int(input("enter the number you want: "))
if num > 0:
    print("num is positive")
elif num < 0:
    print("num is negative")
else:
    print("num is zero")

# To check number is divisible by 2 or not
num = int(input("enter the number you want: "))
if num % 2 == 0:
    print("num is even")
else:
    print("num is odd")

# To check the year is leap year or not
year = int(input("Enter the year you want: "))
if (year % 100 == 0) and (year % 400 == 0):
    print("Leap Year")
elif (year % 4 == 0) and (year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# To find the largest between three numbers
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
num3 = int(input("enter the third number: "))
if num1 > num2 and num1 > num3:
    print("num1 is largest")
elif num2 > num1 and num2 > num3:
    print("num2 is largest")
else:
    print("num3 is largest")