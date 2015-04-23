Geo = 'geo'

locations = {
    'SanFran': {
        Geo:'enter geodata'},
    'NewYork': {
        Geo:'enter geodata'},
    'LosAng': {
        Geo:'enter geodata'},
    'Chic': {
        Geo:'enter geodata'},
    }

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