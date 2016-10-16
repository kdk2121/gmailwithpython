import smtplib
from email.MIMEText import MIMEText

class Mail:

        def sendMail(self,id,pw,to,subject,content):
                HOST = 'smtp.gmail.com'
                port = 587
                msg = MIMEText(content, _charset='euc-kr')
                msg['Subject'] = subject
                msg['From'] = id
                msg['To'] = to

                s = smtplib.SMTP(HOST,port)
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(id, pw)
                s.sendmail(id, [to], msg.as_string())
                s.quit
