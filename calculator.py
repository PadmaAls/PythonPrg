# Complete the following function(s)
# Add, Sub, Mul, Div, Pow, Floor Div (fdiv), Mod


def calculate(op, x, y):

    if op == "add":
        return x + y
    elif op == "sub":
        return x - y
    elif op == "div":
        return x / y
    elif op == "mul":
        return x * y
    elif op == "pow":
        return x ** y
    elif op == "fdiv":
        return x // y
    elif op == "mod":
        return x % y

    


# ----------------------------------------------#
#      Do not modify the test code below        #
# ----------------------------------------------#


x = 10
y = 3


def validate(op, expected, actual):
    assert actual == expected, f"{op} -> expected {expected} got {actual}"


result = calculate("add", x, y)
validate("add", expected=13, actual=result)

result = calculate("sub", x, y)
validate("sub", expected=7, actual=result)

result = calculate("div", x, y)
validate("div", expected=3.3333333333333335, actual=result)

result = calculate("mul", x, y)
validate("mul", expected=30, actual=result)

result = calculate("pow", x, y)
validate("pow", expected=1000, actual=result)

result = calculate("fdiv", x, y)
validate("fdiv", expected=3, actual=result)

result = calculate("mod", x, y)
validate("mod", expected=1, actual=result)