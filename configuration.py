import tweepy
import csv
apps={
    'app1':['aVqyTxsUMnnuBUitkSCK6NOTJ','tcS3zRVGBxuFbpBaWfNV2lpTQtauGdBhILsKrfRnT60tKgCm4C','1059516754983030791-8HRSohzalbMSolsuDu6YmcLT8c8wzA','K5pCyW3xo0XohDRMWNPywpxcbY2FqQGSs1OkyQcLpOvH0'],
    'app2':['H4zHUv2RROh8AlPtJKDJwSCX6','mRBUZwTdI7p2LZMvLNALU8tOq9hYdD7AlsVeH2YKDjKD0aV8XH','1059516754983030791-bE2x4jyI9CGLZHIJ4jMgsKUikdNpQp','Alf1WubEz1FWJtb9uoQZ5N7Cy8Tym66I3GNQR3sdkyk7Z'],
    'app3':['m1wzKMqmEbLOdmb34BFCpaD5R','t5Vx7XROLbv6ZI1H2kVf13am2SmcL0c9qlzlYAa7lVRuTZtccM','1059516754983030791-mBE0lO48MyLcfsuKCrxXv7i3IT39zj','CNJM1doxOU93aXXHIHhkMKgwCJm4r59XFI08NAlNAoLRx'],
    'app4':['KhTLoSQ7x7LUuGudGsVPTTG3h','rMCanbMargdzTQX1T4KOPEzOFoW0KdCVcT6iDfWydMVcLzJpFF','1059516754983030791-RQfJJSwWzGq9eFF2lIB7ZN939wSDWr','gtZtrITLAu9O9She0LlTrvi2FcB8w5KEfHnmK4sehhwkV']
}
csvFollowers_name=open('followers_name.csv','w')
csvWriter = csv.writer(csvFollowers_name)
starting_page=1
for app in apps.values():
    apikey = app[0]
    apikeysecret = app[1]
    accesstoken = app[2]
    accesstokensecret = app[3]
    auth=tweepy.OAuthHandler(apikey,apikeysecret)
    auth.set_access_token(accesstoken,accesstokensecret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    try:
            print('follower: ' + user.screen_name)
            csvWriter.writerow([user.screen_name])
    except :
        pass
    starting_page+=25
    #for status in tweepy.Cursor(api.user_timeline, screen_name='@Cristiano', tweet_mode="extended").items():
   # print(status.full_text)