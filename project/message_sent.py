import requests
import json
from tkinter import*
from tkinter.messagebox import*


# function to send message 

def send_sms(number,message):
    
    url= "https://www.fast2sms.com/dev/bulk"
    
    Params={
        
    'authorization': 'WSUbmC2Xai8eyg9Iz1MKBcd7YnZJxspqlNoG0HR6jrfw45D3hTn5vXh2rVPo7c8RLWAlMYQISNGDwmCq',
    'sender_id':'FSTSMS',
    'message': message,
    'route': 'p',
    'number': number,
    'language': 'english',
    }
    
    response= requests.get(url,Params=Params)
    dic=response.json()
    print(dic)
    
    send_sms("8787209758", "This is you tube message" )
    

