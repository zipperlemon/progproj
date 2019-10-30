# Shaafe Khan
from TwitterAPI import TwitterAPI # importeren twitter API
import re, os

def sendTweet(content):
    consumer_key = 'NewUDIZy2opOqnsWlRq3EQutT'
    consumer_secret = 'pzskqXmoSznLTPe5Qa6XjoxrgCtXT1qG305nMzVV8ZIGWg2i6H'
    access_token_key = '1188970441303568385-s6sugkh2nDv7e1Y1DFHUXaPhuQI5X6'
    access_secret = 'Ga40JxhyYYtp99wLvRxkL5jcsOrOwm54TipIz76vp2NAH'
    # Alle noodzakelijke keys voor het posten van tweets

    api = TwitterAPI(consumer_key,
                     consumer_secret,
                     access_token_key,
                     access_secret)
    # variable van twitterapi functie en de keys

    gebr_naam = "Rick"
    gebr_tweet = "NS is heilig test"

    # naam en tweet te krijgen via GUI

    # hier worden de namen en tweet samengevoegd

    tweet_post = api.request('statuses/update', {'status': content})
    # naam en tweet worden gepost
    print(tweet_post.status_code)
    return tweet_post.status_code
    # error code print


def removeBadChars(string):
    tmp = re.sub("[{}<>]", "", string)
    return tmp


def getTweetFiles():
    allTweetFiles = os.listdir("tweets")
    allTweets = []

    for file in allTweetFiles:
        if os.stat(os.getcwd() + "\\tweets\\" + file).st_size > 0:
            allTweets.append(file)

    return allTweets
