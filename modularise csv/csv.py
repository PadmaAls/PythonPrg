# Input
# Name, City, Math, Science, Language
# John, Chennai, 40, 60, 50
# Dave, Chennai, 34, 60, 50
# Steve, Bangalore, 34, 60, 50

# Expected Output
# Name, City, Math, Science, Language, Total, Average, Top Score
# John, Chennai, 40, 60, 50, 150, 50, 60
# Dave, Chennai, 34, 60, 50
# Steve, Bangalore, 34, 60, 50


# process input string
# - split into lines
# - skip first line
# - split lines into works
# - process only numbers, skip strings
# calculate sum, average, top
# add it back to the line
# combine all lines

# DRY - Do not repeat yourself
# Single Responsibility - do one job, do it well
data = "Name, City, Math, Science, Language \n John, Chennai, 40, 60, 50 \n Dave, Chennai, 34, 60, 50 \n Steve, Bangalore, 34, 60, 50"

from parse import split
from calc import statistics

sep = "\n"
start = 1

lines = split(data, sep, start)
#print(lines)
for line in lines: # John, Chennai, 40, 60, 50
    wordsep = ","
    start = 2
    words = split(line,wordsep,start)
    #print(words)
    tot, avg, top = statistics(words)
    #print(tot)
    #print(avg)
    #print(top)
    
    details = f"{line.replace(" ","")},{tot},{avg},{top}"
    print(details)


