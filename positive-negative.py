# Complete the following function(s)
# Given numbers, categorize as follows
# Above 0 -> Positive
# Below 0 -> Negative
# 0 -> Zero


def categorize(age):
    pass
    if age == 0:
       return "Zero"
    elif age > 0:
        return "Positive"
    elif age < 0:
        return "Negative"


# ----------------------------------------------#
#      Do not modify the test code below        #
# ----------------------------------------------#


def validate(expected, actual):
    assert actual == expected, f"Number -> expected {expected} got {actual}"


result = categorize(0)
validate(expected="Zero", actual=result)

result = categorize(14)
validate(expected="Positive", actual=result)

result = categorize(-8)
validate(expected="Negative", actual=result)