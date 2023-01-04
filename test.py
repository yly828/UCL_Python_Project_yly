import os.path
from message import Message
import pandas
import numpy as np


if not os.path.exists("messages.csv"):
    messages = pandas.DataFrame(columns=["author", "time", "text", "seen"])
    messages.to_csv("messages.csv")

df = pandas.read_csv("messages.csv")

if df.empty:
    print("No messages.")
else:
    # I only want to print messages that I have not seen before.
    # I am filtering them by the value of 'seen' which initially is always False.
    new_messages = df[df['seen'] == False]  # This seems to work perfectly well.
    if new_messages.empty:
        print("There are no new messages.")
    else:
        for index, row in new_messages.iterrows():
            author = row["author"]
            time = row["time"]
            text = row["text"]
            print(f"{author} ({time}): {text}")



            # Here I would like to change 'seen' of each row to True so when I revisit the board, the messages I have seen do not pop up again.
            # I've tried multiple myethods here to change the 'seen' column value in each row, then pass them back to the
            # messages.csv. Nothing has worked.

new_mess = input("Leave a message: ")
message = Message(new_mess)
