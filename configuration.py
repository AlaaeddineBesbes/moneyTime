from os import stat_result
import tweepy
import csv
import time
import datetime
apps={
    'app1':['zaETUhWd7e8PysLq0Pgo8spNS','ixKOf4j4pLHenQlCsqCiR3yncxaEsX59t44I3IOaJfQ6p2dGrP','1059516754983030791-APZEXSbab2ihwcGIdp9PfnJsSdRc2r','nHFstbt8dySyVJfSJuiEQbyFUtisnypWuoUgg2qIaSOxB'],
    'app2':['vVvltBl3foYvGBbW7Z7myUVdC','1W5d3ZSLtx2zDDnuSnytKGTj2V5y6WKA9Nut9N0G3ROZOt2xuL','1059516754983030791-otcgBonUb0Lsg2ylFDe8uJTgNWrObJ','uDIYgrjQt94qTqlUFr11GmAKQzongM7G5KFV21ZzifJAI'],
    'app3':['9D6n7XlbRgJhystVmxU9iyXGO','AhCWmeqwyHZq2qtLUab8XBZrJONpfO6L40lbv9AvsJSyj9v4qw','1059516754983030791-8DsWRRM9YjkxOtXtOkMAKBBQtyfMmW','W7P7huIQ09MymHwY3xVg0knXrDF1Pn9pqoQqbadUmbmI0'],
    'app4':['TcBtmfZZEhegtUTGVxxScXlJM','apKx1cAfiqzU8Pn8krdCjfLYFwn9NNiWE9MsIRQwDh0J7g1yMD','1059516754983030791-uBDn9DHZmr5SLnMMyFcNRyITHLOW9m','XAx7C8csijDTthDMYAKVXHanuhCJqyZdroWxTeyVjQAVF']
}




dic_values=list(apps.values())

apikey = dic_values[0][0]
apikeysecret = dic_values[0][1]
accesstoken = dic_values[0][2]
accesstokensecret = dic_values[0][3]

followers = []
followers_screenNames = []
'''def setAPP(app_number):
    apikey = dic_values[app_number][0]
    apikeysecret = dic_values[app_number][1]
    accesstoken = dic_values[app_number][2]
    accesstokensecret = dic_values[app_number][3]
    '''


auth=tweepy.OAuthHandler(apikey,apikeysecret)
auth.set_access_token(accesstoken,accesstokensecret)
api = tweepy.API(auth,wait_on_rate_limit=False)
if(api.verify_credentials):
    print ('We successfully logged in')





def get_followers(screen_name):
    csvFollowers_name=open('followers_name.csv','w')
    csvWriter = csv.writer(csvFollowers_name)
    print('Getting Follower list of ',screen_name)
    users = tweepy.Cursor(api.followers, screen_name=screen_name,count=200)
    try:
        for user in users.items():
            
                followers.append(user)
                print(user.screen_name)
                followers_screenNames.append(user.screen_name)
                csvWriter.writerow([user.screen_name])
    except tweepy.TweepError as e:
        pass
        

def followerTweets(startDate,endDate):
    i=1
    apikey = dic_values[i][0]
    apikeysecret = dic_values[i][1]
    accesstoken = dic_values[i][2]
    accesstokensecret = dic_values[i][3]
    auth=tweepy.OAuthHandler(apikey,apikeysecret)
    auth.set_access_token(accesstoken,accesstokensecret)
    api = tweepy.API(auth,wait_on_rate_limit=False)
    csvFollowers_tweets=open('followers_tweets.csv','w')
    csvWriter = csv.writer(csvFollowers_tweets)
    fol_tweets=[]
    for screen_name in followers_screenNames:
        tweets = tweepy.Cursor(api.user_timeline,screen_name=screen_name,include_rts='false').items()
        for tweet in tweets:
            try:
                if  tweet.created_at<endDate:
                    fol_tweets.append([tweet.text,tweet.created_at])
                if tweet.created_at>startDate:
                    csvWriter.writerow([str(screen_name).encode('utf8'),str(fol_tweets).encode('utf8')])
                    break
                if i>3:
                    i=0

            except tweepy.TweepError as e:
                apikey = dic_values[i][0]
                apikeysecret = dic_values[i][1]
                accesstoken = dic_values[i][2]
                accesstokensecret = dic_values[i][3]
                auth=tweepy.OAuthHandler(apikey,apikeysecret)
                auth.set_access_token(accesstoken,accesstokensecret)
                api = tweepy.API(auth,wait_on_rate_limit=False)
                print("changing api")
                i=i+1
                break
        fol_tweets=[]


client_tweeter_name='@AbdoulMajidBar3'
get_followers(client_tweeter_name)
startDate = datetime.datetime(2021,3,1)
endDate =  datetime.datetime(2021,4,11)           
followerTweets(startDate,endDate)
