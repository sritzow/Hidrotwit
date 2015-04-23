import pymongo
import time as time_ #make sure we don't override time
def millis():
    return int(round(time_.time() * 1000))
	
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
	for tweet in tweets.find(): 			#iterates through each tweet				#pulls tweet from mongo
		try:
			location = tweet["place"]['name'].replace('.', '')		#gets location from tweet dict
			if location in areas:
				areas[location]+=1					#increases location count
			else:
				areas[location]=1					#adds location key
		except:
			pass
	return areas

#below lines are to test if the function does what it is supposed to
startTime = millis()	
areas = tweetsPerArea(tweets)	
for location in areas:
	try:
		print areas[location],location
		
	except:
		pass
	raw_input()
#db = conn.tweetperarea

#db.tweetperarea.save(areas)

endTime = millis()
print "Start: ", startTime, " End: ", endTime, " time: ", (endTime - startTime)