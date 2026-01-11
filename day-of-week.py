# Complete the following function(s)
# Convert numbers into day of week, 1 -> Monday, 2 -> Tuesday ... 7 -> Sunday


def get_week_day(num):

    if num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif num == 4:
        return "Thursday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"
    elif num == 7:
        return "Sunday"
    else:
        return "Invalid Input"


# ----------------------------------------------#
#      Do not modify the test code below        #
# ----------------------------------------------#


def validate(expected, actual):
    assert actual == expected, f"Day -> expected {expected} got {actual}"


result = get_week_day(1)
validate(expected="Monday", actual=result)

result = get_week_day(2)
validate(expected="Tuesday", actual=result)

result = get_week_day(3)
validate(expected="Wednesday", actual=result)

result = get_week_day(4)
validate(expected="Thursday", actual=result)

result = get_week_day(5)
validate(expected="Friday", actual=result)

result = get_week_day(6)
validate(expected="Saturday", actual=result)

result = get_week_day(7)
validate(expected="Sunday", actual=result)

result = get_week_day(10)
validate(expected="Invalid Input", actual=result)