# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
import os
import TextTweet
from PrepareChain import PrepareChain

# APIの秘密鍵
CK,CS,AT,AS=os.environ["CK"], os.environ["CS"], os.environ["AT"], os.environ["AS"]

twische = BlockingScheduler()

# 30分に一度ツイート
@twische.scheduled_job('interval',minutes=30)
def timed_job():
    f = open("data.txt",encoding="utf-8")
    text = f.read()
    f.close()
    chain = PrepareChain(text)
    triplet_freqs = chain.make_triplet_freqs()
    chain.save(triplet_freqs, True)
    TextTweet.puttweet(CK,CS,AT,AS)

if __name__ == "__main__":
    twische.start()
