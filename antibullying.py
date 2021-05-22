
import tweepy
from time import sleep

import pandas as pd

consumer_key = "AoIo5xIosZNkYxpImVq7lH8ap"
consumer_secret = "XUfpRVhvUJrRsJhSz9aGkPeOKjU3JS82YNmy8J4nBTpqsEcf41"
access_token = "1366744193457000455-JQtkQxIo6iwQ7D1m2XtRtQLCAfaYP5"
access_token_secret  = "X2cKqDhN15OR6nNe4MjeAtVx688l8NIoLOASpjbhJF7UP"
# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# twitter_data = pd.DataFrame(columns = ["id", "tm", "screen_name", "text"])

# From tweets that have mentioned me
 
username=input("Enter username")  
          
        # Authorization to consumer key and consumer secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
        # Access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret ) 
        # Calling api 
api = tweepy.API(auth) 
        # 200 tweets to be extracted 
number_of_tweets=200
tweets = api.user_timeline(screen_name=username) 
        # Empty Array 
tmp=[]  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
for j in tweets_for_csv: 
            # Appending tweets to the empty array tmp 
        tmp.append(j)  
        # Printing the tweets 
        print(tmp)

def collect_tweets(screen_name, last_tweet, api):
	tweets = []
	for tweet in api.search(q=screen_name,since_id=last_tweet):
		record = {}
		record["id"] = tweet.id
		record["tm"] = 't'
		record["screen_name"] = tweet.user.screen_name
		record["text"] = (tweet.text).encode('utf-8').strip()#tweet.text
        
		tweets.append(record)
	df = pd.DataFrame(tweets)
	return df


def write_tweet_messages(screen_name, last_tweet, last_message, outfile, api):
	df = collect_tweets(screen_name,last_tweet,api)
	
	result = [df]#,df2]
	result = pd.concat(result)
	with open(outfile, 'w') as f:
		result.to_csv(f, index = False)
		# header = False, columns = ['id','screen_name','text','tm','result']
        
        
import pandas as pd
import tweepy

import joblib

import json
import twitter
import warnings

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler = auth, wait_on_rate_limit=True, compression = True)




#print(api.direct_messages())
#api2=twitter.Api(consumer_key=consumer_key,consumer_secret=consumer_secret,access_token_key=access_token,access_token_secret=access_token_secret)
#print(api2.VerifyCredentials())
outfile = 'E:/academic/ganesh moodle material/6th semester/ISS/project/implementation/dataset/tweets_messages.csv'

with open("E:/academic/ganesh moodle material/6th semester/ISS/project/implementation/dataset/config.json") as json_file:
    config_data = json.load(json_file)

#print(json_data['screen_name'])
#print(api.me().screen_name)
#print(config_data['last_tweet'])
write_tweet_messages(screen_name = api.me().screen_name, last_tweet = config_data['last_tweet'], last_message = config_data['last_message'], outfile = outfile, api = api)
data = pd.read_csv(outfile)
model_file = 'E:/academic/ganesh moodle material/6th semester/ISS/project/implementation/dataset/clean_model.csv'
X = data['text']

loaded_model = joblib.load(model_file)
result = loaded_model.predict(X)
data['result'] = result

data.to_csv("E:/academic/ganesh moodle material/6th semester/ISS/project/implementation/dataset/results.csv")


#message = "We have detected that you have tried to bully @"+ api.me().screen_name+". Please refrain from such behaviour in future.\nYou wrote: "

message = "We have detected that you have tried to bully. Please refrain from such behaviour in future.\nYou wrote: "

for i,row in data.loc[data.result == 1].iterrows():
    if(row['tm'] == 't'):
        sent_message = message+row['text']+" \nOn: "+str(api.get_status(row['id']).created_at)
    else:
        sent_message = message+row['text']+" \nOn: "+str(api.get_direct_message(row['id']).created_at)
    api.update_status("@" + row['screen_name']+"\n You should stop bullying people. (I am a bot in testing, don't take this too seriously)",row['id'])
    #api.update_status("@" + row['screen_name']+"\n You should stop bullying people. (I am a bot in testing, don't take this too seriously)",row['id'])
    print(row['screen_name'], " ", sent_message)
    print("-"*80)
    

    

"""with open('E:/academic/ganesh moodle material/6th semester/ISS/project/implementation/dataset/config.json', 'w') as json_file:
    json.dump(config_data, json_file)"""
