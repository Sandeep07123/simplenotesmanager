import smtplib
from email.message import EmailMessage  #mail format ki use chestam
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465) #465  & 587 is a port number 
    server.login('sandeepponugumati123@gmail.com','lihl bzwq wbci ingh')
    msg=EmailMessage()
    msg['FROM']='sandeepponugumati123@gmail.com'
    msg['TO']=to
    msg['Subject']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()