import pymongo
import time as time_ #make sure we don't override time

"""Point and Rectangle classes.

This code is in the public domain.

Point  -- point with (x,y) coordinates
Rect  -- two points, forming a rectangle
"""
def millis():
    return int(round(time_.time() * 1000))
	
conn = pymongo.MongoClient()
db = conn.tweets

items = db.tweets.find()

def tweetCount():
	db.tweets.count()
	
def countByWord():
	area = {}
	for item in items:
		text = item['text']
		if item["place"] != None:
			if item["place"]['name'] in area:
				a = area[item["place"]['name']]
				for word in text.split(" "):
					word = word.strip(',.@#').lower()
					if len(word) >= 3 and not word.startswith('\\'):
						if word in a:
							a[word] += 1
						else:
							a[word] = 1
			else:
				area[item['place']['name']] = {}
				a = area[item["place"]['name']]
				for word in text.split(" "):
					word = word.strip(',.@#').lower()
					if len(word) >= 3 and not word.startswith('\\'):
						if word in a:
							a[word] += 1
						else:
							a[word] = 1
	return area
	
def countByName():
	area = {}
	for item in items:
		user = item['user']['screen_name']
		if item["place"] != None:
			if item["place"]['name'] in area:
				a = area[item["place"]['name']]
				if user in a:
					a[user] += 1
				else:
					a[user] = 1
			else:
				area[item["place"]['name']] = {user : 1}			
	return area
	
def countByHash():
	area = {}
	for item in items:
		for hashs in item['entities']['hashtags']:
			#print hashs['text']
			if item["place"] != None:
				if item["place"]['name'] in area:
					a = area[item["place"]['name']]
					if hashs['text'] in a:
						a[hashs['text']] += 1
					else:
						a[hashs['text']] = 1
				else:
					area[item['place']['name']] = {hashs['text'] : 1}			
	return area
	
def countByArea():
	area = {}
	for item in items:
		if item["place"] != None:
			if item["place"]['name'] in area:
				area[item["place"]['name']] += 1
			else:
				area[item["place"]['name']] = 1	
	return area
	
startTime = millis()
print tweetCount()
areas = countByHash()


for area in areas:
	print area, areas[area]
	raw_input()
endTime = millis()

print "Start: ", startTime, " End: ", endTime, " time: ", (endTime - startTime)
		