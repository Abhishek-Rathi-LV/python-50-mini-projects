def simple_interest(principal, rate, time):
    return (principal* rate * time)/100
while True:
    
    print("===== SIMPLE INTEREST CALCULATOR =====")
    print("Press 1 for calculating simple intrest ")
    print("press anything else for exit")
    choice=int(input("Enter your choice"))
    if choice==1:
        p=float(input("Enter Principal Amount : "))
        r=float(input("Enter the rate of intrest P.A. :"))
        t=float(input("Enter Time in years : "))
        intrest=simple_interest(p,r,t)
        total=p+intrest
        print("Simple Intrest :",intrest)
        print("Total Amount",total)
    else:
        print("Thank You For choosing us ")
        break
    
