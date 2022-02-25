from bottle import post, redirect, request
import g

##############################

@post("/tweet_delete")
def _():
  tweet_id = request.forms.get("tweet_id")
  for index, tweet in enumerate(g.TWEETS):
    if tweet["id"] == tweet_id:
      g.TWEETS.pop(index)
      return redirect("/tweets")

  return redirect("/tweets")
