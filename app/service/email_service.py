import smtplib
import logging

import ipdb
from  app.config import EMAIL_USER, EMAIL_PASSWORD, MAIL_PORT, MAIL_SENDER, MAIL_SERVER



logger = logging.getLogger("scraper_sncf")

def send_email(recipient, subject, body):
    

    mail_user = EMAIL_USER
    mail_pwd = EMAIL_PASSWORD

    print EMAIL_PASSWORD
    FROM = MAIL_SENDER
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
        logger.info('successfully sent the mail')
    except Exception as e:
        print logger.error("failed to send mail : {}".format(e.args))


def main():
    send_email('clement.san@gmail.com','test subject','test body')


if __name__ == '__main__':

    logger.debug("start scraper...")
    main()
