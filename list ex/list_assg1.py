# 1. Input: [56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]
# 2. Given math scores, find how many scored centum: 100
# 3. Given scores, grade each score: A > 90, B > 80, C > 60, others D
# 4. Given scores, count students for each grade


# 1. Input: [56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]
# 2. Given math scores, find how many scored centum: 100
markslist = [56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]

n = 100
def findcount(n):
    centum = markslist.count(n)
    return centum


totcount = findcount(n)
print("Total count :",totcount)

# 3. Given scores, grade each score: A > 90, B > 80, C > 60, others D

def gradecalc(markslist):
 gradelist = []
 print(len(markslist))
 for i in range(0, len(markslist),1):
    if markslist[i] <= 60:
        gradelist.append("D")
    elif markslist[i] >= 90:
        gradelist.append("A")
    elif markslist[i] >= 80:
           gradelist.append("B")
    elif markslist[i] > 60:
              gradelist.append("C")
 return gradelist

glist = []
glist = gradecalc(markslist)
print("Grade List :",glist)
#print(len(glist))

# 4. Given scores, count students for each grade

def Acountgrade(glist,grade):
    Acount = glist.count(grade)
    return Acount

gradelist = ("A","B","C","D")
for j in range(0, len(gradelist),1):
   grade = gradelist[j]
   Gcnt = Acountgrade(glist,grade)
   print(grade ,Gcnt)

