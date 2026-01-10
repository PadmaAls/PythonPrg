# Given number print day of the week 1 > Monday, 7 > Sunday

def print_day(daynum):
    if daynum == 1:
        print ("Monday")
    else:
        if daynum == 2:
            print ("Tuesday")
        else:
            if daynum == 3:
                print ("Wednesday")
            else:
                if daynum == 4:
                   print ("Thursday")
                else:
                    if daynum == 5:
                        print ("Friday")
                    else:
                        if daynum == 6:
                            print ("Saturday")
                        else:
                            if daynum == 7:
                               print ("Sunday")
                            else:
                                print ("Invalid day number")
                        
daynum = int(input("Enter the number from 1 to 7 to see the weekday : "))

print_day(daynum)
            