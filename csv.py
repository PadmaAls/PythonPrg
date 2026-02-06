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

data = "Name, City, Math, Science, Language \n John, Chennai, 40, 60, 50 \n Dave, Chennai, 34, 60, 50 \n Steve, Bangalore, 34, 60, 50"

# process input string
# - split into lines
# - skip first line
# - split lines into works
# - process only numbers, skip strings
# calculate sum, average, top
# add it back to the line
# combine all lines

def parse_csv(data):
    tokens = data.split("\n")
    tokens_len = len(tokens)
    for i in range(1,tokens_len,1):
        word_split = tokens[i].split(",")
        word_split_len = len(word_split)
    
        sum = 0
        avg = 0
        top = 0

        for j in range(2,word_split_len,1):
            sum = sum + int(word_split[j])
            
            if (top < int(word_split[j])):
                top = int(word_split[j])
        
        
        avg = sum // 3
        wrd3 = word_split[3].strip(" ")
        all_details = f"{word_split[0].strip()},{word_split[1].strip()},{word_split[2].strip()}, {word_split[3].strip()}, {word_split[4].strip()},{sum},{avg},{top}"
        print(all_details)
                 
parse_csv(data)

