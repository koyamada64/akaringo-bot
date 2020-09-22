import os
import re
import requests
import tweepy

def gettweet(CK,CS,AT,AS):

    # APIに接続
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)

    f = open(r"data.txt",mode="a",encoding="utf-8")

    # 自分のTLの最新ツイートを取得
    # results=api.home_timeline(count=8,exclude_replies=True)
    results=api.home_timeline(count=200)

    for result in results:

        text=result.text
        #リンクの削除
        text=re.sub(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-…_]+", "" ,text)

        #RT:の削除
        text=re.sub(r"RT", "" ,text)
        text=re.sub(r":", "" ,text)

        #ライパIDの除外
        text=re.sub(r"[0-9]{7}", "",text)

        #@ツイートの削除(昔仲良くしていたけど今ブロ解された…みたいな人に行くと地獄なので)
        text=re.sub("@[\w]+","",text)

        #「#peing」「#質問箱」を消す
        text=re.sub("#peing","",text)
        text=re.sub("#質問箱","",text)

        #data.txtに追加で書き込み
        f.write(text+"\n")

    f.close()
