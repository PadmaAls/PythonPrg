# compute income tax
# 4-8 -> 5%, 8-12 -> 10%, 12-16 -> 15%, 16-20 -> 20% , 20-24 -> 25% , above 24 -> 30%

def income_tax(income):
    if income >= 400000 and income <= 800000:
        tax = (income * 5)/ 100
        print ("Tax for income is :", tax)
    else:
        if income > 800000 and income <= 1200000:
            tax = (income * 10)/ 100
            print ("Tax for income is :", tax)
        else:
            if income > 1200000 and income <= 1600000:
                tax = (income * 15)/ 100
                print ("Tax for income is :", tax)
            else:
                if income > 1600000 and income <= 2000000:
                    tax = (income * 20)/ 100
                    print ("Tax for income is :", tax)
                else:
                    if income > 2000000 and income <= 2400000:
                        tax = (income * 25)/ 100
                        print ("Tax for income is :", tax)
                    else:
                        if income > 2400000:
                            tax = (income * 30)/ 100
                            print ("Tax for income is :", tax)
                        else:
                            print ("Tax for income is null")
        

income = int(input("Enter the income value : "))
income_tax(income)

#Given metal name print the price - gold/silver/platinum

# GOLD 1G = Rs. 14,199
#SILVER 1G = Rs. 266
#Platinum 1g = Rs.6700

def metal_price(metal, weight_in_gm):
    Gold_Price = 14199
    Silver_Price = 266
    Platinum_Price = 6700
    if metal == "Gold":
       tot_price = weight_in_gm * Gold_Price
       print ("Total Price of Gold is : Rs.",tot_price)
    else:
        if metal == "Silver":
            tot_price = weight_in_gm * Silver_Price
            print ("Total Price of Silver is : Rs.",tot_price)
        else:
           if metal == "Platinum":
              tot_price = weight_in_gm * Platinum_Price
              print ("Total Price of Silver is : Rs.",tot_price)

metal = input("Enter the metal name Gold/Silver/Platinum :")
weight_in_gm = int(input("Enter the weight of metal in gms :"))
metal_price(metal,weight_in_gm)