import pymongo
<<<<<<< HEAD

conn = pymongo.MongoClient()
db = conn.tweets

items = db.tweets.find()
=======
from tester import *


masterTrends = {}
for item in items.saveWord():
    savedWords = item
    print savedWords
    for item in items.saveHash():
        if savedWords in items.saveHash():
            masterTrends[item] += 1
        elif savedWords != items.saveHash():
            masterTrends[item] = 1
print masterTrends
            
            

>>>>>>> dd411503cac64f1240ca4e379a16962134656d28
