from TwitterAPI import TwitterAPI # importeren twitter API


def dispTweets():
    """Displays tweets"""
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
    tweetlist = []
    r = api.request('statuses/home_timeline', {'count': 5})
    for item in r.get_iterator():
        if 'text' and 'created_at' in item:
            timeanddate = item['created_at']
            twittime = timeanddate.split(" ")
            tijdvantweet = twittime[3]
            tweet = item['text']
            list_set = [tweet, tijdvantweet]
            tweetlist.append(list_set)
    print(tweetlist)
    return tweetlist


dispTweets()


