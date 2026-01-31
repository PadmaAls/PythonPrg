

#print multiplication table of a number

tableval = 4

print("Multiplication table using for loop")

for i in range(1,11,1):
    table_format = f"{i} x {tableval} =  {i * tableval}"
    print(table_format)

print("----------------------------------------------------")
#sum of n numbers (1+2+3+...10)

print("Sum of n numbers using for loop")
n = 11
sum = 0
for i in range(1,n,1):
    sum = sum + i

print(sum)
print("----------------------------------------------------")

#find a position of a char in string using for loop Hello (W)orld -> 6

full_str = "Hello World"

full_str_len = len(full_str)
find_char = "W"

for i in range(0,full_str_len,1):
    if full_str[i] == find_char:
       print("Char found in the position : "+str(i))
       break

   
