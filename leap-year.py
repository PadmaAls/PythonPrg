# Complete the following function(s)
# Given an year, return True if it is a leap year, False otherwise


def is_leap_year(year):
    pass
    if year % 4 == 0:
       return True
    else:
       return False
    
    

# ----------------------------------------------#
#      Do not modify the test code below        #
# ----------------------------------------------#


def validate(expected, actual):
    assert actual == expected, f"Leap Year -> expected {expected} got {actual}"


result = is_leap_year(2016)
validate(expected=True, actual=result)

result = is_leap_year(2020)
validate(expected=True, actual=result)

result = is_leap_year(2026)
validate(expected=False, actual=result)