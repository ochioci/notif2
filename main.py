import requests
import json
import time
import smtplib, ssl
import time
from bs4 import BeautifulSoup
lastCheck = 0
reAddress = "beckettrandlettapps@gmail.com"
def run (): 
    checkIn()
    interval = 120
    URL = "https://nycrtspublicportal.azurewebsites.net/data/activeinterventioncases"
    
    #testing
    # URL = "https://doofus2.neocities.org/testing"

    page = requests.get(URL, headers={'Cache-Control': 'no-cache'})
    soup = BeautifulSoup(page.content, 'html.parser')
    
    #DO NOT USE HTTPS
    storeURL = "http://bths.ochi.pw/notify/store.php"
    getURL = "http://bths.ochi.pw/notify/get.php"


    data = (soup.text.strip()).lower()
    prevDataReq = requests.get(getURL, verify = False, headers={'Cache-Control': 'no-cache'})
    prevData = prevDataReq.text.strip()
    jsonData = json.loads(data)["value"]
    tech = False
    toNotify = False
    for school in jsonData:
        if ('brooklyn tech' in school["nycsr_building.nycsr_buildingname"]):
            print ('tech is here!')
            #compare to prev data
            #upload new data
            req = requests.post(storeURL, json.dumps(school), verify = False, headers={'Cache-Control': 'no-cache'})
            # print(req.text)
            tech = True
            newData = json.dumps(school).strip()
            if (prevData != newData): #prevData and newData should both BE STRINGS ADN NOT JSON
                #data has changed
                print(prevData, "===========================================", newData)
                toNotify = True
                notify()
            
    
    if tech == False:
        print ("tech is not here")
        #compare "null" to prev data
        print(prevData)
        req = requests.post(storeURL, json.dumps({"null": True, "nycsr_building.nycsr_buildingname": "null"}), verify = False, headers={'Cache-Control': 'no-cache'})
        if (not (json.loads(prevData)["nycsr_building.nycsr_buildingname"] == "null")):
            toNotify = True
            notify()
        
        #upload new data (null)
        
        # print(req.text)
        a = 0
    
    if (toNotify == False): 
        print ("No Change!")


    time.sleep(interval)
    run()



def checkIn(): 
    global lastCheck
    if (time.time() - lastCheck > 5000): 
        lastCheck = time.time()
        print("checking in!")
        port = 465
        password = "PASSWORD"
        email = "beckettnotifs@gmail.com"
        message = "Checking in!"
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server: 
            print (server.login(email, password))
            server.sendmail(email, "omallsiecat@gmail.com" , message)

def notify ():
    #make sure less secure app access is on, google says it turns off automatically
    print('notify!!! BIG DEAL BIG DEAL')
    port = 465
    password = "PASSWORD"
    email = "beckettnotifs@gmail.com"
    message = "A change was detected"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server: 
        print (server.login(email, password))
        server.sendmail(email, "omallsiecat@gmail.com", message)


run()
