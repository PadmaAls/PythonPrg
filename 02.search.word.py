def search_position(source_data, search_term):
    
    index = source_data.find(search_term)
    return index


# ----------------------------------------------#
#      Do not modify the test code below        #
# ----------------------------------------------#


def validate(expected, actual):
    assert actual == expected, f"Search -> expected {expected} got {actual}"


result = search_position("Learning Python is fun", "fun")
validate(expected=19, actual=result)

result = search_position("So many books, so little time", "books")
validate(expected=8, actual=result)

result = search_position("Be the change that you wish to see in the world", "fun")
validate(expected=-1, actual=result)