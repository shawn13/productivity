# -*- coding: UTF-8 -*-
import datetime
import sys
import smtplib
from email.mime.text import MIMEText
#############
#要发给谁，这里发给2个人
mailto_list=["xiaoshandd@126.com"]
#####################
#设置服务器，用户名、口令以及邮箱的后缀
mail_host="smtp.126.com"
mail_user="shawn13"
mail_pass="reasonSoul[13"
mail_postfix="126.com"
######################
def send_mail(to_list,sub,content):
    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
    d1 = datetime.datetime(2016, 12, 21)
    d2 = datetime.datetime.now()
    day_count = (d1-d2).days
    if send_mail(mailto_list,"生日倒计时","距离老婆的生日还有"+bytes(day_count)+"天，大蛋糕伺候"):
        print "发送成功"
    else:
        print "发送失败"
