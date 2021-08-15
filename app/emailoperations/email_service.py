import smtplib
import ssl


class EmailService:

    def __init__(self, email, smtp_server, port, sender_email, pwd):

        self.email = email
        self.smtp_server = smtp_server
        self.port = port
        self.sender_email = sender_email
        self.pwd = pwd

    def sendEmail(self):
        try:
            context = ssl.create_default_context()
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls(context=context)
            server.login(self.sender_email, self.pwd)
            message = self.email.name + "\n" + \
                      self.email.sender_email + "\n" + \
                      self.email.email_subject + \
                      "\n" + self.email.email_body
            server.sendmail(self.sender_email, "dheeraj.thodupunoori01@gmail.com", message)
            return True
        except Exception as error:
            return False
        finally:
            server.quit()
