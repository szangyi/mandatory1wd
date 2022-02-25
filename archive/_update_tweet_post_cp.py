from bottle import post, redirect, request, get, view, put
import g

##############################

# @post("/update_tweet")
# def _():
#   print("UPDAAAAAATE")
#   tweet_id = request.forms.get("tweet_id")
#   tweet_button_action = request.forms['submit']

#   if tweet_button_action == "delete":
#     tweet_id = request.forms.get("tweet_id")
#     for index, tweet in enumerate(g.TWEETS):
#       if tweet["id"] == tweet_id:
#         g.TWEETS.pop(index)
#         return redirect("/tweets")

#   elif tweet_button_action == "update":
#     for index, tweet in enumerate(g.TWEETS):
#       if tweet["id"] == tweet_id:
#         tweet_title = request.forms.get("tweet_title")
#         tweet_desc = request.forms.get("tweet_desc")
#         g.TWEETS[index]["tweet_title"] = tweet_title
#         g.TWEETS[index]["tweet_desct"] = tweet_desc
#         # return redirect("/tweets")
#         return redirect("/tweets")
      
  
# @put("/tweets/<tweet_id>") 
# def _(tweet_id): 
#   print('#'*10)
#   print('updaaaaate')
#   tweets = g.TWEETS
#   new_tweet_title = request.forms.get("tweet_title") 
#   new_tweet_desc = request.forms.get("tweet_desc") 
#   tweets[int(tweet_id)] = {"id": tweet_id, "title": new_tweet_title, "desc": new_tweet_desc} 
#   return redirect("/items")    
    
    

@post("/tweet_update")
def _():
  # Grab post["id"] from the form
  current_tweet_id = request.forms.get("tweet_id")
  print("#"*5)
  print("update tweet")
  print(current_tweet_id)
  # if tweet_id:
  # Loop through posts
  for index, tweet in enumerate(g.TWEETS):
    # If post["id"] matches post_id update the value of post_content with data from the form
    if tweet["id"] == current_tweet_id:
      tweet["tweet_title"] = request.forms.get("new_tweet_title")
      tweet["tweet_desc"] = request.forms.get("new_tweet_desc")
  return redirect("/tweets")
      
# @get("/tweets/<tweetid:path>")
# @view("tweets")
# def _(tweetid):
#   print("#"*5)
#   print("path view")
#   return