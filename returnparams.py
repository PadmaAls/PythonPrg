def sum(a,b):
    c = a + b
    print ("Sum value : ", c)
    print("------------------")

sum(10,20)


def multiply(a, b):
    c = a * b
    print ("Multiply value inside func ", c)
    return c

d = multiply(10,20)
print ("Multiply value outside fn", d)
print("------------------------------")

def subt(a,b):
    c = a - b
    print("Subt value is :", c)
    return c

c = subt (40,20)
print("Print return value for subt after function :",c)
print("------------------------------")

def trudiv(a,b):
    c = a / b
    print ("True Div value inside fn :",c)
    return c

c = trudiv(30,4)
print("True div value outside function :", c)
print("------------------------------")

def floordiv(a,b):
    c = a // b
    print("Floor div value inside fn :", c)
    return c

c = floordiv(30,4)
print("Floor div value outside function :", c)
print("------------------------------")

def mod(a,b):
    c = a % b
    print ("MOd value inside function :", c)
    return c

c = mod(30,4)
print("Mod value outside function :", c)
print("------------------------------")