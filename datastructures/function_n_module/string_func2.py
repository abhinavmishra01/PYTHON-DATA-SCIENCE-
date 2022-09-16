# string  validation function 


value =input('enter something:')
#test
if value.isnumeric():
    print("only numbers", value.isnumeric())
if value.isalpha():
    print('only alphabets', value.isalpha())
    if value.isalnum():
      print('alphabet & numbers', value.isalnum())
if value.isspace():
    print('only spaces', value.isspace())
if value.isupper():
    print('uppercase alphabets', value.isupper())
if value.islower():
    print('lowercase alphabets', value.isupper())
