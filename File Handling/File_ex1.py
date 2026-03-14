# read 
# read only "r" - if the file is not there throws error

#write
#Read and Write "w" - if the file is not there it creates a file
#Write overwrites the file all old contents are lost

#append
#Both Read and Write "a" - if file is not there it creates a new file
#write adds the content to the existing content doesn't overwrite

#file = open("path name",mode)

file = open(r"C:\Users\alash\Desktop\Python\fileread.txt","r")

content = file.read()
print("Type of Content : ",type(content))
print(content)
file.close()
print("****************************************************************")

with open(r"C:\Users\alash\Desktop\Python\fileread.txt","r") as file:

#  contline = file.readline()
#  while(len(contline) > 0):
#   contline = file.readline()
#   print(contline)

 
 readbool =  True
 while readbool:
    contline = file.readline()
    readbool = len(contline) > 0
    print("Length : ", len(contline))
    print(contline)

 print("Type of Contline :",type(contline))

print("****************************************************************")


with open(r"C:\Users\alash\Desktop\Python\fileread.txt","r") as file:
 contlines = file.readlines()
 print("Type of Contlines :",type(contlines))
 print(contlines)

print("****************************************************************")

try:
   file = open(r"C:\Users\alash\Desktop\Python\filereadnew.txt","r")


except FileNotFoundError:
      print("File Not Found")
finally:
      file.close()

