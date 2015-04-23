import pymongo
import collections
#Player = collections.namedtuple('Player', 'score name')

conn = pymongo.MongoClient()
db = conn.tweets

def sortCount(base):
	new = {}
	for area in base.find():
		for key, value in sorted(area.iteritems(), key=lambda (k,v): (v,k), reverse = True):
			if key != '_id':
				new[key] = value
			#print key, value
	return new
	
def sort(base):
	new = {}
	for area in base.find():
		for item in area:
			if item != '_id':
				print "TWEETS:",item
				for key, value in sorted(area[item].iteritems(), key=lambda (k,v): (v,k), reverse = True):
					try:
						if key != '_id':
							new[key] = value
							#print key, value
					except:
						pass
	return new
'''					
sort(db.byname)
raw_input()

sort(db.byhash)
raw_input()
'''
#print sortCount(db.byarea)
#raw_input()

#sort(db.byword)
#raw_input()

					