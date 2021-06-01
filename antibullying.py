
import tweepy
from time import sleep
from datetime import date
import seaborn as sns
import pandas as pd
       
import pandas as pd
import tweepy

import joblib

import json
import twitter
import warnings
consumer_key = "" #API
consumer_secret = ""  #API
access_token = ""  #API
access_token_secret  = ""  #API
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

tweets = api.user_timeline(screen_name=username) 
        # Empty Array 
tmp=[]
model_file = 'E:/academic/ganesh moodle material/6th semester/ISS/project/implementation/dataset/clean_model.csv' 
outfile1 = 'E:/academic/ganesh moodle material/6th semester/ISS/project/implementation/dataset/tweetswhole_messages.csv'
tmps=[] 
        # create array of tweet information: username,  
        # tweet id, date/time, text 
tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
for j in tweets_for_csv: 
    texts={}
    texts["text"]=j
    tmp.append(texts)
    tmps.append(j)  
        # Printing the tweets 
    print(tmps)
df2=pd.DataFrame(tmp)
result1 = [df2]
result1 = pd.concat(result1)
with open(outfile1, 'w') as f:
	result1.to_csv(f, index = False)
# Appending tweets to the empty array tmp 
    
data1 = pd.read_csv(outfile1)
y = data1['text']
whole=[]
loaded_model1 = joblib.load(model_file)
result1 = loaded_model1.predict(y)
whole = result1


poscount=0
negcount=0
count=0
for i in whole:
    count=count+1
    if(i==1):
        poscount=poscount+1
    else:
        negcount=negcount+1


data1["result"]=result1
print(poscount)
print(negcount)
print(count)
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
#print(api.me().screen_name)NithinZahir26
#print(config_data['last_tweet'])api.me().screen_name
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
today=date.today()
for i,row in data.loc[data.result == 1].iterrows():
    
    
    sent_message = message+row['text']+" \nOn: "+str(today)
  
    api.update_status("@" + row['screen_name']+"\n You should stop bullying people. (I am a bot in testing, don't take this too seriously)",row['id'])
    #api.update_status("@" + row['screen_name']+"\n You should stop bullying people. (I am a bot in testing, don't take this too seriously)",row['id'])
    print(row['screen_name'], " ", sent_message)
    print("-"*80)
    

    

"""with open('E:/academic/ganesh moodle material/6th semester/ISS/project/implementation/dataset/config.json', 'w') as json_file:
    json.dump(config_data, json_file)"""
