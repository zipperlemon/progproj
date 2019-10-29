# Shaafe Khan
from TwitterAPI import TwitterAPI # importeren twitter API

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
gebr_tweet = "NS is heilig"
# naam en tweet te krijgen via GUI


def gebr_naam_tweet(naam, tweet):
    naam_en_tweet = "\"{0}\" - {1}" .format(tweet, naam)
    return naam_en_tweet
# hier worden de namen en tweet samengevoegd


tweet_post = api.request('statuses/update', {'status': gebr_naam_tweet(gebr_naam, gebr_tweet)})
# naam en tweet worden gepost
print(tweet_post.status_code)
# error code print

