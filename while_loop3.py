print ("Sum of natural numbers until a given number 4-> 1+2+3+4 = 10")
def sum_of_nums(limit):
    num = 1
    sum = 0
    while (num <= limit):
        sum = num + sum
        num = num + 1
    print(sum)

sum_of_nums(4)

print ("---------------------------------------------------------")
print ("Print factorial of a given number 5-> 5*4*3*2*1 = 120")

def fact_of_nums(limit):
    num = 1
    fact_val = 1
    while (num <= limit):
        fact_val = num * fact_val
        num = num + 1
    print(fact_val)

fact_of_nums(5)