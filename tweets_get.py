from bottle import get, view, request, response, redirect
import g


##############################
@get("/tweets")
@view("tweets")
def _():
  response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
  user_session_id = request.get_cookie("user_session_id")
  if user_session_id not in g.SESSIONS:
    return redirect("/login")
  
  tweet_title = request.params.get("tweet_title")
  tweet_desc = request.params.get("tweet_desc")
  user = g.SESSIONS[user_session_id]
  # if the user is not logged in:
  
  return dict(user=user, tweets=g.TWEETS, tweet_title=tweet_title, tweet_desc=tweet_desc)