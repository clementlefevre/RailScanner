from service import email_service



def main():
    email_service.send_email('clement.san@gmail.com','test subject','test body')

if __name__ == '__main__':
    main()