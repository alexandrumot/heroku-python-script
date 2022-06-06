import requests
from bs4 import BeautifulSoup
import re
import time
import datetime

import emailer

now = datetime.datetime.now()

url_base = "https://gogoanime.sk/spy-x-family-episode-"
curr_episode = 8

email_sender = "hackerutz21@gmail.com"
email_recipient = "hackerutz21@gmail.com"
email_password = "aghwpyjnitsqvstd"

email_body = "Here is the new episode: "

while True:
    next_episode = curr_episode + 1
    email_subject = f'Spy X Family: New Episode {next_episode} [Automated Email]  ' \
                    + str(now.day) + '-' \
                    + str(now.month) + '-' \
                    + str(now.year)

    r = requests.get(url_base + str(next_episode))
    soup = BeautifulSoup(r.content, "html.parser")
    video_elem = soup.find("iframe", attrs={"src": re.compile(
        r'//goload\.pro/streaming\.php\?id=\S+title=Spy\+x\+Family\+Episode\+(\d+)')})
    try:
        src_video_url = video_elem.attrs.get("src")
        video_url = "https:" + src_video_url
    except AttributeError:
        print("The is no new episode to watch!")
    else:
        print(email_body + video_url)
        emailer.send(
            email_sender,
            email_recipient,
            email_password,
            email_subject,
            email_body + video_url
        )

        curr_episode += 1

    time.sleep(5)
