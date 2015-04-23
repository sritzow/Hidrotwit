import pymongo

conn = pymongo.MongoClient()
db = conn.tweets
tweets = db.tweets.find()

def tagsByArea(tweets):
    hashtag_list = {}
    for each in tweets:                             
        try:
            hashtags = each['entities']['hashtags']
            for tags in hashtags:
                if tags['text'] in hashtag_list:
                    hashtag_list[tags['text']] += 1                 
                else:
                    hashtag_list[tags['text']] = 1                  
        except:
            print 'error'
    return hashtag_list


tags = tagsByArea(tweets)
for hashtags in tags:
    print tags[hashtags],hashtags



'''import pymongo

conn = pymongo.MongoClient()
db = conn.tweets
tweets = db.tweets.find()

def tagsByArea(tweets):
    hashtag_list = {}
    area = {}
    for each in tweets:                             
        try:
            hashtags = each['entities']['hashtags']
            for tags in hashtags:
                if each['place'] != None:
                    if each['place']['name'] in area:
                        area = hashtag_list[each['place']['name']]
                        if tags['text'] in area:
                            area[tags['text']] += 1                 
                        else:
                            area[tags['text']] = 1
        except:
            pass
    return area


tags = tagsByArea(tweets)
for hashtags in tags:
    print tags[hashtags],hashtags'''