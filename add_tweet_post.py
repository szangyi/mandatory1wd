from bottle import post, redirect, request
import g
import uuid
import time
from time import gmtime, strftime

##############################
##############################
##############################
@post("/add_tweet")
def _():
  tweet_id = str(uuid.uuid4())
  tweet_title = request.forms.get("tweet_title")
  tweet_desc = request.forms.get("tweet_desc")
  
  tweet = {
    "id" : tweet_id, 
    "title" : tweet_title,
    "desc" : tweet_desc,
    # "iat" : int(time.time()),
    "iat" : strftime("%a, %d %b %Y %H:%M", gmtime())
    }
  
  g.TWEETS.append(tweet)
  print("#"*70)
  print("these are the tweets")
  print(g.TWEETS)
  return redirect("/tweets")