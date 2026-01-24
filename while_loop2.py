print("------------------------------------------------------------")

#print all numbers divisible by 3

print ("All numbers divisible by 3 until a given number")

def div_by_three(limit):
    num = 1
    while num <= limit:
        if (num % 3) == 0:
           print(num)
        num = num + 1
        
div_by_three(10)

print("---------------------------------------------------------------------")

print("All numbers divisible by 3 and 5 until a given number")


def div_by_both(limit):
    num = 1
    while num <= limit:
        if (num % 3) == 0 and (num % 5) == 0:
           print(num)
        num = num + 1

div_by_both(50)