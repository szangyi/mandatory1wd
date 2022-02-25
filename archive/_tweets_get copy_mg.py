from bottle import get, view, request, response, redirect
import g


##############################

# @get("/tweets")
# differentiate the path make it conditional, if there is an id do this, if no then do that
# @get("/tweets")
# @get("/tweets/<tweetid:path>")
# @view("tweets")
# # def _():
# # def _(tweetid):
# def index(tweetid='index'):
  
#   if tweetid == request.forms.get("tweet_id"):
#     print("whatw")
#   else:
#     print("ssssssss")
#     response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
#     user_session_id = request.get_cookie("user_session_id")
#     if user_session_id not in g.SESSIONS:
#       return redirect("/login")
    
#     #tweet_title = request.params.get("tweet_title")
#     #tweet_desc = request.params.get("tweet_desc")
#     user = g.SESSIONS[user_session_id]
#     # if the user is not logged in:
    
#     # return dict(user=user, tweets=g.TWEETS, tweet_title=tweet_title, tweet_desc=tweet_desc)
#     return dict(user=user, tweets=g.TWEETS)



@get("/tweets")
@view("tweets")
def _():
  response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
  user_session_id = request.get_cookie("user_session_id")
  current_tweet_id = request.query.get('update')
  # if the user is not logged in:
  if user_session_id not in g.SESSIONS:
    return redirect("/login")

  user = g.SESSIONS[user_session_id]

  
  print("#"*5)
  print("update tweet")
  print(current_tweet_id)
  
  
  
  
  # Update specific post 
  tweet_update = {}
  tweet_update_id = request.params.get("update")
  print("#"*20)
  print("udpate tweeeeeet id")
  print(tweet_update_id)
  print(tweet_update)

  # If update_post_id exists
  if tweet_update_id:
    # Loop through all posts
    for tweet in g.TWEETS:
      print("#"*15)
      print("THIS IS THE TWEET")
      print(tweet)
      # if id of the post matches update_post_id set it as update_post
      if tweet["id"] == tweet_update_id:
        tweet_update = tweet
  
  
  # return dict(user=user, tweets=g.TWEETS, current_tweet_id=current_tweet_id)
  return dict(user=user, tweets=g.TWEETS, current_tweet_id=current_tweet_id, tweet_update=tweet_update)
  