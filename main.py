import requests
from bs4 import BeautifulSoup
import re
import time
import datetime
import os
import emailer
from notify_run import Notify
 
notify = Notify()
now = datetime.datetime.now()

url_base = "https://gogoanime.sk/spy-x-family-episode-"
curr_episode = 9

email_sender = os.environ.get("SENDER")
email_receiver = os.environ.get("RECEIVER")
email_password = os.environ.get("PASSWORD")

email_body = "Here is the new episode: "
log_datetime = f'{str(now.hour+3)}:{str(now.minute)}:{str(now.second)} {str(now.day)}-{str(now.month)}-{str(now.year)}: '

while True:
    next_episode = curr_episode + 1
    email_subject = f'Spy X Family: New Episode {next_episode} Watch it now! {str(now.day)}-{str(now.month)}-{str(now.year)}'

    r = requests.get(url_base + str(next_episode))
    soup = BeautifulSoup(r.content, "html.parser")
    video_elem = soup.find("iframe", attrs={"src": re.compile(
        r'//goload\.pro/streaming\.php\?id=\S+title=Spy\+x\+Family\+Episode\+(\d+)')})
    try:
        src_video_url = video_elem.attrs.get("src")
        video_url = "https:" + src_video_url
    except AttributeError:
        print(log_datetime)
        print("The is no new episode to watch!")
    else:
        print(log_datetime, email_body + video_url)
        emailer.send(
            email_sender,
            email_receiver,
            email_password,
            email_subject,
            email_body + video_url
        )
        notify.send(f'Spy X Family: New Episode {next_episode}!')

        curr_episode += 1

    time.sleep(3600)
