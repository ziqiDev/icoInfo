import smtplib
import time
from configparser import ConfigParser
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def sendEmail(content):
    from_addr = getEmailProperties('send_add')
    password = getEmailProperties('send_pass')
    to_addr = getEmailProperties('receiver_add')
    smtp_server = 'smtp.ym.163.com'
    header = getheader()

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = _format_addr('icoInfoServer <%s>' % from_addr)
    msg['To'] = _format_addr(to_addr)
    msg['Subject'] = Header(header, 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(0)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


def getheader():
    date = (time.strftime("%Y-%m-%d", time.localtime()))
    header = '%s_ico信息汇总' % date
    return header


def getEmailProperties(name):
    cf = ConfigParser()
    cf.read('conf/conf.config')
    return cf.get("email", name)


# sendEmail()
