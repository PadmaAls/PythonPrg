


phone_book = [
    ("Test1","123-456-7890","test1@gmail.com"),
    ("Test2","223-456-7890","test2@gmail.com"),
    ("Test3","323-456-7890","test3@gmail.com"),
    ("Test4","423-456-7890","test4@gmail.com"),
    ("Test5","523-456-7890","test5@gmail.com")
    ]


phone_book_dict = {}


for users in phone_book:
    name,phno,email = users
    phone_book_dict.update({name: users})
    
print(phone_book_dict)
print("*******************************")
print("Find a user in the dictionary")
search_user = phone_book_dict.get("Test2")
search_user1 = phone_book_dict.get(name)
print(search_user)
print(search_user1)


print("*******************************")
print("Delete a user in the dictionary")

remove_item = phone_book_dict.pop("Test3")
print(remove_item)
print("*******************************")
print("Dictionary after Delete")
print(phone_book_dict)




