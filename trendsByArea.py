import pymongo

conn = pymongo.MongoClient()
db = conn.tweets

items = db.tweets.find()