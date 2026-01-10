def vote_eligib(age):
    can_vote = age > 18
    print("Eligible to Vote : ", can_vote)
        
age = 20    
vote_eligib(age)

age = 13
vote_eligib(age)

print("******************************************************")

def drive_eligib(age):
    can_drive = age > 18
    print("Eligible to Drive :",can_drive)

age = 20
drive_eligib(age)

age = 15
drive_eligib(age)

print("******************************************************")

def pass_or_fail(marks):
    p_or_f = marks >= 35
    print("Passed : ?", p_or_f)
    print("Failed ?",not p_or_f)

marks = 45
pass_or_fail(marks)

print("******************************************************")

def fail_or_pass(marks):
    f_or_p =  marks < 34
    print("Failed : ?", f_or_p)
    print("Passed : ?", not f_or_p)

marks = 20
fail_or_pass(marks)
print("******************************************************")


def centum(marks):
    is_cent = marks == 100
    print ("Is Centum ? : ", is_cent)

marks = 100
centum(marks)


print("******************************************************")

marks = 45
centum(marks)

print("******************************************************")


def fever_check(temp):
    has_fever = temp >= 100
    print ("Has Fever ? : ", has_fever)

temp = 100
fever_check(temp)

print("******************************************************")

temp = 97
fever_check(temp)

temp = int(input("Enter the temp : "))
fever_check(temp)

print("******************************************************")

def check_user_pwd(user,pwd):
    user_match = user == "admin"
    pwd_match = pwd == 1234
    user_pwd_match = user_match and pwd_match
    print ("User Name and Password Matched ?: ", user_pwd_match)

user = input("Enter the user name :")
pwd = int(input("Enter the pwd :"))
check_user_pwd(user,pwd)

print("******************************************************")

def pos_neg(num):
    pos = num > 0
    print ("The number is positive : ", pos)
    neg =  num < 0
    print ("The number is negative : ", neg)
    zero = num == 0
    print("The number is zero : ", zero)
    even = num % 2 == 0
    print("The number is even : ", even)
    print("The number is odd : ", not even)


num = int(input("Enter the num value  :"))
pos_neg(num)


    