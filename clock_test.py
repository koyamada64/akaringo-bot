# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
import os
import TextTweet

# APIの秘密鍵
CK="uZ6mQkBSn6Nfwi7wXuc5dS6o8"
CS="6aMAiBussLyCX65zST7052oa8ot7OHSmlp3fh3vUdAo0tMTUPY"
AT="1299632209142325248-3miG1Tua7Pvy22u9kV5cXOjZ0OjJTp"
AS="wHSvgM8CuJA2OV3RURNNsT9tJd27rbSqYMFJ1V8kTcljE"

twische = BlockingScheduler()

# 30分に一度ツイート
@twische.scheduled_job('interval',minutes=1)
def timed_job():
    TextTweet.puttweet(CK,CS,AT,AS)

if __name__ == "__main__":
    twische.start()