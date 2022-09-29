from email import message
import smtplib  as  S
ob=S.SMTP("smtb.gmail.com",587)

ob.starttls()

ob.login("abh6665@gmail.com",) 

subject="sending email using pyton"
body="This is tutorial of sending email using python script in simple steps "

message="Subject:{}\n\n{}".format(subject,body)
#print(message)
listofaddress=("abhinavm7952@gmail.com","abh66665@gmail.com")
ob.sendmail("abhinavm7952@gmail.com",list of address,messsage)
print("send successfully...")
ob.quit()
