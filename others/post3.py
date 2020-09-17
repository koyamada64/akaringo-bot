# -*- coding: utf-8 -*-
import os
import tweepy

CK=os.getenv("CK")
CS=os.getenv("CS")
AT=os.getenv("AT")
AS=os.getenv("AS")

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

# 好きな言葉をツイート
api.update_status("Pythonから")
