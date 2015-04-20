import json
import mongodb
import pymongo

will be streaming language keywords and hashtags
tweettable user database to store locations and data

def tweettable(self, tweets):
	self.db = pymongo.MongoClient().tweets#placeholder for sql connection to be changed when set up
	self.db.tweets.insert(data)#inserts into db
	data = json.loads(tweets)#passes json into self.db.tweets.insert
	db.tweets.save(self, tweets)

    
    
    