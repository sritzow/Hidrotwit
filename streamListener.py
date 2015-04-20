from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import stream

#http://apps.twitter.com -- create and app and get the generated keys
consumer_key=""
consumer_secret=""
#Creat an access token on your pages app
access_token=""
access_token_secret=""

class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        return True
    def on_error(self, status):
        print status
if __name__ == "__main__":
    listenBot = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, listenBot)
    stream.filter(track=['Whatever we should track')



