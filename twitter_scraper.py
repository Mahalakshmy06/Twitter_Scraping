

# Program for Twitter Scraping using MongoDB and streamlit

# Necessary modules are imported
import snscrape.modules.twitter as sntwitter
import streamlit as st
import pandas as pd
import pymongo
from pymongo import MongoClient
from PIL import Image
from datetime import date
import json


# MongoDB client connection is done
client = pymongo.MongoClient("mongodb+srv://Mahalakshmy:Maha14@cluster0.efcoclm.mongodb.net/test?retryWrites=true&w=majority")
twtdb = client.Twitter
twtdb_main = twtdb.Tweets

# Here starts the main function
def main():
  tweets = 0
  st.title("Twitter Scraping 📃 ")

  st.sidebar.image("https://miro.medium.com/v2/resize:fit:1400/0*x4tolX7h2WvXZxCM" , use_column_width = True)
  st.sidebar.header("Scrapping App Menu 👇")
  # Menus used in Twitter Scrape web app -- 5 menus are used
  menu = ["Home","About","Search","View Data","Download"]
  choice = st.sidebar.selectbox("",menu)
  
  # Menu 1 is Home page 
  if choice=="Home":
    st.write('''This application is a Twitter Scraping web app created using Streamlit. 
             It scrapes the twitter data using snscrape for the given hashtag/ keyword for the given period.
             The tweets are then viewed and uploaded in MongoDB and can be dowloaded as CSV or a JSON file.''')

  # Menu 2 is about the Twitter Scrape libraries, databases and apps
  elif choice=="About":
    # Info about Twitter Scrapper
    with st.expander("Twitter Scrapper"):
      st.write('''Twitter Scraper will scrape the data from Public Twitter profiles and easily gather data on
                  a specific user's tweets and use it to gain insights.It will collect the data about **date, id, url, tweet content, users/tweeters,reply count, 
                  retweet count, language, source, like count, followers, friends** and lot more information 
                  to gather the real facts about the Tweets.''')

    # Info about Snscraper
    with st.expander("Snscraper"):
      st.write('''Snscrape is a scraper for social networking services like *twitter, faceboook, instagram and so on*. 
                   It scrapes required things like **user profiles, hashtages, other tweet information** and returns the discovered items from the relavent posts/tweets.''')

    # Info about MongoDB database
    with st.expander("Mongodb"):
      st.write('''MongoDB is an open source document database used for storing unstructured data. The data is stored as JSON like documents called BSON. It is classified as a NoSQL Database.
                  It is used by developers to work easily with real time data analytics, content management and lot of other web applications.''')

    # Info about Streamlit framework
    with st.expander("Streamlit"):
      st.write('''Streamlit is a **awesome opensource framework used for building highly interactive shareable web applications** in python language. 
                  It's easy to share *machine learning and data sciecne web apps* using streamlit. Using this beautiful web apps can be created in minutes.
                  It allows the app to load the large set of datas from web for manipulation and  performing expensive computations.''')

  # Menu 3 is a search option
  elif choice=="Search":
    # Every time after the last tweet the database will be cleared for updating new scraping data
    twtdb_main.delete_many({})

    # Form for collecting user input for twitter scrape
    with st.form(key='form1'):
      # Hashtag input
      st.subheader("Tweet searching Form 🔍")
      st.write("Enter the hashtag or keyword to perform the twitter scraping. Use # or within double quotes")
      query = st.text_input('Hashtag or keyword')

      # No of tweets for scraping
      st.write("Enter the limit for the data scraping: Maximum limit is 1000 tweets")
      limit = st.number_input('Insert a number',min_value=0,max_value=1000,step=10)

      # From date to end date for scraping
      st.write("Enter the Starting date to scrap the tweet data")
      start = st.date_input('Start date')
      end = st.date_input('End date')
      
      # Submit button to scrap
      submit_button = st.form_submit_button(label="Tweet Scrap")
    
    if submit_button:
      st.success(f"Tweet hashtag {query} received for scraping".format(query))

      # TwitterSearchScraper will scrape the data and insert into MongoDB database
      for tweet in sntwitter.TwitterSearchScraper(f'from:{query} since:{start} until:{end}').get_items():
        # To verify the limit if condition is set
        if tweets == limit:
          break
        # Stores the tweet data into MongoDB until the limit  is reached
        else:      
          new = {"date":tweet.date,"user":tweet.user.username, "url":tweet.url, "followersCount":tweet.user.followersCount, "friendsCount":tweet.user.friendsCount, "favouritesCount":tweet.user.favouritesCount,"mediaCount":tweet.user.mediaCount}
          twtdb_main.insert_one(new)
          tweets += 1
      
      # Display the total tweets scraped
      df = pd.DataFrame(list(twtdb_main.find()))
      cnt = len(df)
      st.success(f"Total number of tweets scraped for the input query is := {cnt}".format(cnt))

  # Menu 4 is for displying the data uploaded in MongoDB
  elif choice=="View Data":
    # Save the documents in a dataframe
    df = pd.DataFrame(list(twtdb_main.find()))
    #Display the document 
    st.dataframe(df)  

  # Menu 5 is for Downloading the scraped data as CSV or JSON
  else:
    col1, col2 = st.columns(2)

    # Download the scraped data as CSV
    with col1:
      st.write("Download the tweet data as CSV File")
      # save the documents in a dataframe
      df = pd.DataFrame(list(twtdb_main.find()))
      # Convert the dataframe to csv
      df.to_csv('twittercsv.csv')
      def convert_df(data):
        # Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')
      csv = convert_df(df)
      st.download_button(
                        label="Download data as CSV",
                        data=csv,
                        file_name='twittercsv.csv',
                        mime='text/csv',
                        )
      st.success("Successfully Downloaded data as CSV")

    # Download the scraped data as JSON
    with col2:
      st.write("Download the tweet data as JSON File")
      # Convert dataframe to json string instead as json file 
      twtjs = df.to_json(default_handler=str).encode()
      # Create Python object from JSON string data
      obj = json.loads(twtjs)
      js = json.dumps(obj, indent=4)
      st.download_button(
                        label="Download data as JSON",
                        data=js,
                        file_name='twtjs.js',
                        mime='text/js',
                        )

      st.success("Successfully Downloaded data as JSON")
      
# Call the main function
main()

