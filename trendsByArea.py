from pymongo import MongoClient
from tester import *
conn = MongoClient()
db = conn.tweets

items = db.tweets.find()
#print items
for hashT in items:
    print hashT

"""
masterTrends = {}
items = db.byhash.find()
for area in items:i
	#print area
	for hashT in area:
        print hashT
        for hashTags in hashT:
            print hashTags
raw_input()           
            
"""
