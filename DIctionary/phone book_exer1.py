# Phone Book
# Functional Requirements
# Add contact
# Name and phone are required
# Phone can contain only digits, spaces, -, +, (, )

namelist = ["Padma", "John", "Adam","padma"]
phonenumlist = [+1(312-345-4555),+1(416-346-4555),+1(321-456-2222),+1(322-999-5553)]

def checkduplicate(namelist):

   for name in namelist:
      counter = 0
      for i in range(0,len(namelist),1):
        if str.lower(name) == str.lower(namelist[i]):
          counter = counter + 1
        
      if counter > 1:
         print("Name is repeated :",name)

checkduplicate(namelist)

for phone in phonenumlist:
    for i in range(0,len(phone),1):
        print(type(phone[i]))
        if type(phone[i]) != int:
           if phone[i] != "+":
              if phone[i] != "-":
                 if phone[i] != "(":
                    if phone[i] != ")":
                       print("Phone number is not in right format :",phone)
        
        

# name1 = "Padma"
# phone1 = "+1(312-345-4555)"

# name2 = "John"
# phone2 = "+1(412-346-4555)"

# name3 = "Adam"
# phone3 = "+1(321-456-2222)"

# name4 = "padma"
# phone4 = "+1(322-999-5553)"




# No duplicate names allowed (case-insensitive)
# class init, validation, set / list append
# List all contacts
# Shows numbered list or clean table
# Columns: #, Name, Phone (optionally Email)
# formatting, loops, enumerate, string alignment
# Search by name
# Case-insensitive partial match
# Returns all matching contacts
# list comprehension, str.lower(), any()/filter()
# Delete contact
# Can delete by exact name or by number shown in list
# remove from list/dict, index handling