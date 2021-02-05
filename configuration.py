import tweepy
import csv
apikey = 'oejOwGdz7oKpvxMVEkudXiQwX'
apikeysecret = 'vhKp8C3y62nEJN6ZS3FXTN6SxMR1lJ5RERmAq0Bw2xOpwsj1Ry'
accesstoken = '1059516754983030791-lHBrkm9TZ88nQ10ZGvSGBGRzZUlgZA'
accesstokensecret = 'aZGKDETXIAFV8ixUfAbPxINe9k0c2tN7HNq3wAPUCJbyA'
auth=tweepy.OAuthHandler(apikey,apikeysecret)
auth.set_access_token(accesstoken,accesstokensecret)
api = tweepy.API(auth,wait_on_rate_limit=True)
csvFollowers_name=open('followers_name.csv','w')
csvWriter = csv.writer(csvFollowers_name)
for user in tweepy.Cursor(api.followers, screen_name="@TechCrunch").items():
    print('follower: ' + user.screen_name)
    csvWriter.writerow([user.screen_name])
  

    #for status in tweepy.Cursor(api.user_timeline, screen_name='@Cristiano', tweet_mode="extended").items():
   # print(status.full_text)