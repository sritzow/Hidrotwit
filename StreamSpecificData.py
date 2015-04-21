from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json


consumer_key='xIvqTwnKncz4MvckyIzIzIsCh'
consumer_secret='XlJP5xE5OyVyRcJ5MDP20KratI7juDL0KrDYSAKSAzBb0GsrWc'

access_token='3164465356-IpWdPyksEN5eTHKKDT8KtCHdjbgaz6sFCQ7Trm2'
access_token_secret='onubCuaZdM3jEhcFj7HIighRuYcV7gyvhoGjWw2XByFkN'

class StdOutListener(StreamListener):
	def insert(data):
		self.db.tweets.insert(data)#inserts into db
		db.tweets.save(self, tweets)
		
    def on_data(self, data):
        tweets = json.loads(data)
        tweetstext = ''.join(tweets['text']).encode('utf-8')
        try:
            print(tweets['user']['location'])
            print(tweets['lang'])
            print(tweetstext)
            print(tweets['entities']['hashtags'])
            print(tweets['entities']['trends'])
			#creates connection to MongoDB and creates 'tweets' database
			
			insert(tweets)
			
        except UnicodeEncodeError:
            print('UnicodeEncodeError')
        print (' ')
        return True

    def on_error(self, status):
        print(status)
        return True

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
	self.db = pymongo.MongoClient().tweets
    stream = Stream(auth, l)
    stream.filter(locations=[-122.75,36.8,-121.75,37.8,-74,40,-73,41,-89,41,-88,42,-119,33,-117,34.5])