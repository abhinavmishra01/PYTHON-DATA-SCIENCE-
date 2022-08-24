#string validation

from multiprocessing.sharedctypes import Value


Value = input("Enter the Guest name:")
if value.startswith('Mr.'):
    print("Welcome Sir ")    
elif value.startswith("Mrs."):
    print("Welcome Ma'am ")
elif value.startswith("Dr."):
    print("Welcome Doctor")
else:
    print('You are not invited ')
