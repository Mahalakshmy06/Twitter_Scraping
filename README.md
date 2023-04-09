![TS](https://www.bestproxyreviews.com/wp-content/uploads/2020/05/Twitter-scraping.jpg)

# TWITTER SCRAPING
Scraping is a technique to get information from Social Network sites. It scrapes the twitter data using snscrape for the given hashtag/ keyword for the given period. The tweets are uploaded in MongoDB and can be dowloaded as CSV or a JSON file. Analysing tweets, shares, likes, URLs and interests is a powerful way to derive insight into public conversations.


# Acknowledgements
-[GUVI](https://www.guvi.in/)

-Mentor Mr.K.Balachandar

# Tech Stack
**Language:** Python ; 
**NoSQL Database:** MongoDB ;
**GUI Framework:** Streamlit

# Libraries and Modules needed for the project!
 1. snscrape.modules.twitter - (To Scrape the Data from Twitter)
 2. Pandas - (To Create a DataFrame with the scraped data)
 3. Pymongo - (To upload the dataframe to MongoDB database)
 4. Streamlit - (To Create Graphical user Interface)
 5. Datetime - (To get the current date)
 
 ## Scraping the tweet
 To scrap the data Snscrape python library is used. The TweetSearchScrape() method scrape the Twitter data without Twitter API. The method is passed with a query connecting the hashtag to be search and with start date and end date.
 
 ## Used Streamlit app for creating the GUI. Used menus for searching, displaying the tweets and to download. 

**Menu 1 -- Home**  
Home page of the UI conatins title of the app

**Menu 2 -- About**  
Contains some description about the Twitter Scraping, Snscrape library, MongoDB and Streamlit framework.

**Menu 3 -- Search**  
It is used to search the tweet data using the #hashtag and for given dates and also within double quotes of profile name. 

**Menu 4 -- View Data**  
The scraped data from the MongoDB database are displayed as a DataFrame (using pandas).

**Menu 5 -- Download**  
The scraped data from the MongoDB database can be downloaded in CSV/ JSON file formats as per the requirements.

## Run
  To run this script go to the Terminal and type the below command, you will get a new window opened in your browser there we can interact with the streamlit user interface.
    
    	streamlit run twitter_scraper.py
