import os.path
from datetime import datetime
import pandas


class Message:
    if os.path.exists("messages.csv"):
        messages = pandas.read_csv("messages.csv")
    else:
        messages = pandas.DataFrame()

    def __init__(self, author, text, to="", subject="", private=False):
        self.author = author
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.to = to
        self.subject = subject
        self.text = text
        self.private = private

        message = {"author": self.author, "time": self.timestamp, "to": self.to, "subject": self.subject,
                   "text": self.text, "private": self.private}
        df = pandas.DataFrame([message])
        Message.messages = pandas.concat([Message.messages, df], ignore_index = True)
        Message.messages.to_csv("messages.csv", index = False)



