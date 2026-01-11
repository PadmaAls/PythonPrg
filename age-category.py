# Complete the following function(s)
# Given age categorize as follows
# "Child" (0–12)
# "Teen" (13–19)
# "Adult" (20–64)
# "Senior" (65+)


def categorize(age):
    pass
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teen"
    elif age >= 20 and age <= 64:
        return "Adult"
    elif age >= 65:
        return "Senior"
    else:
        return "Invalid"


# ----------------------------------------------#
#      Do not modify the test code below        #
# ----------------------------------------------#


def validate(expected, actual):
    assert actual == expected, f"Age -> expected {expected} got {actual}"


result = categorize(8)
validate(expected="Child", actual=result)

result = categorize(14)
validate(expected="Teen", actual=result)

result = categorize(32)
validate(expected="Adult", actual=result)

result = categorize(68)
validate(expected="Senior", actual=result)

result = categorize(-1)
validate(expected="Invalid", actual=result)