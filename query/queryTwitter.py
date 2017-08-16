import tweepy
from tweepy import OAuthHandler

sinceId = None
resultSet = set([])
originSet = set([])


def getInfoFromTwitter():
    consumer_key = '3en69qjjjUSZhsXiPPe3oT1ex'
    consumer_secret = 'DDfbbdszFzfpmHwJ7paif7m8WQCDavdTOwkFqlBcmnAcRKStl7'
    access_token = '851977611194490880-1Z39tkNzMqrJM526aHfv7zDNXQMep4D'
    access_secret = 'Psqe0wG0eJCipVaXL7RJcoceHq8bGf4nzGS23Eoi0DiQ7'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, proxy='127.0.0.1:1087', retry_count=3, retry_delay=5,
                     retry_errors=set([401, 404, 500, 503]), wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

    global sinceId
    global resultSet
    global originSet
    resultSet.clear()

    query = '#ico'
    maxId = None
    pageCount = 0
    while pageCount < 10:
        reslist = api.search(q=query, count=100, result_type="recent", since_id=sinceId, max_id=maxId,
                             include_entities=True)
        pageCount += 1
        for tweets in reslist:
            maxId = tweets.id
            if (not tweets.retweeted) and ('RT @' not in tweets.text):
                for tag in tweets.entities['hashtags']:
                    text = tag['text']
                    if text not in originSet:
                        resultSet.add(text)
                        originSet.add(text)
    sinceId = maxId
    return list(resultSet)


# getInfoFromTwitter()

