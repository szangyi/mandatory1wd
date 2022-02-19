from bottle import post, request, redirect, view
import uuid
import g
import time

##############################
@post("/tweets")
def _():
  # tweet_id = str(uuid.uuid4())
  # tweet_title = request.forms.get("tweet_title")
  # tweet_desc = request.forms.get("tweet_desc")

  # tweet = {
  #   "id" : tweet_id, 
  #   "title" : tweet_title,
  #   "desc" : tweet_desc,
  #   "iat" : int(time.time())
  #   }
  # g.TWEETS.append(tweet)
  # print("#"*70)
  # print("these are the tweets")
  # print(g.TWEETS)
  return
  # return dict(tweet_id=tweet_id, tweet_title=tweet_title, tweet_desc=tweet_desc)
# return redirect(f"tweets?tweet_title={tweet_title}&tweet_desc={tweet_desc}&tweet_id={tweet_id}")