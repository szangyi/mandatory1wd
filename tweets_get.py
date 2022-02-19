from bottle import get, view, request
import g


##############################
@get("/tweets")
@view("tweets")
def _():
  tweet_title = request.params.get("tweet_title")
  tweet_desc = request.params.get("tweet_desc")
  return dict(tweets=g.TWEETS, tweet_title=tweet_title, tweet_desc=tweet_desc)