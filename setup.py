import requests
import json
import time
import smtplib, ssl
import time
from bs4 import BeautifulSoup

def checkIn(): 
    global lastCheck
    if (True): 
        lastCheck = time.time()
        print("checking in!")
        port = 465
        password = "PASSWORD"
        email = "beckettnotifs@gmail.com"
        message = "Starting Up"
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server: 
            print (server.login(email, password))
            server.sendmail(email, "omallsiecat@gmail.com" , message)



checkIn()
