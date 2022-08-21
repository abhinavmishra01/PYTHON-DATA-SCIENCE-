from atexit import register
from os import name
print("Register your details")


name=input("enter your name")
email=input("enter your email")
password=input ("enter your password")
confrimpassword= input("enter your confrim password")
gender=input ("enter your gender (M/F/O):")

if len (name)>4 and len (name)<25:
    if '@'in email:
        if password==confrimpassword:
            print ("You are registered")
        else:
              print ("passwords do not match")
    else:
        print (" email is invalid ")
else:
       print ('username must be between 4 and 25 chars')

