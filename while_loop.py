
#print 1, 2 , 3... 10
print("Print 1 to 10 values")
x = 1 #start


while x <= 10: #stop
    print(x)
    x = x + 1 #step

print("------------------------------------------------------------")

#print 2, 4 , 6... 20
print("Print 2, 4 , 6... 20")
def print_double(x):
    while x <= 10:
        print (x*2)
        x = x+1

print_double(1)

print("------------------------------------------------------------")

#print table format 1x2 = 2 ... 10x2 = 20
print ("Table format 1x2 = 2 ... 10x2 = 20")

def table_view(xval, tableval):
    while xval <= 10:
         #xval2 = xval * 2
         table_format = f"{xval} x {tableval} =  {xval * tableval}"
         print(table_format)
         xval = xval + 1
xval = 1
tableval = 2
table_view(xval, tableval)

print("------------------------------------------------------------")

#print odd numbers given a number - 10 - 1,3,5,7,9
print ("odd numbers given a number - 10 - 1,3,5,7,9")

def odd_nums(num):
    val = 1
    while val <= num:
        print(val)
        val = val+2
        

odd_nums(10)



