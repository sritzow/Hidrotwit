import pymongo

# Connection to Mongo DB
try:
	conn=pymongo.MongoClient()
	print "Connected successfully"
except pymongo.errors.ConnectionFailure, e:
   print "Could not establish connection:",e 
   
areas={}
db = conn.tweets
tweets=db.tweets

for i in range(tweets.count()): 			#iterates through each tweet
	tweet=tweets.find()[i]					#pulls tweet from mongo
	location = tweet["place"]['name']		#gets location from tweet dict
	if location in areas:
		areas[location]+=1					#increases location count
	else:
		areas[location]=1					#adds location key
