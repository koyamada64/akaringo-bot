# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
import os
import TextTweet

# APIの秘密鍵
CK,CS,AT,ATS=os.environ["CK"], os.environ["CS"], os.environ["AT"], os.environ["AS"]

twische = BlockingScheduler()

# 30分に一度ツイート
@twische.scheduled_job('interval',minutes=15)
def timed_job():
    TextTweet.puttweet(CK,CS,AT,AS)

if __name__ == "__main__":
    twische.start()