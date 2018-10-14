"""发送邮件(不是很重要)"""
#coding:utf-8
import smtplib
from email.mime.text import MIMEText  #组装普通的email
from email.mime.multipart import MIMEMultipart  #上传附件

import sys
sys.path.append("..")
from  config import config as cf

#发送报告
def send_report():
    msg =  MIMEMultipart()   #混合格式的邮件
    #邮件正文
    body = MIMEText('测试报告','plain','utf-8')
    msg.attach(body)
    #邮件头
    msg['From'] = cf.sender
    msg['To'] = cf.receiver
    msg['Subject'] = cf.subject
    #报告附件
    with open(cf.report_file,'rb') as f:
        att_file = f.read()
    att1 =  MIMEText(att_file,'base64','utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'
    #上面后面两行是固定格式。第二行最后不用format，不然会暴露全路径，纠正上节课的问题
    msg.attach(att1)
    #发送邮件
    smtp = smtplib.SMTP_SSL(cf.smtp_sever)
    smtp.login(cf.smtp_user,cf.smtp_password)
    smtp.sendmail(cf.sender,cf.receiver,msg.as_string())
    cf.logging.info("send email done")


if __name__ == ("__main__"):
    send_report()