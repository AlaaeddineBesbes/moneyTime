from os import stat_result
import tweepy
import csv
import time
import datetime
import tkinter as tk

client_tweeter_name=""
def show_entry_fields():
    client_tweeter_name= str(e1.get())
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

    csvFollowers_name=open('followers_name.csv','w')
    csvWriter = csv.writer(csvFollowers_name)

    csvFollowers_tweets=open('followers_tweets.csv','w')
    csvTweetWriter = csv.writer(csvFollowers_tweets)
    auth=tweepy.OAuthHandler(apikey,apikeysecret)
    auth.set_access_token(accesstoken,accesstokensecret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    if(api.verify_credentials):
        print ('We successfully logged in')


    def get_followers(screen_name):
        print('Getting Follower list of',screen_name)
        users = tweepy.Cursor(api.followers, screen_name=screen_name,count=200)
        try:
            for user in users.items():
                followers.append(user)
                print(user.screen_name)
                followers_screenNames.append(user.screen_name)
                csvWriter.writerow([user.screen_name])
        except tweepy.TweepError as e:
            print(e)
        

    def followerTweets(startDate,endDate):
        
        fol_tweets=[]
        for screen_name in followers_screenNames:
            followers_screenNames.remove(screen_name)
            tweets = tweepy.Cursor(api.user_timeline,screen_name=screen_name,include_rts='false').items()
            for tweet in tweets:
                try:
                    if tweet.created_at< endDate:
                        fol_tweets.append([tweet.text.encode('utf8'),tweet.created_at])
                        print(screen_name,tweet.text,tweet.created_at)
                    if tweet.created_at<startDate:
                        csvTweetWriter.writerow([screen_name,fol_tweets])
                        
                        break
                
                except tweepy.TweepError as e:
                    print(e)
        fol_tweets=[]

    startDate = e2.get()
    endDate=e3.get()
    

    get_followers(client_tweeter_name)
    date_time_str = '2018-06-29 08:15:27.243860'
    startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d')
    endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
    while(len(followers_screenNames)>0):
        print(len(followers_screenNames))
        try:
            followerTweets(startDate,endDate)
        except tweepy.TweepError as e:
            
            time.sleep(1)

    

interface = tk.Tk()

interface.title("Money Time")
interface.geometry("400x200")
tk.Label(interface, 
         text="Money Time, la plateforme qui vous permet \n d'automatiser vos recherches sur twitter!").grid(row=0)
tk.Label(interface, 
         text="Choisir le tweetos").grid(row=1)
tk.Label(interface, 
         text="        Choisir votre intervalle").grid(row=2)
tk.Label(interface, 
         text="Date de départ (Y-M-D)").grid(row=4)
tk.Label(interface, 
         text="Date de fin  (Y-M-D)").grid(row=5)




e1 = tk.Entry(interface)
e2 = tk.Entry(interface)
e3 = tk.Entry(interface)

e1.grid(row=1, column=1)
e2.grid(row=4, column=1)
e3.grid(row=5, column=1)



tk.Button(interface, 
          text='Valider', command=show_entry_fields).place(x=200,y=150)

print(client_tweeter_name)
tk.mainloop()

