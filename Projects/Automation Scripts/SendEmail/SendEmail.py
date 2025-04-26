import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Import the email modules we'll need
from email.message import EmailMessage

MY_ADDRESS = 'eng.aaaziz@gmail.com'
PASSWORD = 'Aieaaziz_0710_1989_1989'

def main():
    
    
    # Open the plain text file whose name is in textfile for reading.
 
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content('Ali')

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'The contents o'
    msg['From'] = MY_ADDRESS
    msg['To'] = MY_ADDRESS
    
    # Send the message via our own SMTP server.
    # s = smtplib.SMTP('localhost')
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('your_email@gmail.com', 'your_password')

    s.send_message(msg)
    s.quit()





#     msg = MIMEMultipart()       # create a message
# 
#     # set up the SMTP server
#     s = smtplib.SMTP(host='smtp.gmail.com', port=587)
#     s.starttls()
#     s.login(MY_ADDRESS, PASSWORD)
# 
# 
#     # add in the actual person name to the message template
#     message = 'Mr ahmed'
# 
#     # Prints out the message body for our sake
#     print(message)
# 
#     # setup the parameters of the message
#     msg['From']=MY_ADDRESS
#     msg['To']= 'eng.aaaziz@gmail.com'
#     msg['Subject']="This is TEST"
#     
#     # add in the message body
#     msg.attach(MIMEText(message, 'plain'))
#     
#     # send the message via the server set up earlier.
#     s.send_message(msg)
#     del msg
#         
#     # Terminate the SMTP session and close the connection
#     s.quit()
    
if __name__ == '__main__':
    main()