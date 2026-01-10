# Given a number if odd double it(2x) , if even return the same 3 > 6, 4 > 4

def double_or_not(number):
    if number % 2 == 0:
        print ("The number is : ",number)
    else:
        print ("The number is : ",number*2)

number = int(input("Enter the number :"))
double_or_not(number)

#Given 2 number find min, find max

def min_or_max(num1, num2):
    if num1 < num2:
       print ("Num1 is minimum & Num2 is maximum")
    else:
       print ("Num2 is minimum & Num1 is maximum")
    
num1 = int(input("Enter Num1 value :"))
num2 = int(input("Enter Num2 value :"))
min_or_max(num1, num2)
    