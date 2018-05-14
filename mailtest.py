#!/usr/bin/env python3

#from smtplib import SMTP
from smtplib import SMTP_SSL, SMTPAuthenticationError
from email.mime.text import MIMEText
from email.header import Header
import sys
#from email.generator import BytesGenerator


def getConnect():
    strUsername = 'tongze.zhu@westwell-lab.com'
    strPasswd = sys.argv[1]
    strServerIp = 'smtp.exmail.qq.com'
    nServerPort = 465
    try:
        smtpconn = SMTP_SSL()
        smtpconn.connect(strServerIp, nServerPort)
        smtpconn.login(strUsername, strPasswd)
        return smtpconn
    except TimeoutError as err:
        print("[Error]: Can't connect to {}: {}".format(strServerIp, err))
        return None
    except SMTPAuthenticationError as err:
        print('not connected:', err)
        smtpconn.quit()
        return None
    except BaseException:
        print('not connected!')
        if smtpconn != None:
            smtpconn.quit()
        return None

def sendNotification(msg):
    strUsername = 'tongze.zhu@westwell-lab.com'
    recipients = ['tongze.zhu@westwell-lab.com', 'a@westwell-lab.com','',]
    mail = MIMEText(msg, 'plain', 'utf-8')
    mail['From'] = strUsername 
    mail['To'] = ','.join([r for r in recipients if r!=''])
    mail['Subject'] = Header('请给我发回复邮件', 'utf-8').encode()
    print(mail.as_string())

    conn = getConnect()
    if conn != None:
        conn.sendmail(strUsername, recipients, mail.as_string())
        conn.quit()
    

sendNotification('你好呀Hello: bye')

