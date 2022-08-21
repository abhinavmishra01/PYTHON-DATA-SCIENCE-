Price = int(input('Enter price of product: '))
quantity = int(input('Enter quantity: '))
amount = Price * quantity
if amount > 1000:
    discount = amount*0.20
else:
    discount = 0
    net_amount =amount-discount
    print ('bill amount;',amount)
    print ('discount;', discount)
    print('your net bill amountis',net_amount)


