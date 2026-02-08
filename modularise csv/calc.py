def statistics(data):
    sum = 0
    avg = 0
    top = 0

    for i in range(0,len(data),1):
        num = int(data[i])
        sum = sum + num
        top = max(top, num)

    #print(len(data))
    avg = sum // len(data)
    return sum, avg, top