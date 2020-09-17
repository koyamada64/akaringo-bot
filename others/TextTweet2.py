# -*- coding: utf-8 -*-
import GenerateText

def puttweet():
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)

    tweet=GenerateText.gentext()

    api.update_status(tweet)
