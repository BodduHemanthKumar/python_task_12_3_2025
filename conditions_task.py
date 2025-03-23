#1. Write a Python program that takes an integer as input and prints whether it is even or odd.

number = int(input("please enter an number : "))
if number%2==0:
    print(number," is even number. ")
else:
    print(number," is odd number.")


#2. write a program taht takes two numbers as input and prints the larger number. If they are equal, print "both numbers are equal"."

number1= int(input("please enter first number: "))
number2= int(input("please enter second number: "))
if number1>number2:
    print(number1," is greater than ",number2)
elif number2>number1:
    print(number2," is greater than ",number1)
else:
    print("both number are equal")


#3. write a Python program that asks the user for a number and prints whether it is positive, negative, or zero.

number = int(input("please enter a number : "))
if number>0:
    print(number," is positive number.")
elif number<0:
    print(number," is negative number")
else:
    print(number," is zero")


#4. write a program that asks the user for their age. If the age is 18 or above, Print "you are eligible to Vote", otherwise print "you are 
# not eligible to vote".

age = int(input("please enter your age : "))
if age==18 or age >18:
    print("You are eligible to Vote.")
else:
    print("You are not eligible to Vote")


#5. write a program that takes a student's marks (out of 100) and print:"pass" if the marks are 40 and more, "fail" if marks are less than 40.

marks = int(input("please enter your marks out of 100 : "))
if marks<=100 and marks>=40:
    print("You are Pass.")
elif marks>100:
    print("please enter your marks out of 100.")
else:
    print("You are Fail.")