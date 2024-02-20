import smtplib, ssl

host='smtp.gmail.com'
port=465 #for SSL

context=ssl.create_default_context() #for sending emails securely Create a secure SSL context

usermail='saivenkatesh619@gmail.com'
password="lfzwbmpcwxtasafu"
sendto='saivenkatesh619@gmail.com'
message="""\
Subject : Mail from your portfolio
Test Mail
"""

with smtplib.SMTP_SSL(host,port,context=context) as server:
    server.login(usermail,password)
    server.sendmail(usermail,sendto,message)
    server.quit()



