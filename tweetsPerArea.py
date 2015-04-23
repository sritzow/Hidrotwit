import pymongo

# Connection to Mongo DB
try:
	conn=pymongo.MongoClient()
	print "Connected successfully"
except pymongo.errors.ConnectionFailure, e:
   print "Could not establish connection:",e 
   
db = conn.tweets
tweets=db.tweets

def tweetsPerArea(tweets):
	areas={}
	for tweet in tweets.find():					#pulls tweets and iterates through each tweet
		try:
			location = tweet["place"]['name']	#gets location from tweet dict
			if location in areas:
				areas[location]+=1				#increases location count
			else:
				areas[location]=1				#adds location key
		except:
			pass
	return areas

#below lines are to test if the function does what it is supposed to	
#areas = tweetsPerArea(tweets)	
#for location in areas:
#	print areas[location],location