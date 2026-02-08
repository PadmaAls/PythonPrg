def split(data, sep, start):
    lines = data.split(sep)
    return lines[start:len(lines):1]
    #return lines