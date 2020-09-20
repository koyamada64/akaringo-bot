import os
import re
import requests
import tweepy

def gettweet(CK,CS,AT,AS):

    # APIに接続
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)

    # 自分のTLの最新ツイートを取得
    results=api.home_timeline(count=5,include_rts=False)

    f = open(r"data.txt",mode="a",encoding="utf-8")

    for result in results:

        #リンクの削除
        result.text=re.sub(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-…_]+", "" ,result.text)

        #@ツイートの削除(昔仲良くしていたけど今ブロ解された…みたいな人に行くと地獄なので)
        result.text=re.sub("@[\w]+","",result.text)

        #「#peing」「#質問箱」を消す
        result.text=re.sub("#peing","",result.text)
        result.text=re.sub("#質問箱","",result.text)

        #data.txtに追加で書き込み
        f.write(result.text+"\n")

    f.close()
