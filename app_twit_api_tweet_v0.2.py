# Shaafe Khan
from TwitterAPI import TwitterAPI
# Imports the TwitterAPI python wrapper package used for interacting with Twitter API


api = TwitterAPI('NewUDIZy2opOqnsWlRq3EQutT',
                 'pzskqXmoSznLTPe5Qa6XjoxrgCtXT1qG305nMzVV8ZIGWg2i6H',
                 '1188970441303568385-s6sugkh2nDv7e1Y1DFHUXaPhuQI5X6',
                 'Ga40JxhyYYtp99wLvRxkL5jcsOrOwm54TipIz76vp2NAH')
# Turns necessary API/User Authentication keys and TwitterAPI package into a callable variable


gebr_naam = "Rick"
gebr_tweet = "NS is heilig"
# Variables containing the name and tweet content inputted by the user


def gebr_naam_tweet(naam, tweet):
    """Returns the name and tweet content as one string"""
    naam_en_tweet = "\"{0}\" - {1}" .format(tweet, naam)
    return naam_en_tweet


tweet_post = api.request('statuses/update', {'status': gebr_naam_tweet(gebr_naam, gebr_tweet)})
# Sends a status update request to the TwitterAPI package. status value is the return of gebr_naam_tweet function with name and tweet content data


print(tweet_post.status_code)
# Displays the status update request error code
