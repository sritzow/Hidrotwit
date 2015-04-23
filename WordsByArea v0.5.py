#### this is my closest to getting words per area so far!!!
import pymongo

try:
	conn=pymongo.MongoClient()
	print "Established Connection"
except pymongo.errors.ConnectionFailure:
	print "Connection Failed, Womp Womp..."

db = conn.tweets
items = db.tweets.find()
words = tweet.text.split(' ')
words = [0]

for word in item[]:
	print item
	if len(word) in item <= 3:
		item.remove(word)
		print "Item Removed"
	else:
		words.append(word) and words.count(word)

print words
print words.count
		