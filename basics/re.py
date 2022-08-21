
from tkinter import*
root=Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

# Heading

Label(root, text="Python Registration Form",font="ar 15 bold").grid (row=0,column =3)


#Fields Name

name=Label(root , text ="name")
phone= Label(root,text="phone")
gender = Label (root, text ="Gender")
emergency=Label (root , text= "emergency")
paymentmood = Label(root, text= "Payment Mood")

#packing Fileds

name. grid(row=1, column =2)
phone.grid (row=2,column =2)
gender.grid (row=3, column =2)
emergency.grid(row=4, column =2)
paymentmood.grid(row=5,column=2)

# Variable for storing data
namevalue= StringVar
phonevalue= StringVar
gendervalue=StringVar
emergencyvalue=StringVar
paymentmoodvalue=StringVar
checkvalue=IntVar

#Creating entry Field
nameentry=Entry(root,TextVariable=namevalue)
phoneentry=Entry(root, TextVariable = phonevalue)
genderentry =Entry(root,Textvariable= gendervalue)
paymentmoodentry=Entry(root,Textvariable= paymentmoodvalue)
emergencyentry=Entry(root,Textvariable= emergencyvalue)

#packing entry fields 
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmoodentry.grid(row=5,column=3)

#Creating Checkbox
Checkbutton=Checkbutton(text="remember me?", variable=checkvalue)
Checkbutton.grid(row=6,column=3)

# SUMBIT BUTTON
Button(text="Submit",command=getvals).grid(row=7,column=3)



root.mainloop()