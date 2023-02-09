from googleapiclient.discovery import build 
import pandas as pd
from IPython.display import JSON
from dateutil import parser
import isodate

#import data visualization packages

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#import NLP package for wordcloud
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
from wordcloud import WordCloud


api_key= 'AIzaSyDXOWxWVdocxNJYLxKrjyJQR9vGKo011O4'
api_service_name = "youtube"
api_version = "v3"
channel_ids = ["UC5_4POQX0WtMhUpRsh-YQhA","UCJQJAI7IjbLcpsjWdSzYz0Q"
              #to add more channel ids
              ]
youtube = build(api_service_name, api_version, developerKey=api_key)

#function to return channel statistics

def getChannelStats(youtube,channel_ids):
    
    stat_data=[];
    
    request = youtube.channels().list(part="snippet,contentDetails,statistics",id=",".join(channel_ids))
    response = request.execute()
    
    #looping through each channel item & creating a dictionary
    for item in response["items"]:
        data={"ChannelName": item["snippet"]["title"],
              "SubscribersCount" : item["statistics"]["subscriberCount"],
              "NoofVideos" : item["statistics"]["videoCount"],
              "Playlist" : item["contentDetails"]["relatedPlaylists"]["uploads"]
             }
        stat_data.append(data)
        
    #returning channel stat as a dataframe    
    return(stat_data)


