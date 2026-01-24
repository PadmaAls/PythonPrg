
x = 1 #start


while x <= 10: #stop
    print(x)
    x = x + 1 #step

def table_view(xval):
    while xval <= 10:
         #xval2 = xval * 2
         table_format = f"{xval} x 2 =  {xval * 2}"
         print(table_format)
         xval = xval + 1

table_view(1)


