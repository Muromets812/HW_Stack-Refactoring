import imaplib
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class WorkMail:
    def __init__(self, login, password):
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"
        self.login = login
        self.password = password

    def send_message(self, subject, recipients, new_message):
        # send message
        message = MIMEMultipart()
        message['From'] = self.login
        message['To'] = ', '.join(recipients)
        message['Subject'] = subject
        message.attach(MIMEText(new_message))

        message_send = smtplib.SMTP(self.GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        message_send.ehlo()
        # secure our email with tls encryption
        message_send.starttls()
        # re-identify ourselves as an encrypted connection
        message_send.ehlo()
        message_send.login(self.login, self.password)
        message_send.sendmail(self.login, message_send, message.as_string())
        message_send.quit()

        # send end

    def receive_message(self, header=None):
            # recieve
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email.message_from_string(raw_email)
        mail.logout()
        # end recieve

    if __name__ == "__main__":
        my_mail = WorkMail(login='abc@gmail.com', password='qwerty')
        my_mail.send_message('test', [xyz@gmail.com], 'test message')
        my_mail.receive_message()
