#### this is my closest to getting words per area so far!!!
import pymongo

try:
	conn=pymongo.MongoClient()
	print "Established Connection"
except pymongo.errors.ConnectionFailure:
	print "Connection Failed, Womp Womp..."

db = conn.tweets #ok
items = db.tweets.find() #ok
words = tweet.text.split(' ') #? what is tweet in this case
words = [0] #?

for word in item[]: #Do you mean items?
	print item
	if len(word) in item <= 3: #you are looping through each word already no need to check if in item
		item.remove(word) #why remove word?
		print "Item Removed"
	else:
		words.append(word) and words.count(word) #not sure if this works o.o

print words
print words.count
		
