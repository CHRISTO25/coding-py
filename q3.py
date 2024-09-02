principal_amount = int(input("Enter the principal amount : "))
interest_rate    = float(input("Enter the interest rate : "))
number_of_years  = float(input("Enter the year : "))

si = int((principal_amount* interest_rate*number_of_years)/100)
print(si)