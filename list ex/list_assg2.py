# 5. Given numbers, reverse numbers [1, 2, 3] -> [3, 2, 1]
# 6. Given numbers, rotate them in place N times [1, 2, 3, 4, 5] -> [4, 5, 1, 2, 3]
# 7. Given numbers, double them in place [1, 2, 3, 4, 5] -> [2, 4, 6, 8, 10]
# 8. Sort given numbers 
# 9. Sum of given numbers
# 10. Find even, odd
# 11. Multiply by 2

# 5. Given numbers, reverse numbers [1, 2, 3] -> [3, 2, 1]
list1 = [1, 2, 3]

def reverselist(listnm):
  revlist = []
  print(len(listnm))
  for num in listnm[::-1]:
     revlist.append(num) 
  return revlist

rlist = reverselist(list1)
print("Reverse list :", rlist)

# 6. Given numbers, rotate them in place N times [1, 2, 3, 4, 5] -> [4, 5, 1, 2, 3]

list2 = [1, 2, 3, 4, 5]


def rotate(listval):
        lastval = listval.pop()
        listval.insert(0,lastval)
        return listval

n = 3
for i in range(1,n+1,1):
    if i == 1:
       list = rotate(list2)
    else:
       list = rotate(list)

print("Rotate list :",list)

# 7. Given numbers, double them in place [1, 2, 3, 4, 5] -> [2, 4, 6, 8, 10]  - This is same as multiply by 2

def doublenum(listval):
    for i in range(0,len(listval),1):
      listval[i] = listval[i] * 2
    return listval

doublelist = doublenum(list2)
print("Double list :",doublelist)

# 8. Sort given numbers 

list4 = [56, 54, 100, 35, 83, 81, 66, 93, 81, 86]

def sortnum(listnm):
    length = len(listnm)
    for i in range(0, length-1,1):
        for j in range(0,length-1,1):
            num1 = listnm[j]
            num2 = listnm[j+1]
            if num1 > num2:
               listnm[j],listnm[j+1] = num2,num1
    return listnm
    
sortlist = sortnum(list4)
print("Sort List :",sortlist)

# 9. Sum of given numbers
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def total(listnm):
    tot = 0
    for i in range(0,len(listnm),1):
        tot = tot + listnm[i]         
    return tot

tot = total(list3)
print("Total of numbers : ",tot)

# 10. Find even, odd


def findeven(listnm):
    listeven = []
    listodd = []
    for i in range(0,len(listnm),1):
      if(listnm[i] % 2 == 0):
         listeven.append(listnm[i])
      else:
         listodd.append(listnm[i])
    return listeven, listodd

evenlist, oddlist = findeven(list3)
print("Even List :",evenlist)
print("Odd List :",oddlist)