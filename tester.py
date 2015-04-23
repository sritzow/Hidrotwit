import pymongo

conn = pymongo.MongoClient()
db = conn.tweets
items = db.tweets.find()

for item in items:
	print item
		
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
