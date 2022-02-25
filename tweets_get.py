from bottle import get, view, request, response, redirect
import g


##############################

@get("/tweets")
@view("tweets")
def _():
  response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
  error = request.params.get("error")
  user_session_id = request.get_cookie("user_session_id")
  tweet_title = request.forms.get("tweet_title")
  tweet_desc = request.forms.get("tweet_desc")
  
  # if the user is not logged in:
  if user_session_id not in g.SESSIONS:
    return redirect("/login")

  user = g.SESSIONS[user_session_id]

  
  return dict(error=error,user=user,tweet_title=tweet_title, tweet_desc=tweet_desc, tweets = g.TWEETS)
