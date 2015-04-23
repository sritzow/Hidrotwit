import tweepy
 
cons_key = 'xIvqTwnKncz4MvckyIzIzIsCh'
cons_sec = 'XlJP5xE5OyVyRcJ5MDP20KratI7juDL0KrDYSAKSAzBb0GsrWc'
acc_token = '3164465356-IpWdPyksEN5eTHKKDT8KtCHdjbgaz6sFCQ7Trm2'
acc_secret = 'onubCuaZdM3jEhcFj7HIighRuYcV7gyvhoGjWw2XByFkN'
 
auth = tweepy.auth.OAuthHandler(cons_key, cons_sec)
auth.set_access_token(acc_token, acc_secret)
api = tweepy.API(auth)

# This list will remove common words from the search results
exceptList = ['i', 'the', 'a', 'in', 'this', 'you', 'on', 'at', 'me', 'by', 'im', 'u', 'are']
 
tweets = []

hashtags = {}

cursor = tweepy.Cursor(api.search,
                       geocode='37.74533,-122.420082,50km',
                       rpp=1000,
                       result_type='recent',
                       lang='en').items(500)

for tweet in cursor:
 
    words = tweet.text.split(' ')
    finWords = []
 
    nextWord = 0 # Used to grab the next word if the current word is a verb
    lastWord = ""
 
    for word in words:
        word = word.strip('.')
        word = word.strip(',')
        word = word.strip('!')
        word = word.strip('?')
 
        #If the word is a hashtag, add it to the hashtag dictionary
        if word != '' and word != None:
            if word[0] == '#':
                if word not in hashtags.keys():
                    hashtags[word] = 1
                else:
                    hashtags[word] += 1
            elif word not in exceptList:
                word = word.lower() # Convert to lowercase

print('\n')
print("Most popular hashtags")
for word in sorted(hashtags, key=hashtags.get, reverse=True):
    try:
        print("{}: {}".format(word, hashtags[word]))
    except:
        pass # Unicode conversion can cause printing problems
print('\n')