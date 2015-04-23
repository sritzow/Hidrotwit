import pymongo

conn = pymongo.MongoClient()
db = conn.tweets

items = db.tweets.find()
areas={'chicago' : {}, 'la' : {}, 'sanfran' : {}}
for item in items:
	user = item['user']['screen_name']
	if item['place'] != None:
		location = item["place"]['name']	#gets location from tweet dict
		if location in areas:
			area = areas[location]
			if user in area:
				area[user] += 1
			else:
				area[user] = 1
		else:
			areas[location] = {user : 1}
		
for area in areas:
	print areas[area], area