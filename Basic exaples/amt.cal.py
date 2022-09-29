Amt=int (input("enter amount :"))
pm =  (input ("payment method (credit,cash,upi);"))

if Amt >1000:
    Amt-= Amt *.03 #discount 3%
    if pm == 'credit':
        Amt-=100

        Amt+=Amt*.18 #tax 18%
        print("your final amt is :",Amt)
