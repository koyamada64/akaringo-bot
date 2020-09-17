# -*- coding: utf-8 -*-
import tweepy

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

# 好きな言葉をツイート
api.update_status("Pythonから")
