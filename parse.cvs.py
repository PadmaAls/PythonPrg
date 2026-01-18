# "John,30,2026" -> "John,31,2027"


def csv_incr_year_and_age(input_data):
    Name, Age, Year = input_data.split(",")
    Age = int(Age) + 1
    Year = int(Year) + 1
    Age = str(Age)
    Year = str(Year)
    incr_data = Name+","+ Age+","+Year
    print(incr_data)
    return incr_data



# ----------------------------------------------#
#      Do not modify the test code below        #
# ----------------------------------------------#


def validate(expected, actual):
    assert actual == expected, f"Search -> expected {expected} got {actual}"


result = csv_incr_year_and_age("John,20,2026")
validate(expected="John,21,2027", actual=result)

result = csv_incr_year_and_age("Sam,12,2018")
validate(expected="Sam,13,2019", actual=result)

result = csv_incr_year_and_age("Dave,32,1950")
validate(expected="Dave,33,1951", actual=result)