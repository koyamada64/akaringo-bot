# -*- coding: utf-8 -*-
import os
import TextTweet

# APIの秘密鍵
CK,CS,AT,ATS=os.environ["CK"], os.environ["CS"], os.environ["AT"], os.environ["AS"]

TextTweet.puttweet(CK,CS,AT,AS)