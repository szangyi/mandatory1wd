from bottle import post, redirect, request
import g
import uuid
from time import gmtime, strftime

##############################
@post("/tweet_add")
def _():
  tweet_id = str(uuid.uuid4())  
  tweet_title = request.forms.get("tweet_title")
  tweet_desc = request.forms.get("tweet_desc")
  if len(tweet_title) < 1:
    return redirect(f"tweets?error=tweet_title&tweet_desc={tweet_desc}&tweet_title={tweet_title}")
  if len(tweet_desc) < 1:
    return redirect(f"tweets?error=tweet_desc&tweet_title={tweet_title}&tweet_desc={tweet_desc}")
  
  user_session_id = request.get_cookie("user_session_id")
  user = g.SESSIONS[user_session_id]
  
  tweet = {
    "id" : tweet_id, 
    "title" : tweet_title,
    "desc" : tweet_desc,
    "user_id": user["id"],
    "iat" : strftime("%a, %d %b %Y %H:%M", gmtime())
    }

  g.TWEETS.append(tweet)
  print("#"*70)
  print("these are the tweets")
  print(g.TWEETS)
  return redirect("/tweets")