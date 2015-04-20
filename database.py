import json
import mongodb
import pymongo

#will be streaming language keywords and hashtags
#tweettable user database to store locations and data

def tweettable(self, tweets):
	self.db = pymongo.MongoClient().tweets#creates connection to MongoDB and creates 'tweets' database
	self.db.tweets.insert(data)#inserts into db
	data = json.loads(tweets)#passes json into self.db.tweets.insert
	db.tweets.save(self, tweets)