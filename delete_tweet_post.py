from bottle import post, redirect, request
import g

##############################
##############################
##############################
@post("/delete-tweet")
def _():
  # VALIDATE
  print("#")
  print("deleteeeeee")
  tweet_id = request.forms.get("tweet_id")
  # Delete the item for if enumarate
  for index, tweet in enumerate(g.TWEETS):
    if tweet["id"] == tweet_id:
      g.TWEETS.pop(index)
      return redirect("/tweets")

  return redirect("/tweets")