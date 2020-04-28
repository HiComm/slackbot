from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from os.path import basename


class Mail:
    def __init__(self):
        # SMTP認証情報
        self.account = "t.matsutake"
        self.password = "Hi2481"
    
        # 送受信先
        self.from_email = "slackbot@hioki.co.jp"

    def sendMail(self, to, subject, message, filepath):
        # MIMEの作成
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["To"] = to
        msg["From"] = self.from_email
        msg.attach(MIMEText(message))
        
        with open(filepath, "rb") as f:
            part = MIMEApplication(
                f.read(),
                Name=basename(filepath)
            )
    
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(filepath)
        msg.attach(part)
    
        # メール送信処理
        server = smtplib.SMTP("mail.hioki.co.jp", 587)
        #server.starttls()
        server.login(self.account, self.password)
        server.sendmail(self.from_email, [to], msg.as_string())
        server.close()