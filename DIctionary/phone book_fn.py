

phone_book = [
    ("Test1","123-456-7890","test1@gmail.com"),
    ("Test2","223-456-7890","test2@gmail.com"),
    ("Test3","*323-456-7890","test3@gmail.com"),
    ("Test3","423-456-7890","test4@gmail.com"),
    ("Test2","(523-456-7890)","test5@gmail.com")
    ]

phone_book_dict = {}


def add_phone_book_dict(phone_book_dict,name,phonenum):
    for name_exists in phone_book_dict:
        if name_exists.upper() == name.upper():
            print("Duplicate Name skipped: ", name)
            return
    for ph in phonenum:
        #print(phonenum)
        if ph.isdigit() or ph == "(" or ph == ")" or ph == "-" or ph == "+":
            phone_book_dict.update({name : phonenum})
        else:
            print("Phone number is not having valid chars this entry skipped",phonenum)
            return
    print(f"{name:<10} | {phonenum:>14}")   

for name,phonenum,email in phone_book:
    add_phone_book_dict(phone_book_dict,name,phonenum)

#search by name pattern match
def search_pattern(pattern, dictname):
   result = {k: v for k, v in dictname.items() if pattern in k}
   return(result)

pattern = "Test1"
result = search_pattern(pattern,phone_book_dict)
print(result)


#search by exact key print the values
def search_by_exact_key(keyval, dictname):
    exact_value = dictname.get(keyval)
    return(exact_value)

keyval = "Test2"
exact_value = search_by_exact_key(keyval,phone_book_dict)
print(exact_value)

def remove_item_dict(remove_item, dictname):
    removeitem = phone_book_dict.pop(remove_item)
    return(removeitem)


remove_item = "Test3"
removeitem = remove_item_dict(remove_item,phone_book_dict)
print(removeitem)
print(phone_book_dict)