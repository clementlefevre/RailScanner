# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

from app.config import EMAIL_USER, EMAIL_PASSWORD, MAIL_PORT, MAIL_SENDER, MAIL_SERVER, MAIL_SUBJECT_PREFIX, MAIL_USE_TLS


def send_email(recipient, subject, body):
    import smtplib

    mail_user = EMAIL_USER
    mail_pwd = EMAIL_PASSWORD
    FROM = MAIL_SENDER

    print mail_user
    print mail_pwd
    print FROM
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
        server.ehlo()
        server.starttls()
        server.login(mail_user, mail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except Exception as e:
        print "failed to send mail"
        print e.args


if __name__ == '__main__':
    send_email('clement.san@gmail.com', 'test subject', 'test body')
