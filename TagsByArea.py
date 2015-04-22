import tweepy
import json


consumer_key='xIvqTwnKncz4MvckyIzIzIsCh'
consumer_secret='XlJP5xE5OyVyRcJ5MDP20KratI7juDL0KrDYSAKSAzBb0GsrWc'

access_token='3164465356-IpWdPyksEN5eTHKKDT8KtCHdjbgaz6sFCQ7Trm2'
access_token_secret='onubCuaZdM3jEhcFj7HIighRuYcV7gyvhoGjWw2XByFkN'


class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        tweets = json.loads(data)
        try:
            #print(tweets['user']['location'])
            print(tweets['entities']['hashtags'])
            
        except UnicodeEncodeError:
            print('UnicodeEncodeError')
        print (' ')
        return True

    def on_error(self, status):
        print(status)
        return True

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    stream.filter(locations=[-122.75,36.8,-121.75,37.8,-74,40,-73,41,-89,41,-88,42,-119,33,-117,34.5])