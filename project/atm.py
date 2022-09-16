import time
print("please insert your card")

time.sleep(S)

pasword=1234

pin=int(input("enter your atm pin"))

balance= 5000

if pin==pasword:
    
    print(" "
          1== balance
          2== withdraw balance
          3== deposit balance
          4== exit
          === 
           )
            
    try:
     option=int(input("lease enter your choise"))
     
    except:
        print("plese enter valid option")
    
    if option==1:
     print(f"your current {balance}")
     
     if option==2:
     
         withdraw_amount=int(input('please enter withdraw_amount'))
         
         balance=balance=withdraw_amount
         
         print(f"{withdraw_amount}is debited from your account")
         print(f"your updated balance is {balance}")
         
         if opton==3:
           
           deposit_amount=intput("please enter deposit_amount")
         
         
         balance=balance+deposit_amount
         print(f"{deposit_amount}is credit to your account")
         
         print(f"your updated   balance is {balance}")
         
         
         if option==4:
          break 