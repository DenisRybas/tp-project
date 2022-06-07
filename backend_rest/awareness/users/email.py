import smtplib
import ssl

import flask


class SmtpEmail:
    def __init__(self, login: str, password: str):
        self._smtp = smtplib.SMTP_SSL(
            flask.current_app.config["MAIL_SERVER"],
            flask.current_app.config["MAIL_PORT"],
        )
        self._login = login
        self._password = password

    def send(self, message, to):
        self._smtp.ehlo()
        self._smtp.starttls(context=ssl.create_default_context())
        msg = "Subject: {}\n\n{}".format("From awareness team", message)
        self._smtp.login(self._login, self._password)
        self._smtp.sendmail(self._login, [to], msg=msg)
        self._smtp.quit()
