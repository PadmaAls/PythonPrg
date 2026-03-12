# # Phone Book
#     - add name, number, email
#     - add entry
#     - delete entry
#     - search for a name
#     - print all entries

phone_book = [{"name": "John", "phone": "98438345"}]

# hash
john = {"name": "John", "age": 30, "graduate": True, 1: "XYZ"}

# set
john["name"] = "John S"
john.update({"name": "John S", "age": 31, "qualification": "graduate", "last": "abc"})

# get
name = john.get("name")
name = john["name"]

x = john.pop("name")
print(x)

# del john["name"]

# x = john.popitem()
# print(x)

# value = john[1]
print(john)

# print(dir(john))

# Big O - O(1)


def add(datadict, key, value):
    datadict.update({key: value})


add(john, "name", "John S")
add(john, "name", "John Sen")

print(john)