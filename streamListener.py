import tweepy
from authKeys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']


class HidroTwitListener(tweepy.StreamListener):
    def on_data(self, data):
        print data
        return True
    def on_error(self, status):
        print status

if __name__ == "__main__":
    listenBot = HidroTwitListener()
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    stream = tweepy.Stream(auth, listenBot)
    stream.filter(track=['programming'])



