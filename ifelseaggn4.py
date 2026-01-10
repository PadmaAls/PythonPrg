# Given score print pass or fail

def pass_or_fail(mark1, mark2, mark3, mark4, mark5):
    if mark1 >= 36 and mark2 >= 36 and mark3 >=36 and mark4 >=36 and mark5>= 36:
       print ("All Pass")
    else:
        print ("Failed")

mark1 = 70
mark2 = 43
mark3 = 36
mark4 = 45
mark5 = 40

pass_or_fail(mark1, mark2, mark3, mark4, mark5)

#Given a number print whether positive, negative or zero

def pos_neg_zer(num):
    if num > 0:
       print ("The number is positive")
    else:
        if num < 0:
           print ("The number is negtaive")
        else:
            if num == 0:
               print ("The number is Zero")


num = int(input("Enter the num value : "))
pos_neg_zer(num)


#Given room temperature print it is hot, normal or cold --- 21 to 24 - Normal,Above 24 - Hot, Below 21 - Cold

def check_temp(temp):
    if temp < 21:
       print ("The temp is COLD")
    else:
        if temp >= 21 and temp <= 24:
            print ("The temp is NORMAL")
        else:
            if temp > 24:
               print ("The temp is HOT")

temp = int(input("Enter the temp value : "))
check_temp(temp)