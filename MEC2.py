from email.message import EmailMessage
import smtplib
import csv
import imghdr
import os

# I have to disable 2FA -2 Factor authentication
#I have to allow low key security access
try:
    smtpObj= smtplib.SMTP('smtp-mail.outlook.com',587) #set up a connection with SMTP Server
    smtpObj.ehlo()
    smtpObj.starttls() # TLS - transport layer security to ensure our message go securely
    id=os.environ.get('EMAIL_ADD')
    pwd=os.environ.get('EMAIL_PASS')
    print(id)
    print(pwd)

    smtpObj.login(id,pwd) # logged into my mail
    
    with open('emails.csv','r') as email_file:  # reading csv file
        csv_reader=csv.DictReader(email_file)   # converting each row into dictonary
        msg=EmailMessage() # create email message object
        for row in csv_reader:
            msg=EmailMessage() # create email message object
            msg['To']=row['To']
            msg['From']=row['From']
            msg['Subject']=row['Subject']
            msg.set_content(row['Content'])
            
            images=['img1.jpg','img2.jpg']
            for img in images:
                with open(img,'rb') as f:
                    img_data=f.read()
                    img_type=imghdr.what(f.name)
                    img_name=f.name
                msg.add_attachment(img_data,maintype='image',subtype=img_type,filename=img_name)
    
            with open('resume.pdf','rb') as f1:
                file_data=f1.read()
                file_name=f1.name
            msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)

            smtpObj.send_message(msg) #it will send an email using the given email object

    smtpObj.quit() #it will quit the current smtp connection
    

except Exception as err:
    print(err)