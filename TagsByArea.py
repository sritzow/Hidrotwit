import pymongo
from Rect import *
from Point import *
conn = pymongo.MongoClient()
db = conn.tweets
tweets = db.tweets.find()

def getArea(tweet):
    sf = Rect(Point(-122.75,36.8), Point(-121.75,37.8))
    ny = Rect(Point(-74,40), Point(-73,41))
    ch = Rect(Point(-89,41), Point(-88,42))
    la = Rect(Point(-119,33), Point(-117,34.5))
     
    if tweet['place'] != None:
        box = tweet['place']['bounding_box']
        coord = box['coordinates']
        loc = Rect(Point(coord[0][0][0], coord[0][0][1]), Point(coord[0][2][0], coord[0][2][1]))
        if sf.overlaps(loc):
            return "San Fran"
        if ny.overlaps(loc):
            return "New York"
        if ch.overlaps(loc):
            return "Chicago"
        if la.overlaps(loc):
            return "Los Angeles"
    return None

def tagsByArea(tweets):
    area = {}
    hashtag_list = {}
    for each in tweets:
        tweetArea = getArea(each)
        if tweetArea != None:                             
            try:
                if tweetArea in area:
                    a = area[tweetArea]
                    hashtags = each['entities']['hashtags']
                    for tags in hashtags:
                        if tags['text'] in a:
                            a[tags['text']] += 1
                        else:
                            a[tags['text']] = 1
                else:
                    area[tweetArea] = {}
                    a = area[tweetArea]
                    hashtags = each['entities']['hashtags']
                    for tags in hashtags:
                        if tags['text'] in a:
                            a[tags['text']] += 1
                        else:
                            a[tags['text']] = 1
            except:
                print 'error'
    return area


tags = tagsByArea(tweets)
for hashtags in tags:
    print hashtags, tags[hashtags]