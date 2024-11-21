import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# 連接到郵件伺服器
server = smtplib.SMTP('smtp.world4you.com', 25)
server.ehlo()

# 讀取郵件密碼
with open('password.txt', 'r') as f:
    password = f.read()
    
# 登錄郵件帳戶
server.login('mailtesting@neuralnine.com', password)

# 創建郵件內容
msg = MIMEMultipart()
msg['From'] = 'NeuralNine'
msg['To'] = 'testmails@spaml.de'
msg['Subject'] = 'Just A Test'

# 讀取郵件正文
with open('message.txt', 'r') as f:
    message = f.read()
    
# 添加郵件正文
msg.attach(MIMEText(message, 'plain'))

# 添加附件
filename = 'coding.jpg'
attachment = open(filename, 'rb')
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

# 將郵件內容轉為字符串並發送郵件
text = msg.as_string()
server.sendmail('mailtesting@neuralnine.com', 'testmails@spaml.de', text)