from dotenv import load_dotenv
from email.message import EmailMessage
from jinja2 import Template
import smtplib
import os


def GetEmailBody():
        openEmailTmpl = open(baseDir+"/templates/IT-EquipmentEmail.html", 'r').read()
        getHtmlCont = Template(openEmailTmpl)
        emailData = {}
        return getHtmlCont.render(fName=userData['firstName'])        

"""
Summary
-------------------
Sends the IT-Equipment email or the first day credentials email depends from which function from zonit script was called.

Parameters
-------------------
userData : Requestes this dictionary that contains basic employee info to send the email
emailFlag : Use to check if it is IT-Equipment or credentials email to send depending from the function in zonit script (DoSendITEmail() or DoSendCredsEmail()) that was called

Returns
-------------------
Nothing just prints a message when the email was sent
"""
print(f"User-> {userData['userEmail']} | And Email To -> {userData['userPrEmail']}")
load_dotenv(baseDir+'.env')
EMAIL_ADDRESS = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')
credsMsg = EmailMessage()        
msgBody = self.GetEmailBody()        
credsMsg['To'] =  #Receipent#
credsMsg['Subject'] = # Email Subject
credsMsg['From'] = EMAIL_ADDRESS    

credsMsg.add_alternative(msgBody, subtype='html')            
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(credsMsg)
    print(f"Email To -> {} Sent Successfully . . .")            
