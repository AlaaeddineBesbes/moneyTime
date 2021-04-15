from os import stat_result
import tweepy
import csv
import time
import datetime
import tkinter as tk


def show_entry_fields():
    #setting the apikeys and the access tokens
    apikey = 'zaETUhWd7e8PysLq0Pgo8spNS'
    apikeysecret = 'ixKOf4j4pLHenQlCsqCiR3yncxaEsX59t44I3IOaJfQ6p2dGrP'
    accesstoken = '1059516754983030791-APZEXSbab2ihwcGIdp9PfnJsSdRc2r'
    accesstokensecret = 'nHFstbt8dySyVJfSJuiEQbyFUtisnypWuoUgg2qIaSOxB'
    #followers list to hold the follower object
    #followers_screenNames list to hold the followers names
    followers = []
    followers_screenNames = []
    #extracting the clinet twitter screen Name and the dates to extract the tweets
    client_twitter_name=e1.get()
    startDate = e2.get()
    endDate=e3.get()
    
    #creating a csv writer to save to followers list
    csvFollowers_name=open('followers_name.csv','w')
    csvWriter = csv.writer(csvFollowers_name)

    ##creating a csv writer to save to followers tweets
    csvFollowers_tweets=open('followers_tweets.csv','w')
    csvTweetWriter = csv.writer(csvFollowers_tweets)
    #setting the auth keys to auth object 
    auth=tweepy.OAuthHandler(apikey,apikeysecret)
    auth.set_access_token(accesstoken,accesstokensecret)
    #creating the api to send the requests
    api = tweepy.API(auth,wait_on_rate_limit=True)
    #verifing the credentials 
    if(api.verify_credentials):
        print ('We successfully logged in')

    #get_followers a function that extract followers names from a given twitter account
    def get_followers(screen_name):
        print('Getting Follower list of',screen_name)
        #creating the users opbject that contains all the followers with the get followers api 
        users = tweepy.Cursor(api.followers, screen_name=screen_name,count=200)
        #ectracting the names and saving them to a csv file
        try:
            for user in users.items():
                followers.append(user)
                print(user.screen_name)
                followers_screenNames.append(user.screen_name)
                csvWriter.writerow([user.screen_name])
        except tweepy.TweepError as e:
            print(e)
        
    #followerTweets a function that extract tweets between 2 dates of all the followers
    def followerTweets(startDate,endDate):  
    #going through all the followers names  
        for screen_name in followers_screenNames:
            fol_tweets=[]
            #deleting the name from the list to keep track of the number of names left
            followers_screenNames.remove(screen_name)
            #creating the tweets object with the get user timeline api
            tweets = tweepy.Cursor(api.user_timeline,screen_name=screen_name,include_rts='false').items()
            for tweet in tweets:
                #all the tweets are in a chronological order once a tweet is more old than the start date 
                #we finish the extraction and save the tweets 
                try:
                    if tweet.created_at< endDate:
                        fol_tweets.append([tweet.text.encode('utf8'),tweet.created_at])
                        print(screen_name,tweet.text,tweet.created_at)

                    if tweet.created_at<startDate:
                        csvTweetWriter.writerow([screen_name,fol_tweets])
                        
                        break
                
                except tweepy.TweepError as e:
                    print(e)
        

    
    
    #using the functions to start the procedure of extracting
    get_followers(client_twitter_name)
    startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d')
    endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
    
    while(len(followers_screenNames)>0):
        print(len(followers_screenNames) ,"left ...")
        try:
            followerTweets(startDate,endDate)
        except tweepy.TweepError as e:
            #sometimes when sending a lot of requests twitter stops authenticating the credentials 
            #we solved this using a time sleep
            time.sleep(1)
    print("the job is done ")

    

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

tk.mainloop()

