from email.message import EmailMessage
import smtplib
import csv

def credentials():
    id='20B91A05T0@srkrec.ac.in'
    pwd='Zampoclone@142'
    return (id,pwd)

try:
    smtpObj=smtplib.SMTP('smtp-mail.outlook.com',587)
    smtpObj.ehlo()
    smtpObj.starttls()   
    id=credentials()[0]
    pwd=credentials()[1]

    smtpObj.login(id,pwd)
    msg=EmailMessage()

    msg['To']='20B91A05T0@srkrec.ac.in'
    msg['Subject']='testing'
    msg['From']='20B91A05T0@srkrec.ac.in'
    msg.set_content('Heii')

    smtpObj.send_message(msg)
    smtpObj.quit()
    
except Exception as err:
    print(err)