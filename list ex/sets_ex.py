teamA = {"John", "Dave", "Mike","Bob"}
teamB = set()

teamB.add("Bob") #add single entry to a set
teamB.update(["Charlie", "Robert", "John"]) #add multiple entries from a list to a set
print("Length :", len(teamA))

teamB.difference(teamA) #what this line will do?

x = 6 + 4

print("Team A : ", teamA)
print("Team B : ", teamB)
# union
all_members = teamA | teamB
print("Union : ", all_members)
print("Union Count : ", len(all_members))

# intersection
common_a_b = teamA & teamB
print("Intersection : ", common_a_b)
print("Intersection Count : ", len(common_a_b))

# difference
only_team_a = teamA - teamB
print("Diff only Team A : ", only_team_a)
print("Diff Only A Count : ", len(only_team_a))

# symmetric difference
contributes_100 = teamA ^ teamB
print("Individual contri 100% :", contributes_100)
print("Individual contribution Count : ", len(contributes_100))


x = set("Hello")
print(x)
#add an element to set
x.add(2)
print(x)
#remove an element from set throws key error when element is not there
x.remove("e")
print(x)

# remove duplicates
numbers = [1, 2, 3, 3, 4, 1]
unique = list(set(numbers))
print(numbers)
print(unique)

set_nums = {1, 2, 3, 4, 5}
nums = {1, 2, 3}

# sub, super set check
print(nums.issubset(set_nums))
print(set_nums.issuperset(nums))

print(set_nums.issubset(nums))


# days = {"mon"..."sat" ,"sun"}
# work_week = { "mon" ... "fri" }

numbers = [1, 2, 3, 4]
numbers.sort()
print("Numbers  : ", numbers)
ordered = sorted(numbers)
print("Ordered : ",ordered)