# Complete the following function(s)
# Given a number return following
# number divisible by 3 -> "fizz"
# number divisible by 5 -> "buzz"
# number divisible by both 3 and 5 -> "fizzbuzz"


def fizzBuzz(number):
    if number % 3 == 0 and number % 5 == 0:
       return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"


# ----------------------------------------------#
#      Do not modify the test code below        #
# ----------------------------------------------#


def validate(expected, actual):
    assert actual == expected, f"FizzBuzz -> expected {expected} got {actual}"


result = fizzBuzz(9)
validate(expected="fizz", actual=result)

result = fizzBuzz(10)
validate(expected="buzz", actual=result)

result = fizzBuzz(15)
validate(expected="fizzbuzz", actual=result)