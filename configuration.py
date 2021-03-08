from os import stat_result
import tweepy
import csv
import time
import datetime
apps={
    'app1':['6HrUE4jOeiji0rFHal0IJAoyQ','T0uFpIDdUVfIDALPwUYl5MIOycJ8TNVebafUxcYcy6uglO8cUi','1059516754983030791-hy17of2OaUWvdLSS6cRE05ShBQX21t','cHX1s2F4wYfMuDKBtqK1n1Mp1bzdTJVkGI5AteicW6EEF'],
    'app2':['H4zHUv2RROh8AlPtJKDJwSCX6','mRBUZwTdI7p2LZMvLNALU8tOq9hYdD7AlsVeH2YKDjKD0aV8XH','1059516754983030791-bE2x4jyI9CGLZHIJ4jMgsKUikdNpQp','Alf1WubEz1FWJtb9uoQZ5N7Cy8Tym66I3GNQR3sdkyk7Z'],
    'app3':['m1wzKMqmEbLOdmb34BFCpaD5R','t5Vx7XROLbv6ZI1H2kVf13am2SmcL0c9qlzlYAa7lVRuTZtccM','1059516754983030791-mBE0lO48MyLcfsuKCrxXv7i3IT39zj','CNJM1doxOU93aXXHIHhkMKgwCJm4r59XFI08NAlNAoLRx'],
    'app4':['KhTLoSQ7x7LUuGudGsVPTTG3h','rMCanbMargdzTQX1T4KOPEzOFoW0KdCVcT6iDfWydMVcLzJpFF','1059516754983030791-RQfJJSwWzGq9eFF2lIB7ZN939wSDWr','gtZtrITLAu9O9She0LlTrvi2FcB8w5KEfHnmK4sehhwkV']
}

apikey = '6HrUE4jOeiji0rFHal0IJAoyQ'
apikeysecret = 'T0uFpIDdUVfIDALPwUYl5MIOycJ8TNVebafUxcYcy6uglO8cUi'
accesstoken = '1059516754983030791-hy17of2OaUWvdLSS6cRE05ShBQX21t'
accesstokensecret = 'cHX1s2F4wYfMuDKBtqK1n1Mp1bzdTJVkGI5AteicW6EEF'
dic_values=list(apps.values())
'''def setAPP(app_number):
    apikey = dic_values[app_number][0]
    apikeysecret = dic_values[app_number][1]
    accesstoken = dic_values[app_number][2]
    accesstokensecret = dic_values[app_number][3]
setAPP(3)
'''
auth=tweepy.OAuthHandler(apikey,apikeysecret)
auth.set_access_token(accesstoken,accesstokensecret)
api = tweepy.API(auth,wait_on_rate_limit=True)
if(api.verify_credentials):
    print ('We successfully logged in')
screen_name='@elonmusk'
def get_followers(screen_name):
    csvFollowers_name=open('followers_name.csv','w')
    csvWriter = csv.writer(csvFollowers_name)
    print('Getting Follower list of ',screen_name)
    followers = []
    followers_screenNames = []
    users = tweepy.Cursor(api.followers, screen_name=screen_name, wait_on_rate_limit=True,count=200)
    for user in users.items():
        try:
            followers.append(user)
            print(user.screen_name)
            followers_screenNames.append(user.screen_name)
            csvWriter.writerow([user.screen_name])
        except tweepy.TweepError as e:
            print("Going to sleep:", e)
            time.sleep(60)

    
def followerTweets(screen_name):
    startDate = datetime.datetime(2021,3,1)
    endDate =   datetime.datetime(2021,3,8)
    tweets = tweepy.Cursor(api.user_timeline,screen_name=screen_name,include_rts='false').items()
    for tweet in tweets:
        if tweet.created_at>startDate and tweet.created_at<endDate:
            print(tweet.text)
followerTweets('@Univ_Savoie')