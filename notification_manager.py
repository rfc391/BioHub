
import yagmail
import os

class NotificationManager:
    def __init__(self):
        self.email = os.environ.get('EMAIL_USER')
        self.password = os.environ.get('EMAIL_PASS')
        self.yag = yagmail.SMTP(self.email, self.password)

    def send_email_notification(self, subject, body, to=None):
        if to is None:
            to = self.email
        try:
            self.yag.send(to=to, subject=subject, contents=body)
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False
