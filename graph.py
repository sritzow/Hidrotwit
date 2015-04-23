from byhashsort import *
import pymongo
import pygal

conn = pymongo.MongoClient()
db = conn.tweets

vals = sortCount(db.byarea)

pie_chart = pygal.HorizontalBar()
pie_chart.title = 'Tweets per Area'

total = 0
for val in vals:
	total += vals[val]
	print total
	
for val in vals:
	pie_chart.add(val, vals[val])
	
'''
pie_chart.add('New York', nyp)
pie_chart.add('Chicago', chp)
pie_chart.add('Los Angeles', lap)
'''
pie_chart.render_to_file('pie_chart.svg')  
print "rendered"